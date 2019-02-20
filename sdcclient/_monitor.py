import json
import copy
import requests

from sdcclient._common import _SdcCommon

try:
    basestring
except NameError:
    basestring = str


class SdMonitorClient(_SdcCommon):

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True):
        super(SdMonitorClient, self).__init__(token, sdc_url, ssl_verify)
        self.product = "SDC"

    def get_alerts(self):
        '''**Description**
            Retrieve the list of alerts configured by the user.

        **Success Return Value**
            An array of alert dictionaries, with the format described at `this link <https://app.sysdigcloud.com/apidocs/#!/Alerts/get_api_alerts>`__

        **Example**
            `examples/list_alerts.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_alerts.py>`_
        '''
        res = requests.get(self.url + '/api/alerts', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_notifications(self, from_ts, to_ts, state=None, resolved=None):
        '''**Description**
            Returns the list of Sysdig Monitor alert notifications.

        **Arguments**
            - **from_ts**: filter events by start time. Timestamp format is in UTC (seconds).
            - **to_ts**: filter events by start time. Timestamp format is in UTC (seconds).
            - **state**: filter events by alert state. Supported values are ``OK`` and ``ACTIVE``.
            - **resolved**: filter events by resolution status. Supported values are ``True`` and ``False``.

        **Success Return Value**
            A dictionary containing the list of notifications.

        **Example**
            `examples/list_alert_notifications.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_alert_notifications.py>`_
        '''
        params = {}

        if from_ts is not None:
            params['from'] = from_ts * 1000000

        if to_ts is not None:
            params['to'] = to_ts * 1000000

        if state is not None:
            params['state'] = state

        if resolved is not None:
            params['resolved'] = resolved

        res = requests.get(self.url + '/api/notifications', headers=self.hdrs, params=params, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def update_notification_resolution(self, notification, resolved):
        '''**Description**
            Updates the resolution status of an alert notification.

        **Arguments**
            - **notification**: notification object as returned by :func:`~SdcClient.get_notifications`.
            - **resolved**: new resolution status. Supported values are ``True`` and ``False``.

        **Success Return Value**
            The updated notification.

        **Example**
            `examples/resolve_alert_notifications.py <https://github.com/draios/python-sdc-client/blob/master/examples/resolve_alert_notifications.py>`_
        '''
        if 'id' not in notification:
            return [False, 'Invalid notification format']

        notification['resolved'] = resolved
        data = {'notification': notification}

        res = requests.put(self.url + '/api/notifications/' + str(notification['id']), headers=self.hdrs, data=json.dumps(data), verify=self.ssl_verify)
        return self._request_result(res)

    def create_alert(self, name=None, description=None, severity=None, for_atleast_s=None, condition=None,
                     segmentby=[], segment_condition='ANY', user_filter='', notify=None, enabled=True,
                     annotations={}, alert_obj=None):
        '''**Description**
            Create a threshold-based alert.

        **Arguments**
            - **name**: the alert name. This will appear in the Sysdig Monitor UI and in notification emails.
            - **description**: the alert description. This will appear in the Sysdig Monitor UI and in notification emails.
            - **severity**: syslog-encoded alert severity. This is a number from 0 to 7 where 0 means 'emergency' and 7 is 'debug'.
            - **for_atleast_s**: the number of consecutive seconds the condition must be satisfied for the alert to fire.
            - **condition**: the alert condition, as described here https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts
            - **segmentby**: a list of Sysdig Monitor segmentation criteria that can be used to apply the alert to multiple entities. For example, segmenting a CPU alert by ['host.mac', 'proc.name'] allows to apply it to any process in any machine.
            - **segment_condition**: When *segmentby* is specified (and therefore the alert will cover multiple entities) this field is used to determine when it will fire. In particular, you have two options for *segment_condition*: **ANY** (the alert will fire when at least one of the monitored entities satisfies the condition) and **ALL** (the alert will fire when all of the monitored entities satisfy the condition).
            - **user_filter**: a boolean expression combining Sysdig Monitor segmentation criteria that makes it possible to reduce the scope of the alert. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **notify**: the type of notification you want this alert to generate. Options are *EMAIL*, *SNS*, *PAGER_DUTY*, *SYSDIG_DUMP*.
            - **enabled**: if True, the alert will be enabled when created.
            - **annotations**: an optional dictionary of custom properties that you can associate to this alert for automation or management reasons
            - **alert_obj**: an optional fully-formed Alert object of the format returned in an "alerts" list by :func:`~SdcClient.get_alerts` This is an alternative to creating the Alert using the individual parameters listed above.

        **Success Return Value**
            A dictionary describing the just created alert, with the format described at `this link <https://app.sysdigcloud.com/apidocs/#!/Alerts/post_api_alerts>`__

        **Example**
            `examples/create_alert.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_alert.py>`_
        '''
        #
        # Get the list of alerts from the server
        #
        res = requests.get(self.url + '/api/alerts', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        res.json()

        if alert_obj is None:
            if None in (name, description, severity, for_atleast_s, condition):
                return [False, 'Must specify a full Alert object or all parameters: name, description, severity, for_atleast_s, condition']
            else:
                #
                # Populate the alert information
                #
                alert_json = {
                    'alert': {
                        'type': 'MANUAL',
                        'name': name,
                        'description': description,
                        'enabled': enabled,
                        'severity': severity,
                        'timespan': for_atleast_s * 1000000,
                        'condition': condition,
                        'filter': user_filter
                    }
                }

                if segmentby != None and segmentby != []:
                    alert_json['alert']['segmentBy'] = segmentby
                    alert_json['alert']['segmentCondition'] = {'type': segment_condition}

                if annotations != None and annotations != {}:
                    alert_json['alert']['annotations'] = annotations

                if notify != None:
                    alert_json['alert']['notificationChannelIds'] = notify
        else:
            # The REST API enforces "Alert ID and version must be null", so remove them if present,
            # since these would have been there in a dump from the list_alerts.py example.
            alert_obj.pop('id', None)
            alert_obj.pop('version', None)
            alert_json = {
                'alert': alert_obj
            }

        #
        # Create the new alert
        #
        res = requests.post(self.url + '/api/alerts', headers=self.hdrs, data=json.dumps(alert_json), verify=self.ssl_verify)
        return self._request_result(res)

    def update_alert(self, alert):
        '''**Description**
            Update a modified threshold-based alert.

        **Arguments**
            - **alert**: one modified alert object of the same format as those in the list returned by :func:`~SdcClient.get_alerts`.

        **Success Return Value**
            The updated alert.

        **Example**
            `examples/update_alert.py <https://github.com/draios/python-sdc-client/blob/master/examples/update_alert.py>`_
        '''
        if 'id' not in alert:
            return [False, "Invalid alert format"]

        res = requests.put(self.url + '/api/alerts/' + str(alert['id']), headers=self.hdrs, data=json.dumps({"alert": alert}), verify=self.ssl_verify)
        return self._request_result(res)

    def delete_alert(self, alert):
        '''**Description**
            Deletes an alert.

        **Arguments**
            - **alert**: the alert dictionary as returned by :func:`~SdcClient.get_alerts`.

        **Success Return Value**
            ``None``.

        **Example**
            `examples/delete_alert.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_alert.py>`_
        '''
        if 'id' not in alert:
            return [False, 'Invalid alert format']

        res = requests.delete(self.url + '/api/alerts/' + str(alert['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, None]

    def get_explore_grouping_hierarchy(self):
        '''**Description**
            Return the user's current grouping hierarchy as visible in the Explore tab of Sysdig Monitor.

        **Success Return Value**
            A list containing the list of the user's Explore grouping criteria.

        **Example**
            `examples/print_explore_grouping.py <https://github.com/draios/python-sdc-client/blob/master/examples/print_explore_grouping.py>`_
        '''
        res = requests.get(self.url + '/api/groupConfigurations', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
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

    def set_explore_grouping_hierarchy(self, new_hierarchy):
        '''**Description**
            Changes the grouping hierarchy in the Explore panel of the current user.

        **Arguments**
            - **new_hierarchy**: a list of sysdig segmentation metrics indicating the new grouping hierarchy.
        '''
        body = {
            'id': 'explore',
            'groups': [{'groupBy': []}]
        }

        for item in new_hierarchy:
            body['groups'][0]['groupBy'].append({'metric': item})

        res = requests.put(self.url + '/api/groupConfigurations/explore', headers=self.hdrs,
                           data=json.dumps(body), verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        else:
            return [True, None]

    def get_views_list(self):
        res = requests.get(self.url + '/api/defaultDashboards', headers=self.hdrs,
                           verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]

    def get_view(self, name):
        gvres = self.get_views_list()
        if gvres[0] is False:
            return gvres

        vlist = gvres[1]['defaultDashboards']

        id = None

        for v in vlist:
            if v['name'] == name:
                id = v['id']
                break

        if not id:
            return [False, 'view ' + name + ' not found']

        res = requests.get(self.url + '/api/defaultDashboards/' + id, headers=self.hdrs,
                           verify=self.ssl_verify)
        return self._request_result(res)

    def get_dashboards(self):
        '''**Description**
            Return the list of dashboards available under the given user account. This includes the dashboards created by the user and the ones shared with her by other users.

        **Success Return Value**
            A dictionary containing the list of available sampling intervals.

        **Example**
            `examples/list_dashboards.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_dashboards.py>`_
        '''
        res = requests.get(self.url + '/ui/dashboards', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def find_dashboard_by(self, name=None):
        '''**Description**
            Finds dashboards with the specified name. You can then delete the dashboard (with :func:`~SdcClient.delete_dashboard`) or edit panels (with :func:`~SdcClient.add_dashboard_panel` and :func:`~SdcClient.remove_dashboard_panel`)

        **Arguments**
            - **name**: the name of the dashboards to find.

        **Success Return Value**
            A list of dictionaries of dashboards matching the specified name.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        '''
        res = self.get_dashboards()
        if res[0] is False:
            return res
        else:
            def filter_fn(configuration):
                return configuration['name'] == name

            def create_item(configuration):
                return {'dashboard': configuration}

            dashboards = list(map(create_item, list(filter(filter_fn, res[1]['dashboards']))))
            return [True, dashboards]

    def create_dashboard_with_configuration(self, configuration):
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps({'dashboard': configuration}),
                            verify=self.ssl_verify)
        return self._request_result(res)

    def create_dashboard(self, name):
        '''
        **Description**
            Creates an empty dashboard. You can then add panels by using ``add_dashboard_panel``.

        **Arguments**
            - **name**: the name of the dashboard that will be created.

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        '''
        dashboard_configuration = {
            'name': name,
            'schema': 1,
            'items': []
        }

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                            verify=self.ssl_verify)
        return self._request_result(res)

    def add_dashboard_panel(self, dashboard, name, panel_type, metrics, scope=None, sort_by=None, limit=None, layout=None):
        """**Description**
            Adds a panel to the dashboard. A panel can be a time series, or a top chart (i.e. bar chart), or a number panel.

        **Arguments**
            - **dashboard**: dashboard to edit
            - **name**: name of the new panel
            - **panel_type**: type of the new panel. Valid values are: ``timeSeries``, ``top``, ``number``
            - **metrics**:  a list of dictionaries, specifying the metrics to show in the panel, and optionally, if there is only one metric, a grouping key to segment that metric by. A metric is any of the entries that can be found in the *Metrics* section of the Explore page in Sysdig Monitor. Metric entries require an *aggregations* section specifying how to aggregate the metric across time and groups of containers/hosts. A grouping key is any of the entries that can be found in the *Show* or *Segment By* sections of the Explore page in Sysdig Monitor. Refer to the examples section below for ready to use code snippets. Note, certain panels allow certain combinations of metrics and grouping keys:
                - ``timeSeries``: 1 or more metrics OR 1 metric + 1 grouping key
                - ``top``: 1 or more metrics OR 1 metric + 1 grouping key
                - ``number``: 1 metric only
            - **scope**: filter to apply to the panel; must be based on metadata available in Sysdig Monitor; Example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **sort_by**: Data sorting; The parameter is optional and it's a dictionary of ``metric`` and ``mode`` (it can be ``desc`` or ``asc``)
            - **limit**: This parameter sets the limit on the number of lines/bars shown in a ``timeSeries`` or ``top`` panel. In the case of more entities being available than the limit, the top entities according to the sort will be shown. The default value is 10 for ``top`` panels (for ``timeSeries`` the default is defined by Sysdig Monitor itself). Note that increasing the limit above 10 is not officially supported and may cause performance and rendering issues
            - **layout**: Size and position of the panel. The dashboard layout is defined by a grid of 12 columns, each row height is equal to the column height. For example, say you want to show 2 panels at the top: one panel might be 6 x 3 (half the width, 3 rows height) located in row 1 and column 1 (top-left corner of the viewport), the second panel might be 6 x 3 located in row 1 and position 7. The location is specified by a dictionary of ``row`` (row position), ``col`` (column position), ``size_x`` (width), ``size_y`` (height).

        **Success Return Value**
            A dictionary showing the details of the edited dashboard.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        """
        panel_configuration = {
            'name': name,
            'showAs': None,
            'showAsType': None,
            'metrics': [],
            'gridConfiguration': {
                'col': 1,
                'row': 1,
                'size_x': 12,
                'size_y': 6
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
        # Convert list of metrics to format used by Sysdig Monitor
        #
        property_names = {}
        k_count = 0
        v_count = 0
        for i, metric in enumerate(metrics):
            property_name = 'v' if 'aggregations' in metric else 'k'

            if property_name == 'k':
                i = k_count
                k_count += 1
            else:
                i = v_count
                v_count += 1
            property_names[metric['id']] = property_name + str(i)

            panel_configuration['metrics'].append({
                'metricId': metric['id'],
                'aggregation': metric['aggregations']['time'] if 'aggregations' in metric else None,
                'groupAggregation': metric['aggregations']['group'] if 'aggregations' in metric else None,
                'propertyName': property_name + str(i)
            })
        #
        # Convert scope to format used by Sysdig Monitor
        #
        if scope != None:
            filter_expressions = scope.strip(' \t\n\r?!.').split(" and ")
            filters = []

            for filter_expression in filter_expressions:
                values = filter_expression.strip(' \t\n\r?!.').split("=")
                if len(values) != 2:
                    return [False, "invalid scope format"]
                filters.append({
                    'metric': values[0].strip(' \t\n\r?!.'),
                    'op': '=',
                    'value': values[1].strip(' \t\n\r"?!.'),
                    'filters': None
                })

            if len(filters) > 0:
                panel_configuration['filter'] = {
                    'filters': {
                        'logic': 'and',
                        'filters': filters
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
                    'to': limit - 1
                }

        elif panel_type == 'number':
            panel_configuration['showAs'] = 'summary'
            panel_configuration['showAsType'] = 'summary'
        elif panel_type == 'top':
            panel_configuration['showAs'] = 'top'
            panel_configuration['showAsType'] = 'bars'

            if sort_by is None:
                panel_configuration['sorting'] = [{
                    'id': 'v0',
                    'mode': 'desc'
                }]
            else:
                panel_configuration['sorting'] = [{
                    'id': property_names[sort_by['metric']],
                    'mode': sort_by['mode']
                }]

            if limit is None:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to': 10
                }
            else:
                panel_configuration['paging'] = {
                    'from': 0,
                    'to': limit - 1
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
        res = requests.put(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                           verify=self.ssl_verify)
        return self._request_result(res)

    def remove_dashboard_panel(self, dashboard, panel_name):
        '''**Description**
            Removes a panel from the dashboard. The panel to remove is identified by the specified ``name``.

        **Arguments**
            - **name**: name of the panel to find and remove

        **Success Return Value**
            A dictionary showing the details of the edited dashboard.

        **Example**
            `examples/dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard.py>`_
        '''
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
        panels = list(filter(filter_fn, dashboard_configuration['items']))

        if len(panels) > 0:
            #
            # ... and remove it
            #
            for panel in panels:
                dashboard_configuration['items'].remove(panel)

            #
            # Update dashboard
            #
            res = requests.put(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                               verify=self.ssl_verify)
            return self._request_result(res)
        else:
            return [False, 'Not found']

    def create_dashboard_from_template(self, dashboard_name, template, scope, shared=False, public=False, annotations={}):
        if scope is not None:
            if isinstance(scope, basestring) == False:
                return [False, 'Invalid scope format: Expected a string']

        #
        # Clean up the dashboard we retireved so it's ready to be pushed
        #
        template['id'] = None
        template['version'] = None
        template['schema'] = 1
        template['name'] = dashboard_name
        template['isShared'] = shared
        template['isPublic'] = public
        template['publicToken'] = None

        #
        # set dashboard scope to the specific parameter
        # NOTE: Individual panels might override the dashboard scope, the override will NOT be reset
        #
        template['filterExpression'] = scope

        if 'items' in template:
            for chart in template['items']:
                if 'overrideFilter' in chart and chart['overrideFilter'] == False:
                    # patch frontend bug to hide scope override warning even when it's not really overridden
                    chart['scope'] = scope

        if 'annotations' in template:
            template['annotations'].update(annotations)
        else:
            template['annotations'] = annotations

        template['annotations']['createdByEngine'] = True

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + '/ui/dashboards', headers=self.hdrs, data=json.dumps({'dashboard': template}), verify=self.ssl_verify)
        return self._request_result(res)

    def create_dashboard_from_view(self, newdashname, viewname, filter, shared=False, public=False, annotations={}):
        '''**Description**
            Create a new dasboard using one of the Sysdig Monitor views as a template. You will be able to define the scope of the new dashboard.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **viewname**: the name of the view to use as the template for the new dashboard. This corresponds to the name that the view has in the Explore page.
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria that defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **public**: if set to True, the new dashboard will be shared with public token.
            - **annotations**: an optional dictionary of custom properties that you can associate to this dashboard for automation or management reasons

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/create_dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_dashboard.py>`_
        '''
        #
        # Find our template view
        #
        gvres = self.get_view(viewname)
        if gvres[0] is False:
            return gvres

        view = gvres[1]['defaultDashboard']

        view['timeMode'] = {'mode': 1}
        view['time'] = {'last': 2 * 60 * 60 * 1000000, 'sampling': 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(newdashname, view, filter, shared, public, annotations)

    def create_dashboard_from_dashboard(self, newdashname, templatename, filter, shared=False, public=False, annotations={}):
        '''**Description**
            Create a new dasboard using one of the existing dashboards as a template. You will be able to define the scope of the new dasboard.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **viewname**: the name of the dasboard to use as the template, as it appears in the Sysdig Monitor dashboard page.
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **public**: if set to True, the new dashboard will be shared with public token.
            - **annotations**: an optional dictionary of custom properties that you can associate to this dashboard for automation or management reasons

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/create_dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_dashboard.py>`_
        '''
        #
        # Get the list of dashboards from the server
        #
        res = requests.get(self.url + '/ui/dashboards', headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
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
        return self.create_dashboard_from_template(newdashname, dboard, filter, shared, public, annotations)

    def create_dashboard_from_file(self, newdashname, filename, filter, shared=False, public=False, annotations={}):
        '''
        **Description**
            Create a new dasboard using a dashboard template saved to disk.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **filename**: name of a file containing a JSON object for a dashboard in the format of an array element returned by :func:`~SdcClient.get_dashboards`
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **public**: if set to True, the new dashboard will be shared with public token.
            - **annotations**: an optional dictionary of custom properties that you can associate to this dashboard for automation or management reasons

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/dashboard_save_load.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_save_load.py>`_
        '''
        #
        # Load the Dashboard
        #
        with open(filename) as data_file:
            dboard = json.load(data_file)

        dboard['timeMode'] = {'mode': 1}
        dboard['time'] = {'last': 2 * 60 * 60 * 1000000, 'sampling': 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(newdashname, dboard, filter, shared, public, annotations)

    def delete_dashboard(self, dashboard):
        '''**Description**
            Deletes a dashboard.

        **Arguments**
            - **dashboard**: the dashboard object as returned by :func:`~SdcClient.get_dashboards`.

        **Success Return Value**
            `None`.

        **Example**
            `examples/delete_dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/delete_dashboard.py>`_
        '''
        if 'id' not in dashboard:
            return [False, "Invalid dashboard format"]

        res = requests.delete(self.url + '/ui/dashboards/' + str(dashboard['id']), headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, None]

    def get_metrics(self):
        '''**Description**
            Return the metric list that can be used for data requests/alerts/dashboards.

        **Success Return Value**
            A dictionary containing the list of available metrics.

        **Example**
            `examples/list_metrics.py <https://github.com/draios/python-sdc-client/blob/master/examples/list_metrics.py>`_
        '''
        res = requests.get(self.url + '/api/data/metrics', headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)


# For backwards compatibility
SdcClient = SdMonitorClient
