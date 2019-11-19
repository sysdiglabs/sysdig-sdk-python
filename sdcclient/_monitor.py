import json
import copy
import requests
import re

from sdcclient._common import _SdcCommon

try:
    basestring
except NameError:
    basestring = str


class SdMonitorClient(_SdcCommon):

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True, custom_headers=None):
        super(SdMonitorClient, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDC"
        self._dashboards_api_version = 'v2'
        self._dashboards_api_endpoint = '/api/{}/dashboards'.format(self._dashboards_api_version)
        self._default_dashboards_api_endpoint = '/api/{}/defaultDashboards'.format(self._dashboards_api_version)

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
        res = requests.get(self.url + self._default_dashboards_api_endpoint, headers=self.hdrs,
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

        res = requests.get(self.url + self._default_dashboards_api_endpoint + '/' + id, headers=self.hdrs,
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
        res = requests.get(self.url + self._dashboards_api_endpoint, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def get_dashboard(self, dashboard_id):
        '''**Description**
            Return a dashboard with the pased in ID. This includes the dashboards created by the user and the ones shared with them by other users.

        **Success Return Value**
            A dictionary containing the requested dashboard data.

        **Example**
            `examples/dashboard_basic_crud.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_basic_crud.py>`_
        '''
        res = requests.get(self.url + self._dashboards_api_endpoint + "/" + str(dashboard_id), headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def update_dashboard(self, dashboard_data):
        '''**Description**
            Updates dashboard with provided in data. Please note that the dictionary will require a valid ID and version field to work as expected.

        **Success Return Value**
            A dictionary containing the updated dashboard data.

        **Example**
            `examples/dashboard_basic_crud.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_basic_crud.py>`_
        '''
        res = requests.put(self.url + self._dashboards_api_endpoint + "/" + str(dashboard_data['id']), headers=self.hdrs, verify=self.ssl_verify, data=json.dumps({'dashboard': dashboard_data}))
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
        # Remove id and version properties if already set
        configuration_clone = copy.deepcopy(configuration)
        if 'id' in configuration_clone:
            del configuration_clone['id']
        if 'version' in configuration_clone:
            del configuration_clone['version']

        res = requests.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs, data=json.dumps({'dashboard': configuration_clone}),
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
            'schema': 2,
            'widgets': [],
            'eventsOverlaySettings': {
                'filterNotificationsUserInputFilter': ''
            }
        }

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                            verify=self.ssl_verify)
        return self._request_result(res)

    def add_dashboard_panel(self, dashboard, name, panel_type, metrics, scope=None, sort_direction='desc', limit=None, layout=None):
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
            - **sort_direction**: Data sorting; The parameter is optional and it's a string identifying the sorting direction (it can be ``desc`` or ``asc``)
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
            'metrics': [],
            'gridConfiguration': {
                'col': 1,
                'row': 1,
                'size_x': 12,
                'size_y': 6
            },
            'customDisplayOptions': {}
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
                'id': metric['id'],
                'timeAggregation': metric['aggregations']['time'] if 'aggregations' in metric else None,
                'groupAggregation': metric['aggregations']['group'] if 'aggregations' in metric else None,
                'propertyName': property_name + str(i)
            })

        panel_configuration['scope'] = scope
        # if chart scope is equal to dashboard scope, set it as non override
        panel_configuration['overrideScope'] = ('scope' in dashboard and dashboard['scope'] != scope) or ('scope' not in dashboard and scope != None)

        if 'custom_display_options' not in panel_configuration:
            panel_configuration['custom_display_options'] = {
                'valueLimit': {
                    'count': 10,
                    'direction': 'desc'
                },
                'histogram': {
                    'numberOfBuckets': 10
                },
                'yAxisScale': 'linear',
                'yAxisLeftDomain': {
                    'from': 0,
                    'to': None
                },
                'yAxisRightDomain': {
                    'from': 0,
                    'to': None
                },
                'xAxis': {
                    'from': 0,
                    'to': None
                }
            }
        #
        # Configure panel type
        #
        if panel_type == 'timeSeries':
            panel_configuration['showAs'] = 'timeSeries'

            if limit != None:
                panel_configuration['custom_display_options']['valueLimit'] = {
                    'count': limit,
                    'direction': 'desc'
                }

        elif panel_type == 'number':
            panel_configuration['showAs'] = 'summary'
        elif panel_type == 'top':
            panel_configuration['showAs'] = 'top'

            if limit != None:
                panel_configuration['custom_display_options']['valueLimit'] = {
                    'count': limit,
                    'direction': sort_direction
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

        #
        # ... and add the new panel
        #
        dashboard_configuration['widgets'].append(panel_configuration)

        #
        # Update dashboard
        #
        res = requests.put(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
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

        #
        # ... find the panel
        #
        def filter_fn(panel):
            return panel['name'] == panel_name
        panels = list(filter(filter_fn, dashboard_configuration['widgets']))

        if len(panels) > 0:
            #
            # ... and remove it
            #
            for panel in panels:
                dashboard_configuration['widgets'].remove(panel)

            #
            # Update dashboard
            #
            res = requests.put(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']), headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                               verify=self.ssl_verify)
            return self._request_result(res)
        else:
            return [False, 'Not found']

    def create_dashboard_from_template(self, dashboard_name, template, scope, shared=False, public=False):
        if scope is not None:
            if isinstance(scope, basestring) == False:
                return [False, 'Invalid scope format: Expected a string']

        #
        # Clean up the dashboard we retireved so it's ready to be pushed
        #
        template['id'] = None
        template['version'] = None
        template['schema'] = 2
        template['name'] = dashboard_name
        template['shared'] = shared
        template['public'] = public
        template['publicToken'] = None

        # default dashboards don't have eventsOverlaySettings property
        # make sure to add the default set if the template doesn't include it
        if 'eventsOverlaySettings' not in template or not template['eventsOverlaySettings']:
            template['eventsOverlaySettings'] = {
                'filterNotificationsUserInputFilter': ''
            }

        # set dashboard scope to the specific parameter
        scopeExpression = self.convert_scope_string_to_expression(scope)
        if scopeExpression[0] == False:
            return scopeExpression
        if scopeExpression[1]:
            template['scopeExpressionList'] = map(lambda ex: {'operand': ex['operand'], 'operator': ex['operator'], 'value': ex['value'], 'displayName': '', 'variable': False}, scopeExpression[1])
        else:
            template['scopeExpressionList'] = None

        # NOTE: Individual panels might override the dashboard scope, the override will NOT be reset
        if 'widgets' in template and template['widgets'] is not None:
            for chart in template['widgets']:
                if 'overrideScope' not in chart:
                    chart['overrideScope'] = False

                if chart['overrideScope'] == False:
                    # patch frontend bug to hide scope override warning even when it's not really overridden
                    chart['scope'] = scope
                
                if chart['showAs'] != 'map':
                    # if chart scope is equal to dashboard scope, set it as non override
                    chart_scope = chart['scope'] if 'scope' in chart else None
                    chart['overrideScope'] = chart_scope != scope
                else:
                    # topology panels must override the scope
                    chart['overrideScope'] = True

        #
        # Create the new dashboard
        #
        res = requests.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs, data=json.dumps({'dashboard': template}), verify=self.ssl_verify)
            
        return self._request_result(res)

    def create_dashboard_from_view(self, newdashname, viewname, filter, shared=False, public=False):
        '''**Description**
            Create a new dasboard using one of the Sysdig Monitor views as a template. You will be able to define the scope of the new dashboard.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **viewname**: the name of the view to use as the template for the new dashboard. This corresponds to the name that the view has in the Explore page.
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria that defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **public**: if set to True, the new dashboard will be shared with public token.

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
        return self.create_dashboard_from_template(newdashname, view, filter, shared, public)

    def create_dashboard_from_dashboard(self, newdashname, templatename, filter, shared=False, public=False):
        '''**Description**
            Create a new dasboard using one of the existing dashboards as a template. You will be able to define the scope of the new dasboard.

        **Arguments**
            - **newdashname**: the name of the dashboard that will be created.
            - **viewname**: the name of the dasboard to use as the template, as it appears in the Sysdig Monitor dashboard page.
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **public**: if set to True, the new dashboard will be shared with public token.

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/create_dashboard.py <https://github.com/draios/python-sdc-client/blob/master/examples/create_dashboard.py>`_
        '''
        #
        # Get the list of dashboards from the server
        #
        res = requests.get(self.url + self._dashboards_api_endpoint, headers=self.hdrs, verify=self.ssl_verify)
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
        return self.create_dashboard_from_template(newdashname, dboard, filter, shared, public)

    def create_dashboard_from_file(self, dashboard_name, filename, filter, shared=False, public=False):
        '''
        **Description**
            Create a new dasboard using a dashboard template saved to disk. See :func:`~SdcClient.save_dashboard_to_file` to use the file to create a dashboard (usefl to create and restore backups).

            The file can contain the following JSON formats:
            1. dashboard object in the format of an array element returned by :func:`~SdcClient.get_dashboards`
            2. JSON object with the following properties:
                * version: dashboards API version (e.g. 'v2')
                * dashboard: dashboard object in the format of an array element returned by :func:`~SdcClient.get_dashboards`

        **Arguments**
            - **dashboard_name**: the name of the dashboard that will be created.
            - **filename**: name of a file containing a JSON object
            - **filter**: a boolean expression combining Sysdig Monitor segmentation criteria defines what the new dasboard will be applied to. For example: *kubernetes.namespace.name='production' and container.image='nginx'*.
            - **shared**: if set to True, the new dashboard will be a shared one.
            - **public**: if set to True, the new dashboard will be shared with public token.

        **Success Return Value**
            A dictionary showing the details of the new dashboard.

        **Example**
            `examples/dashboard_save_load.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_save_load.py>`_
        '''
        #
        # Load the Dashboard
        #
        with open(filename) as data_file:
            loaded_object = json.load(data_file)

        #
        # Handle old files
        #
        if 'dashboard' not in loaded_object:
            loaded_object = {
                'version': 'v1',
                'dashboard': loaded_object
            }

        dashboard = loaded_object['dashboard']

        if loaded_object['version'] != self._dashboards_api_version:
            #
            # Convert the dashboard (if possible)
            #
            conversion_result, dashboard = self._convert_dashboard_to_current_version(dashboard, loaded_object['version'])

            if conversion_result == False:
                return conversion_result, dashboard

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(dashboard_name, dashboard, filter, shared, public)

    def save_dashboard_to_file(self, dashboard, filename):
        '''
        **Description**
            Save a dashboard to disk. See :func:`~SdcClient.create_dashboard_from_file` to use the file to create a dashboard (usefl to create and restore backups).

            The file will contain a JSON object with the following properties:
            * version: dashboards API version (e.g. 'v2')
            * dashboard: dashboard object in the format of an array element returned by :func:`~SdcClient.get_dashboards`

        **Arguments**
            - **dashboard**: dashboard object in the format of an array element returned by :func:`~SdcClient.get_dashboards`
            - **filename**: name of a file that will contain a JSON object

        **Example**
            `examples/dashboard_save_load.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_save_load.py>`_
        '''
        with open(filename, 'w') as outf:
            json.dump({
                'version': self._dashboards_api_version,
                'dashboard': dashboard
            }, outf)

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

        res = requests.delete(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']), headers=self.hdrs, verify=self.ssl_verify)
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

    @staticmethod
    def convert_scope_string_to_expression(scope):
        '''**Description**
            Internal function to convert a filter string to a filter object to be used with dashboards.
        '''
        #
        # NOTE: The supported grammar is not perfectly aligned with the grammar supported by the Sysdig backend.
        # Proper grammar implementation will happen soon.
        # For practical purposes, the parsing will have equivalent results.
        #

        if scope is None or not scope:
            return [True, []]

        expressions = []
        string_expressions = scope.strip(' \t\n\r').split(' and ')
        expression_re = re.compile('^(?P<not>not )?(?P<operand>[^ ]+) (?P<operator>=|!=|in|contains|starts with) (?P<value>(:?"[^"]+"|\'[^\']+\'|\(.+\)|.+))$')

        for string_expression in string_expressions:
            matches = expression_re.match(string_expression)

            if matches is None:
                return [False, 'invalid scope format']

            is_not_operator = matches.group('not') is not None

            if matches.group('operator') == 'in':
                list_value = matches.group('value').strip(' ()')
                value_matches = re.findall('(:?\'[^\',]+\')|(:?"[^",]+")|(:?[,]+)', list_value)

                if len(value_matches) == 0:
                    return [False, 'invalid scope value list format']

                value_matches = map(lambda v: v[0] if v[0] else v[1], value_matches)
                values = map(lambda v: v.strip(' "\''), value_matches)
            else:
                values = [matches.group('value').strip('"\'')]

            operator_parse_dict = {
                'in': 'in' if not is_not_operator else 'notIn',
                '=': 'equals' if not is_not_operator else 'notEquals',
                '!=': 'notEquals' if not is_not_operator else 'equals',
                'contains': 'contains' if not is_not_operator else 'notContains',
                'starts with': 'startsWith'
            }

            operator = operator_parse_dict.get(matches.group('operator'), None)
            if operator is None:
                return [False, 'invalid scope operator']

            expressions.append({
                'operand': matches.group('operand'),
                'operator': operator,
                'value': values
            })

        return [True, expressions]

    def _get_dashboard_converters(self):
        return {
            'v2': {
                'v1': self._convert_dashboard_v1_to_v2
            }
        }

    def _convert_dashboard_to_current_version(self, dashboard, version):
        converters_to = self._get_dashboard_converters().get(self._dashboards_api_version, None)
        if converters_to == None:
            return False, 'unexpected error: no dashboard converters from version {} are supported'.format(self._dashboards_api_version)
        
        converter = converters_to.get(version, None)

        if converter == None:
            return False, 'dashboard version {} cannot be converted to {}'.format(version, self._dashboards_api_version)

        try:
            return converter(dashboard)
        except Exception as err:
            return False, str(err)

    def _convert_dashboard_v1_to_v2(self, dashboard):
        #
        # Migrations
        #
        # Each converter function will take:
        #   1. name of the v1 dashboard property
        #   2. v1 dashboard configuration
        #   3. v2 dashboard configuration
        #
        # Each converter will apply changes to v2 dashboard configuration according to v1
        #
        def when_set(converter):
            def fn(prop_name, old_obj, new_obj):
                if prop_name in old_obj and old_obj[prop_name] is not None:
                    converter(prop_name, old_obj, new_obj)
            
            return fn

        def with_default(converter, default=None):
            def fn(prop_name, old_obj, new_obj):
                if prop_name not in old_obj:
                    old_obj[prop_name] = default

                converter(prop_name, old_obj, new_obj)
            
            return fn
            
        def keep_as_is(prop_name, old_obj, new_obj):
            new_obj[prop_name] = old_obj[prop_name]
        
        def drop_it(prop_name = None, old_obj = None, new_obj = None):
            pass
        
        def ignore(prop_name = None, old_obj = None, new_obj = None):
            pass

        def rename_to(new_prop_name):
            def rename(prop_name, old_obj, new_obj):
                new_obj[new_prop_name] = old_obj[prop_name]

            return rename

        def convert_schema(prop_name, old_dashboard, new_dashboard):
            new_dashboard[prop_name] = 2

        def convert_scope(prop_name, old_dashboard, new_dashboard):
            # # TODO!

            scope = old_dashboard[prop_name]
            scope_conversion = self.convert_scope_string_to_expression(scope)

            if scope_conversion[0]:
                if scope_conversion[1]:
                    new_dashboard['scopeExpressionList'] = scope_conversion[1]
                else:
                    # the property can be either `null` or a non-empty array
                    new_dashboard['scopeExpressionList'] = None
            else:
                raise SyntaxError('scope not supported by the current grammar')

        def convert_events_filter(prop_name, old_dashboard, new_dashboard):
            rename_to('eventsOverlaySettings')(prop_name, old_dashboard, new_dashboard)

            if 'showNotificationsDoNotFilterSameMetrics' in new_dashboard['eventsOverlaySettings']:
                del new_dashboard['eventsOverlaySettings']['showNotificationsDoNotFilterSameMetrics']
            if 'showNotificationsDoNotFilterSameScope' in new_dashboard['eventsOverlaySettings']:
                del new_dashboard['eventsOverlaySettings']['showNotificationsDoNotFilterSameScope']

        def convert_items(prop_name, old_dashboard, new_dashboard):    
            def convert_color_coding(prop_name, old_widget, new_widget):
                best_value = None
                worst_value= None
                for item in old_widget[prop_name]['thresholds']:
                    if item['color'] == 'best':
                        best_value = item['max'] if not item['max'] else item['min']
                    elif item['color'] == 'worst':
                        worst_value = item['min'] if not item['min'] else item['max']
                
                if best_value is not None and worst_value is not None:
                    new_widget[prop_name] = {
                        'best': best_value,
                        'worst': worst_value
                    }

            def convert_display_options(prop_name, old_widget, new_widget):
                keep_as_is(prop_name, old_widget, new_widget)

                if 'yAxisScaleFactor' in new_widget[prop_name]:
                    del new_widget[prop_name]['yAxisScaleFactor']

            def convert_group(prop_name, old_widget, new_widget):
                group_by_metrics = old_widget[prop_name]['configuration']['groups'][0]['groupBy']
                
                migrated = []
                for metric in group_by_metrics:
                    migrated.append({ 'id': metric['metric'] })
                
                new_widget['groupingLabelIds'] = migrated

            def convert_override_filter(prop_name, old_widget, new_widget):
                if old_widget['showAs'] == 'map':
                    # override scope always true if scope is set
                    new_widget['overrideScope'] = True
                else:
                    new_widget['overrideScope'] = old_widget[prop_name]


            def convert_name(prop_name, old_widget, new_widget):
                #
                # enforce unique name (on old dashboard, before migration)
                #
                unique_id = 1
                name = old_widget[prop_name]

                for widget in old_dashboard['items']:
                    if widget == old_widget:
                        break
                    
                    if old_widget[prop_name] == widget[prop_name]:
                        old_widget[prop_name] = '{} ({})'.format(name, unique_id)
                        unique_id += 1

                keep_as_is(prop_name, old_widget, new_widget)

            def convert_metrics(prop_name, old_widget, new_widget):
                def convert_property_name(prop_name, old_metric, new_metric):
                    keep_as_is(prop_name, old_metric, new_metric)
                    
                    if old_metric['metricId'] == 'timestamp':
                        return 'k0'

                metric_migrations = {
                    'metricId': rename_to('id'),
                    'aggregation': rename_to('timeAggregation'),
                    'groupAggregation': rename_to('groupAggregation'),
                    'propertyName': convert_property_name
                }

                migrated_metrics = []
                for old_metric in old_widget[prop_name]:
                    migrated_metric = {}

                    for key in metric_migrations.keys():
                        if key in old_metric:
                            metric_migrations[key](key, old_metric, migrated_metric)

                    migrated_metrics.append(migrated_metric)

                # Property name convention:
                # timestamp: k0 (if present)
                # other keys: k* (from 0 or 1, depending on timestamp)
                # values: v* (from 0)
                sorted_metrics = []
                timestamp_key = filter(lambda m: m['id'] == 'timestamp' and not ('timeAggregation' in m and m['timeAggregation'] is not None), migrated_metrics)
                no_timestamp_keys = filter(lambda m: m['id'] != 'timestamp' and not ('timeAggregation' in m and m['timeAggregation'] is not None), migrated_metrics)
                values = filter(lambda m: 'timeAggregation' in m and m['timeAggregation'] is not None, migrated_metrics)
                if timestamp_key:
                    timestamp_key[0]['propertyName'] = 'k0'
                    sorted_metrics.append(timestamp_key[0])
                k_offset = 1 if timestamp_key else 0
                for i in range(0, len(no_timestamp_keys)):
                    no_timestamp_keys[i]['propertyName'] = 'k{}'.format(i + k_offset)
                    sorted_metrics.append(no_timestamp_keys[i])
                for i in range(0, len(values)):
                    values[i]['propertyName'] = 'v{}'.format(i)
                    sorted_metrics.append(values[i])
                    
                new_widget['metrics'] = sorted_metrics

            widget_migrations = {
                'colorCoding': when_set(convert_color_coding),
                'compareToConfig': when_set(keep_as_is),
                'customDisplayOptions': with_default(convert_display_options, {}),
                'gridConfiguration': keep_as_is,
                'group': when_set(convert_group),
                'hasTransparentBackground': when_set(rename_to('transparentBackground')),
                'limitToScope': when_set(keep_as_is),
                'isPanelTitleVisible': when_set(rename_to('panelTitleVisible')),
                'markdownSource': when_set(keep_as_is),
                'metrics': with_default(convert_metrics, []),
                'name': with_default(convert_name, 'Panel'),
                'overrideFilter': convert_override_filter,
                'paging': drop_it,
                'scope': with_default(keep_as_is, None),
                'showAs': keep_as_is,
                'showAsType': drop_it,
                'sorting': drop_it,
                'textpanelTooltip': when_set(keep_as_is),
            }

            migrated_widgets = []
            for old_widget in old_dashboard[prop_name]:
                migrated_widget = {}

                for key in widget_migrations.keys():
                    widget_migrations[key](key, old_widget, migrated_widget)

                migrated_widgets.append(migrated_widget)
       
            new_dashboard['widgets'] = migrated_widgets
            
            return migrated
        
        migrations = {
            'autoCreated': keep_as_is,
            'createdOn': keep_as_is,
            'eventsFilter': with_default(convert_events_filter, {
                'filterNotificationsUserInputFilter': ''
            }),
            'filterExpression': convert_scope,
            'scopeExpressionList': ignore, # scope will be generated from 'filterExpression'
            'id': keep_as_is,
            'isPublic': rename_to('public'),
            'isShared': rename_to('shared'),
            'items': convert_items,
            'layout': drop_it,
            'modifiedOn': keep_as_is,
            'name': keep_as_is,
            'publicToken': drop_it,
            'schema': convert_schema,
            'teamId': keep_as_is,
            'username': keep_as_is,
            'version': keep_as_is,
        }

        #
        # Apply migrations
        #
        migrated = {}
        for key in migrations.keys():
            migrations[key](key, copy.deepcopy(dashboard), migrated)

        return True, migrated


# For backwards compatibility
SdcClient = SdMonitorClient
