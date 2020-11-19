import copy
import json

from sdcclient._monitor import SdMonitorClient

try:
    basestring
except NameError:
    basestring = str


class SdMonitorClientV1(SdMonitorClient):
    '''**Description**
        Handles dashboards version 1 (ie. up to February 2019). For later Sysdig Monitor versions, please use :class:`~SdMonitorClient` instead.
    '''

    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True):
        super(SdMonitorClientV1, self).__init__(token, sdc_url, ssl_verify)
        self._dashboards_api_version = 'v1'
        self._dashboards_api_endpoint = '/ui/dashboards'
        self._default_dashboards_api_endpoint = '/api/defaultDashboards'

    def create_dashboard_from_template(self, dashboard_name, template, scope, shared=False, public=False,
                                       annotations={}):
        if scope is not None:
            if not isinstance(scope, basestring):
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

        # set dashboard scope to the specific parameter
        ok, scope_expression = self.convert_scope_string_to_expression(scope)
        if not ok:
            return ok, scope_expression
        template['filterExpression'] = scope
        template['scopeExpressionList'] = map(
            lambda ex: {'operand': ex['operand'], 'operator': ex['operator'], 'value': ex['value'], 'displayName': '',
                        'isVariable': False}, scope_expression)

        if 'widgets' in template and template['widgets'] is not None:
            # Default dashboards (aka Explore views) specify panels with the property `widgets`,
            # while custom dashboards use `items`
            template['items'] = list(template['widgets'])
            del template['widgets']

        # NOTE: Individual panels might override the dashboard scope, the override will NOT be reset
        if 'items' in template and template['items'] is not None:
            for chart in template['items']:
                if 'overrideFilter' not in chart:
                    chart['overrideFilter'] = False

                if not chart['overrideFilter']:
                    # patch frontend bug to hide scope override warning even when it's not really overridden
                    chart['scope'] = scope

                # if chart scope is equal to dashboard scope, set it as non override
                chart_scope = chart['scope'] if 'scope' in chart else None
                chart['overrideFilter'] = chart_scope != scope

        if 'annotations' in template:
            template['annotations'].update(annotations)
        else:
            template['annotations'] = annotations

        template['annotations']['createdByEngine'] = True

        #
        # Create the new dashboard
        #
        res = self.http.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs,
                             data=json.dumps({'dashboard': template}), verify=self.ssl_verify)
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
            'items': []
        }

        #
        # Create the new dashboard
        #
        res = self.http.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs,
                             data=json.dumps({'dashboard': dashboard_configuration}),
                             verify=self.ssl_verify)
        return self._request_result(res)

    def add_dashboard_panel(self, dashboard, name, panel_type, metrics, scope=None, sort_by=None, limit=None,
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

        panel_configuration['scope'] = scope
        # if chart scope is equal to dashboard scope, set it as non override
        panel_configuration['overrideFilter'] = ('scope' in dashboard and dashboard['scope'] != scope) or \
                                                ('scope' not in dashboard and scope is not None)

        #
        # Configure panel type
        #
        if panel_type == 'timeSeries':
            panel_configuration['showAs'] = 'timeSeries'
            panel_configuration['showAsType'] = 'line'

            if limit is not None:
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
        if layout is not None:
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
        res = self.http.put(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']), headers=self.hdrs,
                            data=json.dumps({'dashboard': dashboard_configuration}),
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
            res = self.http.put(self.url + self._dashboards_api_endpoint + '/' + str(dashboard['id']),
                                headers=self.hdrs, data=json.dumps({'dashboard': dashboard_configuration}),
                                verify=self.ssl_verify)
            return self._request_result(res)
        else:
            return [False, 'Not found']

    def _get_dashboard_converters(self):
        '''**Description**
            Internal function to return dashboard converters from one version to another one.
        '''
        # There's not really a previous version...
        return {}
