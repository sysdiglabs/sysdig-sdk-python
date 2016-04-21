import os
import json
import requests
import copy

class SdcClient:
    userinfo = None
    n_connected_agents = None
    lasterr = None

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com'):
        self.token = os.environ.get("SDC_TOKEN", token)
        self.hdrs = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        self.url = os.environ.get("SDC_URL", sdc_url)

    def __checkResponse(self, res):
        if res.status_code >= 300:
            errorcode = res.status_code
            self.lasterr = None

            try:
                j = res.json()
            except:
                self.lasterr = 'status code ' + str(errorcode)
                return False

            if 'errors' in j:
                if 'message' in j['errors'][0]:
                    self.lasterr = j['errors'][0]['message']

                if 'reason' in j['errors'][0]:
                    if self.lasterr is not None:
                        self.lasterr += ' '
                    else:
                        self.lasrerr = ''

                    self.lasterr += j['errors'][0]['reason']
            elif 'message' in j:
                self.lasterr = j['message']
            else:
                self.lasterr = 'status code ' + str(errorcode)
            return False
        return True

    def get_user_info(self):
        if self.userinfo is None:
            res = requests.get(self.url + '/api/user/me', headers=self.hdrs)
            if not self.__checkResponse(res):
                return [False, self.lasterr]
            self.userinfo = res.json()
        return [True, self.userinfo]

    def get_connected_agents(self):
        res = requests.get(self.url + '/api/agents/connected', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data['agents']]

    def get_n_connected_agents(self):
        res = requests.get(self.url + '/api/agents/connected', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        data = res.json()
        return [True, data['total']]

    def get_alerts(self):
        res = requests.get(self.url + '/api/alerts', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_notifications(self, from_ts, to_ts, state=None, resolved=None):
        params = {}

        if from_ts is not None:
            params['from'] = from_ts * 1000000

        if to_ts is not None:
            params['to'] = to_ts * 1000000

        if state is not None:
            params['state'] = state

        if resolved is not None:
            params['resolved'] = resolved

        res = requests.get(self.url + '/api/notifications', headers=self.hdrs, params=params)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def update_notification_resolution(self, notification, resolved):
        if 'id' not in notification:
            return [False, "Invalid notification format"]

        notification['resolved'] = resolved
        data = {'notification': notification}

        res = requests.put(self.url + '/api/notifications/' + str(notification['id']), headers=self.hdrs, data=json.dumps(data))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def create_alert(self, name, description, severity, for_atleast_s, condition, segmentby=[],
                     segment_condition='ANY', user_filter='', notify='', enabled=True, annotations={}):
        #
        # Get the list of alerts from the server
        #
        res = requests.get(self.url + '/api/alerts', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        j = res.json()

        #
        # If this alert already exists, don't create it again
        #
        for db in j['alerts']:
            if 'description' in db:
                if db['description'] == description:
                    return [False, 'alert ' + name + ' already exists']

        #
        # Populate the alert information
        #
        alert_json = {
            'alert' : {
                'type' : 'MANUAL',
                'name' : name,
                'description' : description,
                'enabled' : enabled,
                'severity' : severity,
                'timespan' : for_atleast_s * 1000000,
                'condition' : condition,
                'filter': user_filter
            }
        }

        if segmentby != None and segmentby != []:
            alert_json['alert']['segmentBy'] = segmentby
            alert_json['alert']['segmentCondition'] = {'type' : segment_condition}

        if annotations != None and annotations != {}:
            alert_json['alert']['annotations'] = annotations

        if notify != None and notify != []:
            alert_json['alert']['notify'] = notify

        #
        # Create the new alert
        #
        res = requests.post(self.url + '/api/alerts', headers=self.hdrs, data=json.dumps(alert_json))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def delete_alert(self, alert):
        if 'id' not in alert:
            return [False, "Invalid alert format"]

        res = requests.delete(self.url + '/api/alerts/' + str(alert['id']), headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]

        return [True, None]

    def get_notification_settings(self):
        res = requests.get(self.url + '/api/settings/notifications', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def set_notification_settings(self, settings):
        res = requests.put(self.url + '/api/settings/notifications', headers=self.hdrs,
                           data=json.dumps(settings))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def add_email_notification_recipient(self, email):
        #
        # Retirieve the user's notification settings
        #
        res = requests.get(self.url + '/api/settings/notifications', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        j = res.json()

        #
        # Enable email notifications
        #
        j['userNotification']['email']['enabled'] = True

        #
        # Add the given recipient
        #
        if email not in j['userNotification']['email']['recipients']:
            j['userNotification']['email']['recipients'].append(email)
        else:
            return [False, 'notification target ' + email + ' already present']

        return self.set_notification_settings(j)

    def get_explore_grouping_hierarchy(self):
        res = requests.get(self.url + '/api/groupConfigurations', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]

        data = res.json()

        if 'groupConfigurations' not in data:
            return [False, 'corrupted groupConfigurations API response']

        gconfs = data['groupConfigurations']

        for gconf in gconfs:
            if gconf['id'] == 'explore':
                res = []
                items = gconf['groups'][0]['groupBy']

                for item in items:
                    res.append(item['metric'])

                return [True, res]

        return [False, 'corrupted groupConfigurations API response, missing "explore" entry']

    def get_data_retention_info(self):
        res = requests.get(self.url + '/api/history/timelines/', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_topology_map(self, grouping_hierarchy, time_window_s, sampling_time_s):
        #
        # Craft the time interval section
        #
        tlines = self.get_data_retention_info()

        for tline in tlines[1]['agents']:
            if tline['sampling'] == sampling_time_s * 1000000:
                timeinfo = tline

        if timeinfo is None:
            return [False, "sampling time " + str(sampling_time_s) + " not supported"]

        timeinfo['from'] = timeinfo['to'] - timeinfo['sampling']

        #
        # Create the grouping hierarchy
        #
        gby = [{'metric': g} for g in grouping_hierarchy]

        #
        # Prepare the json
        #
        req_json = {
            'format': {
                'type': 'map',
                'exportProcess': True
            },
            'time': timeinfo,
            #'filter': {
            #    'filters': [
            #        {
            #            'metric': 'agent.tag.Tag',
            #            'op': '=',
            #            'value': 'production-maintenance',
            #            'filters': None
            #        }
            #    ],
            #    'logic': 'and'
            #},
            'limit': {
                'hostGroups': 20,
                'hosts': 20,
                'containers': 20,
                'processes': 10
            },
            'group': {
                'configuration': {
                    'groups': [
                        {
                            'filters': [],
                            'groupBy': gby
                        }
                    ]
                }
            },
            'nodeMetrics': [
                {
                    'id': 'cpu.used.percent',
                    'aggregation': 'timeAvg',
                    'groupAggregation': 'avg'
                }
            ],
            'linkMetrics': [
                {
                    'id': 'net.bytes.total',
                    'aggregation': 'timeAvg',
                    'groupAggregation': 'sum'
                }
            ]
        }

        #
        # Fire the request
        #
        res = requests.post(self.url + '/api/data?format=map', headers=self.hdrs,
                            data=json.dumps(req_json))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_views_list(self):
        res = requests.get(self.url + '/data/drilldownDashboardDescriptors.json', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_view(self, name):
        gvres = self.get_views_list()
        if gvres[0] is False:
            return gvres

        vlist = gvres[1]['drilldownDashboardDescriptors']

        id = None

        for v in vlist:
            if v['name'] == name:
                id = v['id']
                break

        if not id:
            return [False, 'view ' + name + ' not found']

        res = requests.get(self.url + '/data/drilldownDashboards/' + id + '.json', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_dashboards(self):
        res = requests.get(self.url + '/ui/dashboards', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def find_dashboard_by(self, name=None):
        res = self.get_dashboards()
        if res[0] is False:
            return res
        else:
            def filter_fn(configuration):
                return configuration['name'] == name
            def create_item(configuration):
                return {'dashboard': configuration}

            dashboards = map(create_item, filter(filter_fn, res[1]['dashboards']))
            return [True, dashboards]

    def create_dashboard(self, name):
        dashboard_configuration = {
            'name':   name,
            'schema': 1,
            'items':  []
        }

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, res.json()]

    def add_dashboard_panel(self, dashboard, name, panel_type, metrics, scope=None, sort_by=None, limit=None, layout=None):
        panel_configuration = {
            'name':                 name,
            'showAs':               None,
            'showAsType':           None,
            'metrics':              [],
            'gridConfiguration':    {
                'col':      1,
                'row':      1,
                'size_x':   12,
                'size_y':   6
            }
        }

        if panel_type == 'timeSeries':
            #
            # In case of a time series, the current dashboard implementation
            # requires the timestamp to be explicitly specified as "key".
            # However, this function uses the same abstraction of the data API
            # that doesn't require to specify a timestamp key (you only need to
            # specify time window and sampling)
            #
            metrics = copy.copy(metrics)
            metrics.insert(0, {'id': 'timestamp'})

        #
        # Convert list of metrics to format used by Sysdig Cloud
        #
        property_names = {}
        for i, metric in enumerate(metrics):
            property_name = 'v' if 'aggregations' in metric else 'k'
            property_names[metric['id']] = property_name + str(i)

            panel_configuration['metrics'].append({
                'metricId':         metric['id'],
                'aggregation':      metric['aggregations']['time'] if 'aggregations' in metric else None,
                'groupAggregation': metric['aggregations']['group'] if 'aggregations' in metric else None,
                'propertyName':     property_name + str(i)
            })
        #
        # Convert scope to format used by Sysdig Cloud
        #
        if scope != None:
            filter_expressions = scope.strip(' \t\n\r?!.').split(" and ")
            filters = []

            for filter_expression in filter_expressions:
                values = filter_expression.strip(' \t\n\r?!.').split("=")
                if len(values) != 2:
                    return [False, "invalid scope format"]
                filters.append({
                    'metric':   values[0].strip(' \t\n\r?!.'),
                    'op':       '=',
                    'value':    values[1].strip(' \t\n\r"?!.'),
                    'filters':  None
                })

            if len(filters) > 0:
                panel_configuration['filter'] = {
                    'filters': {
                        'logic':    'and',
                        'filters':  filters
                    }
                }

        #
        # Configure panel type
        #
        if panel_type == 'timeSeries':
            panel_configuration['showAs'] = 'timeSeries'
            panel_configuration['showAsType'] = 'line'

            if limit != None:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to':   limit - 1
                }

        elif panel_type == 'number':
            panel_configuration['showAs'] = 'summary'
            panel_configuration['showAsType'] = 'summary'
        elif panel_type == 'top':
            panel_configuration['showAs'] = 'top'
            panel_configuration['showAsType'] = 'bars'

            if sort_by is None:
                panel_configuration['sorting'] = [{
                    'id':   'v0',
                    'mode': 'desc'
                }]
            else:
                panel_configuration['sorting'] = [{
                    'id':   property_names[sort_by['metric']],
                    'mode': sort_by['mode']
                }]

            if limit is None:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to':   10
                }
            else:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to':   limit - 1
                }


        #
        # Configure layout
        #
        if layout != None:
            panel_configuration['gridConfiguration'] = layout

        #
        # Clone existing dashboard...
        #
        dashboard_configuration = copy.deepcopy(dashboard)
        dashboard_configuration['id'] = None

        #
        # ... and add the new panel
        #
        dashboard_configuration['items'].append(panel_configuration)

        #
        # Update dashboard
        #
        res = requests.put(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, res.json()]

    def remove_dashboard_panel(self, dashboard, panel_name):
        #
        # Clone existing dashboard...
        #
        dashboard_configuration = copy.deepcopy(dashboard)
        dashboard_configuration['id'] = None

        #
        # ... find the panel
        #
        def filter_fn(panel):
            return panel['name'] == panel_name
        panels = filter(filter_fn, dashboard_configuration['items'])

        if len(panels) > 0:
            #
            # ... and remove it
            #
            for panel in panels:
                dashboard_configuration['items'].remove(panel)

            #
            # Update dashboard
            #
            res = requests.put(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}))
            if not self.__checkResponse(res):
                return [False, self.lasterr]
            else:
                return [True, res.json()]
        else:
            return [False, 'Not found']

    def create_dashboard_from_template(self, newdashname, template, scope):
        if scope is None:
            scope = []

        if type(scope) is str:
            checks = scope.strip(' \t\n\r?!.').split(" and ")
            scope = []

            for c in checks:
                elements = c.strip(' \t\n\r?!.').split("=")
                if len(elements) != 2:
                    return [False, "invalid scope format"]
                scope.append({elements[0].strip(' \t\n\r?!.'): elements[1].strip(' \t\n\r?!.')})
        else:
            if not(type(scope) is list):
                return [False, "invalid scope format"]

        #
        # Create the unique ID for this dashboard
        #
        baseconfid = newdashname
        for sentry in scope:
            baseconfid = baseconfid + str(sentry.keys()[0])
            baseconfid = baseconfid + str(sentry.values()[0])

        #
        # Clean up the dashboard we retireved so it's ready to be pushed
        #
        template['id'] = None
        template['version'] = None
        template['name'] = newdashname
        template['isShared'] = False # make sure the dashboard is not shared

        #
        # Assign the filter and the group ID to each view to point to this service
        #
        filters = []
        gby = []
        for sentry in scope:
            filters.append({'metric' : sentry.keys()[0], 'op' : '=', 'value' : sentry.values()[0],
                            'filters' : None})
            gby.append({'metric': sentry.keys()[0]})

        filter = {
            'filters' :
            {
                'logic' : 'and',
                'filters' : filters
            }
        }

        #
        # create the grouping configurations for each chart
        #
        j = 0
        if 'items' in template:
            for chart in template['items']:
                if len(scope) != 0:
                    j = j + 1

                    confid = baseconfid + str(j)

                    gconf = {'id': confid,
                             'groups': [
                                 {
                                     'groupBy': gby
                                 }
                             ]
                            }

                    res = requests.post(self.url + '/api/groupConfigurations', headers=self.hdrs,
                                        data=json.dumps(gconf))
                    if not self.__checkResponse(res):
                        return [False, self.lasterr]

                    chart['filter'] = filter
                    chart['groupId'] = confid
                else:
                    chart['filter'] = None
                    chart['groupId'] = None

        if 'annotations' in template:
            template['annotations']['createdByEngine'] = True
        else:
            template['annotations'] = {'createdByEngine': True}

        ddboard = {'dashboard': template}

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps(ddboard))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, res.json()]

    def create_dashboard_from_view(self, newdashname, viewname, filter):
        #
        # Find our template view
        #
        gvres = self.get_view(viewname)
        if gvres[0] is False:
            return gvres

        view = gvres[1]['drilldownDashboard']

        view['timeMode'] = {'mode' : 1}
        view['time'] = {'last' : 2 * 60 * 60 * 1000000, 'sampling' : 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(newdashname, view, filter)

    def create_dashboard_from_dashboard(self, newdashname, templatename, filter):
        #
        # Get the list of dashboards from the server
        #
        res = requests.get(self.url + '/ui/dashboards', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]

        j = res.json()

        #
        # Find our template dashboard
        #
        dboard = None

        for db in j['dashboards']:
            if db['name'] == templatename:
                dboard = db
                break

        if dboard is None:
            self.lasterr = 'can\'t find dashboard ' + templatename + ' to use as a template'
            return [False, self.lasterr]

        #
        # Create the dashboard
        #
        return self.create_dashboard_from_template(newdashname, dboard, filter)

    def create_dashboard_from_file(self, newdashname, filename, scope):
        #
        # Load the Dashboard
        #
        with open(filename) as data_file:
            dboard = json.load(data_file)

        dboard['timeMode'] = {'mode' : 1}
        dboard['time'] = {'last' : 2 * 60 * 60 * 1000000, 'sampling' : 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        self.create_dashboard_from_template(newdashname, dboard, scope)

    def delete_dashboard(self, dashboard):
        if 'id' not in dashboard:
            return [False, "Invalid dashboard format"]

        res = requests.delete(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]

        return [True, None]

    def post_event(self, name, description=None, severity=None, event_filter=None, tags=None):
        edata = {
            'event': {
                'name': name
                }
            }

        if description is not None:
            edata['event']['description'] = description

        if severity is not None:
            edata['event']['severity'] = severity

        if event_filter is not None:
            edata['event']['filter'] = event_filter

        if tags is not None:
            edata['event']['tags'] = tags

        res = requests.post(self.url + '/api/events/', headers=self.hdrs, data=json.dumps(edata))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_events(self, name=None, from_ts=None, to_ts=None, tags=None):
        params = {}

        if name is not None:
            params['name'] = name

        if from_ts is not None:
            params['from'] = from_ts

        if to_ts is not None:
            params['to'] = to_ts

        if tags is not None:
            params['tags'] = tags

        res = requests.get(self.url + '/api/events/', headers=self.hdrs, params=params)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def delete_event(self, event):
        if 'id' not in event:
            return [False, "Invalid event format"]

        res = requests.delete(self.url + '/api/events/' + str(event['id']), headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, None]

    def get_data(self, metrics, start_ts, end_ts=0, sampling_s=0,
                 filter='', datasource_type='host'):
        reqbody = {
            'metrics': metrics,
            'dataSourceType': datasource_type,
        }

        if start_ts < 0:
            reqbody['last'] = -start_ts
        elif start_ts == 0:
            return [False, "start_ts cannot be 0"]
        else:
            reqbody['start'] = start_ts
            reqbody['end'] = end_ts

        if filter != '':
            reqbody['filter'] = filter

        if sampling_s != 0:
            reqbody['sampling'] = sampling_s

        res = requests.post(self.url + '/api/data/', headers=self.hdrs, data=json.dumps(reqbody))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_metrics(self):
        res = requests.get(self.url + '/api/data/metrics', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_sysdig_captures(self):
        res = requests.get(self.url + '/api/sysdig', headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def poll_sysdig_capture(self, capture):
        if 'id' not in capture:
            return [False, 'Invalid capture format']

        res = requests.get(self.url + '/api/sysdig/' + str(capture['id']), headers=self.hdrs)
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def create_sysdig_capture(self, hostname, capture_name, duration, capture_filter='', folder='/'):
        res = self.get_connected_agents()
        if not res[0]:
            return res

        capture_agent = None

        for agent in res[1]:
            if hostname == agent['hostName']:
                capture_agent = agent
                break

        if capture_agent is None:
            return [False, hostname + ' not found']

        data = {
            'agent': capture_agent,
            'name' : capture_name,
            'duration': duration,
            'folder': folder,
            'filters': capture_filter,
            'bucketName': ''
        }

        res = requests.post(self.url + '/api/sysdig', headers=self.hdrs, data=json.dumps(data))
        if not self.__checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]
