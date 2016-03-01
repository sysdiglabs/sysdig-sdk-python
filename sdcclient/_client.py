import sys
import time
import requests
import json
import re

class SdcClient:
    userinfo = None
    n_connected_agents = None

    def __init__(self, token, sdc_url = 'https://app.sysdigcloud.com'):
        self.token = token
        self.hdrs = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        self.url = sdc_url
   
    def __checkResponse(self, r):
        if r.status_code >= 300:
            self.errorcode = r.status_code

            try:
               j = r.json()
            except:
                self.lasterr = 'status code ' + str(self.errorcode)
                return False

            if 'errors' in j:
                if 'message' in j['errors'][0]:
                    self.lasterr = j['errors'][0]['message']
                else:
                    self.lasterr = j['errors'][0]['reason']
            elif 'message' in j:
                    self.lasterr = j['message']
            else:
                self.lasterr = 'status code ' + str(self.errorcode)
            return False
        return True

    def get_user_info(self):
        if self.userinfo == None:
            r = requests.get(self.url + '/api/user/me', headers=self.hdrs)
            if not self.__checkResponse(r):
                return [False, self.lasterr]
            self.userinfo = r.json()
        return [True, self.userinfo]

    def get_n_connected_agents(self):
        r = requests.get(self.url + '/api/agents/connected', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        data = r.json()
        return [True, data['total']]

    def get_alerts(self):
        r = requests.get(self.url + '/api/alerts', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def create_alert(self, name, description, severity, for_atelast_us, condition, for_each = [], filter = [], annotations={}):
        #
        # Get the list of alerts from the server
        #
        r = requests.get(self.url + '/api/alerts', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        j = r.json()

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
                'enabled' : True,
                'severity' : severity,
                'notify' : [ 'EMAIL' ],
                'timespan' : for_atelast_us,
                'condition' : condition,
                'filter': filter
            }
        }

        if for_each != None and for_each != []: 
            alert_json['alert']['segmentBy'] = for_each
            alert_json['alert']['segmentCondition'] = { 'type' : 'ANY' }

        if annotations != None and annotations != {}:
            alert_json['alert']['annotations'] = annotations

        #
        # Create the new alert
        #
        r = requests.post(self.url + '/api/alerts', headers=self.hdrs, data = json.dumps(alert_json))
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def get_notification_settings(self):
        r = requests.get(self.url + '/api/settings/notifications', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def set_notification_settings(self, settings):
        r = requests.put(self.url + '/api/settings/notifications', headers=self.hdrs, data = json.dumps(settings))
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def add_email_notification_recipient(self, email):
        #
        # Retirieve the user's notification settings
        #
        r = requests.get(self.url + '/api/settings/notifications', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        j = r.json()

        #
        # Enable email notifications
        #
        j['userNotification']['email']['enabled'] = True

        #
        # Add the given recipient
        #
        if not email in j['userNotification']['email']['recipients']:
            j['userNotification']['email']['recipients'].append(email)
        else:
            return [False, 'notification target ' + email + ' already present']

        return self.set_notification_settings(j)

    def get_explore_grouping_hierarchy(self):
        r = requests.get(self.url + '/api/groupConfigurations', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]

        data = r.json()

        if not 'groupConfigurations' in data:
            return [False, 'corrputed groupConfigurations API response']

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
        r = requests.get(self.url + '/api/history/timelines/', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def get_topology_map(self, grouping_hierarchy, time_window_s, sampling_time_s):
        #
        # Craft the time interval section
        #
        tlines = self.get_data_retention_info()

        for tline in tlines[1]['agents']:
            if tline['sampling'] == sampling_time_s * 1000000:
                timeinfo = tline

        if timeinfo == None:
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
        r = requests.post(self.url + '/api/data?format=map', headers=self.hdrs, data = json.dumps(req_json))
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def get_views_list(self):
        r = requests.get(self.url + '/data/drilldownDashboardDescriptors.json', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def get_view(self, name):
        gvres = self.get_views_list()
        if gvres[0] == False:
            return gvres

        vlist = gvres[1]['drilldownDashboardDescriptors']
        
        id = None

        for v in vlist:
            if v['name'] == name:
                id = v['id']
                break

        if not id:
            return [False, 'view ' + name + ' not found']

        r = requests.get(self.url + '/data/drilldownDashboards/' + id + '.json', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def get_dashboards(self):
        r = requests.get(self.url + '/ui/dashboards', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]

    def create_dashboard_from_template(self, newdashname, template, scope):
        if scope == None:
            scope = []

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
            filters.append({'metric' : sentry.keys()[0], 'op' : '=', 'value' : sentry.values()[0]   , 'filters' : None})
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
        for chart in template['items']:
            if len(scope) != 0:
                j = j + 1

                confid = baseconfid + str(j)

                gconf = { 'id': confid,
                    'groups': [
                        {
                            'groupBy': gby
                        }
                    ]
                }

                r = requests.post(self.url + '/api/groupConfigurations', headers=self.hdrs, data = json.dumps(gconf))
                if not self.__checkResponse(r):
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
        r = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data = json.dumps(ddboard))
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        else:
            return [True, r.json()]

    def create_dashboard_from_view(self, newdashname, viewname, scope, time_window_s):
        #
        # Find our template view
        #
        gvres = self.get_view(viewname)
        if gvres[0] == False:
            return gvres

        view = gvres[1]['drilldownDashboard']

        view['timeMode'] = {'mode' : 1}
        view['time'] = {'last' : time_window_s * 1000000, 'sampling' : time_window_s * 1000000}

        #
        # Create the new dashboard
        #
        self.create_dashboard_from_template(newdashname, view, scope)

    def create_dashboard_from_dasboard(self, newdashname, templatename, scope):
        #
        # Get the list of dashboards from the server
        #
        r = requests.get(self.url + '/ui/dashboards', headers=self.hdrs)
        if not self.__checkResponse(r):
            return [False, self.lasterr]

        j = r.json()

        #
        # Find our template dashboard
        #
        dboard = None

        for db in j['dashboards']:
            if db['name'] == templatename:
                dboard = db
                break

        if dboard == None:
            print 'can\'t find dashboard ' + templatename + ' to use as a template'
            sys.exit(0)

        '''
        #
        # If this dashboard already exists, don't create it another time
        #
        for db in j['dashboards']:
            if db['name'] == newdashname:
                for view in db['items']:
                    if view['groupId'][0:len(baseconfid)] == baseconfid:
                        print 'dashboard ' + newdashname + ' already exists - ' + baseconfid
                        return
        '''

        #
        # Create the dashboard
        #
        self.create_dashboard_from_template(newdashname, dboard, scope)

    def create_dashboard_from_file(self, newdashname, filename, scope, time_window_s):
        #
        # Load the Dashboard
        #
        with open(filename) as data_file:    
            dboard = json.load(data_file)

        dboard['timeMode'] = {'mode' : 1}
        dboard['time'] = {'last' : time_window_s * 1000000, 'sampling' : time_window_s * 1000000}

        #
        # Create the new dashboard
        #
        self.create_dashboard_from_template(newdashname, dboard, scope)

    '''
        Annotations format:

          "annotations": {
          "key1": "value1",
          "key2": "value2",
          "key3": "value3"}
    '''
    def post_event(self, name, description='', severity=6, host='', tags={}):
        edata = {
          'event': {
            'name': name,
            'severity': severity
          }
        }

        if description != '':
            edata['event']['description'] = description

        if host != '':
            edata['event']['host'] = host

        if tags != {}:
            edata['event']['tags'] = tags

        print edata

        r = requests.post(self.url + '/api/events/', headers=self.hdrs, data = json.dumps(edata))
        if not self.__checkResponse(r):
            return [False, self.lasterr]
        return [True, r.json()]
