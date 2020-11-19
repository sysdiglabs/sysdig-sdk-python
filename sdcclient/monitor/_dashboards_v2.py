import copy
import json

from sdcclient._common import _SdcCommon
from sdcclient.monitor.dashboard_converters import convert_dashboard_between_versions
from sdcclient.monitor.dashboard_converters._dashboard_scope import convert_scope_string_to_expression


class DashboardsClientV2(_SdcCommon):
    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True, custom_headers=None):
        super(DashboardsClientV2, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDC"
        self._dashboards_api_version = 'v2'
        self._dashboards_api_endpoint = '/api/{}/dashboards'.format(self._dashboards_api_version)
        self._default_dashboards_api_endpoint = '/api/{}/defaultDashboards'.format(self._dashboards_api_version)

    def get_views_list(self):
        res = self.http.get(self.url + self._default_dashboards_api_endpoint, headers=self.hdrs,
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

        res = self.http.get(self.url + self._default_dashboards_api_endpoint + '/' + id, headers=self.hdrs,
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
        res = self.http.get(self.url + self._dashboards_api_endpoint, headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def update_dashboard(self, dashboard_data):
        '''**Description**
            Updates dashboard with provided in data. Please note that the dictionary will require a valid ID and version field to work as expected.

        **Success Return Value**
            A dictionary containing the updated dashboard data.

        **Example**
            `examples/dashboard_basic_crud.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_basic_crud.py>`_
        '''
        res = self.http.put(self.url + self._dashboards_api_endpoint + "/" + str(dashboard_data['id']),
                            headers=self.hdrs, verify=self.ssl_verify, data=json.dumps({'dashboard': dashboard_data}))
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

        res = self.http.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs,
                             data=json.dumps({'dashboard': configuration_clone}),
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
        res = self.http.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs,
                             data=json.dumps({'dashboard': dashboard_configuration}),
                             verify=self.ssl_verify)
        return self._request_result(res)

    # TODO COVER
    def add_dashboard_panel(self, dashboard, name, panel_type, metrics, scope=None, sort_direction='desc', limit=None,
                            layout=None):
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
        panel_configuration['overrideScope'] = ('scope' in dashboard and dashboard['scope'] != scope) or \
                                               ('scope' not in dashboard and scope is not None)

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

            if limit is not None:
                panel_configuration['custom_display_options']['valueLimit'] = {
                    'count': limit,
                    'direction': 'desc'
                }

        elif panel_type == 'number':
            panel_configuration['showAs'] = 'summary'
        elif panel_type == 'top':
            panel_configuration['showAs'] = 'top'

            if limit is not None:
                panel_configuration['custom_display_options']['valueLimit'] = {
                    'count': limit,
                    'direction': sort_direction
                }

        #
        # Configure layout
        #
        if layout is not None:
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
        res = self.http.put(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']), headers=self.hdrs,
                            data=json.dumps({'dashboard': dashboard_configuration}),
                            verify=self.ssl_verify)
        return self._request_result(res)

    # TODO COVER
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
            res = self.http.put(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']),
                                headers=self.hdrs,
                                data=json.dumps({'dashboard': dashboard_configuration}),
                                verify=self.ssl_verify)
            return self._request_result(res)
        else:
            return [False, 'Not found']

    def create_dashboard_from_template(self, dashboard_name, template, scope, shared=False, public=False):
        if scope is not None:
            if not isinstance(scope, str):
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
        scopeOk, scopeRes = convert_scope_string_to_expression(scope)
        if not scopeOk:
            return scopeOk, scopeRes
        if scopeRes:
            template['scopeExpressionList'] = list(map(
                lambda ex: {'operand': ex['operand'], 'operator': ex['operator'], 'value': ex['value'],
                            'displayName': '', 'variable': False}, scopeRes))
        else:
            template['scopeExpressionList'] = None

        # NOTE: Individual panels might override the dashboard scope, the override will NOT be reset
        if 'widgets' in template and template['widgets'] is not None:
            for chart in template['widgets']:
                if 'overrideScope' not in chart:
                    chart['overrideScope'] = False

                if not chart['overrideScope']:
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
        res = self.http.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs,
                             data=json.dumps({'dashboard': template}), verify=self.ssl_verify)

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
        ok, gvres = self.get_view(viewname)
        if not ok:
            return ok, gvres

        view = gvres['defaultDashboard']

        view['timeMode'] = {'mode': 1}
        view['time'] = {'last': 2 * 60 * 60 * 1000000, 'sampling': 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(newdashname, view, filter, shared, public)

    def get_dashboard(self, dashboard_id):
        '''**Description**
            Return a dashboard with the pased in ID. This includes the dashboards created by the user and the ones shared with them by other users.

        **Success Return Value**
            A dictionary containing the requested dashboard data.

        **Example**
            `examples/dashboard_basic_crud.py <https://github.com/draios/python-sdc-client/blob/master/examples/dashboard_basic_crud.py>`_
        '''
        res = self.http.get(self.url + self._dashboards_api_endpoint + "/" + str(dashboard_id), headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

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
        res = self.http.get(self.url + self._dashboards_api_endpoint, headers=self.hdrs, verify=self.ssl_verify)
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
            conversion_result, dashboard = convert_dashboard_between_versions(dashboard,
                                                                              loaded_object['version'],
                                                                              self._dashboards_api_version)

            if not conversion_result:
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

        res = self.http.delete(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']), headers=self.hdrs,
                               verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]

        return [True, None]
