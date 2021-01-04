import copy
import json

from sdcclient._common import _SdcCommon
from sdcclient.monitor.dashboard_converters import convert_dashboard_between_versions, \
    convert_scope_string_to_expression

PANEL_VISUALIZATION_TIMECHART = "advancedTimechart"
PANEL_VISUALIZATION_NUMBER = "advancedNumber"


class DashboardsClientV3(_SdcCommon):
    def __init__(self, token="", sdc_url='https://app.sysdigcloud.com', ssl_verify=True, custom_headers=None):
        super(DashboardsClientV3, self).__init__(token, sdc_url, ssl_verify, custom_headers)
        self.product = "SDC"
        self._dashboards_api_version = 'v3'
        self._dashboards_api_endpoint = '/api/{}/dashboards'.format(self._dashboards_api_version)
        self._default_dashboards_api_endpoint = '/api/{}/dashboards/templates'.format(self._dashboards_api_version)

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

        vlist = gvres[1]['dashboardTemplates']

        id = None

        for v in vlist:
            if v['name'] == name:
                id = v['dashboardId']
                break

        if not id:
            return [False, 'view ' + name + ' not found']

        res = self.http.get(self.url + self._default_dashboards_api_endpoint + '/' + id, headers=self.hdrs,
                            verify=self.ssl_verify)
        return self._request_result(res)

    def get_dashboards(self, light=True):
        """
        Return the list of dashboards available under the given user account.
        This includes the dashboards created by the user and the ones shared with her by other users.
        Since every user has multiple tokens -- one per team they are assigned to -- and dashboards are scoped per
        team, in order to download all the dashboards from a user account, all the tokens must be specified.

        Args:
            light (bool): If it's true, only a small portion of information will be retrieved, otherwise all
                          the information from the dashboards will be retrieved.
                          If the retrieved dashboards are going to be restored in the future, then this
                          parameter must be false.

        Returns:
            The list of the dashboards visible for the given token.

        See Also:
            :py:meth:`~.DashboardsClientV3.create_dashboard_with_configuration`

        Examples:
            >>> ok, res = client.get_dashboards(light=False)
            >>> for dashboard in res["dashboards"]:
            >>>     print(dashboard["name"])
        """
        params = {
            "light": "true" if light else "false"
        }
        res = self.http.get(self.url + self._dashboards_api_endpoint, params=params,
                            headers=self.hdrs,
                            verify=self.ssl_verify)
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
            'schema': 3,
            'widgets': [],
            'eventsOverlaySettings': {
                'filterNotificationsUserInputFilter': ''
            },
            'layout': [],
            'panels': [],
        }

        #
        # Create the new dashboard
        #
        res = self.http.post(self.url + self._dashboards_api_endpoint, headers=self.hdrs,
                             data=json.dumps({'dashboard': dashboard_configuration}),
                             verify=self.ssl_verify)
        return self._request_result(res)

    # TODO COVER
    def add_dashboard_panel(self, dashboard, panel_name, visualization, query):
        dboard = copy.deepcopy(dashboard)
        new_panel_id = dboard["panels"][-1]["id"] + 1
        new_panel = {
            "id": new_panel_id,
            "type": visualization,
            "name": panel_name,
            "description": "",
            "advancedQueries": [
                {
                    "enabled": True,
                    "displayInfo": {
                        "displayName": "",
                        "timeSeriesDisplayNameTemplate": "",
                        "type": "lines"
                    },
                    "format": {
                        "unit": "%",
                        "inputFormat": "0-100",
                        "displayFormat": "auto",
                        "decimals": None,
                        "yAxis": "auto"
                    },
                    "query": query
                }
            ]
        }
        new_layout = {
            "panelId": new_panel_id,
            "x": 0,
            # Hackish way to position a panel, the API doesn't provide auto-position
            "y": len(dboard["panels"]) * 12 + 12,
            "w": 12,
            "h": 6,
        }

        if visualization == PANEL_VISUALIZATION_TIMECHART:
            new_panel["axesConfiguration"] = {
                "bottom": {
                    "enabled": True
                },
                "left": {
                    "enabled": True,
                    "displayName": None,
                    "unit": "auto",
                    "displayFormat": "auto",
                    "decimals": None,
                    "minValue": 0,
                    "maxValue": None,
                    "minInputFormat": "0-100",
                    "maxInputFormat": "0-100",
                    "scale": "linear"
                },
                "right": {
                    "enabled": True,
                    "displayName": None,
                    "unit": "auto",
                    "displayFormat": "auto",
                    "decimals": None,
                    "minValue": 0,
                    "maxValue": None,
                    "minInputFormat": "1",
                    "maxInputFormat": "1",
                    "scale": "linear"
                }
            }
            new_panel["legendConfiguration"] = {
                "enabled": True,
                "position": "right",
                "layout": "table",
                "showCurrent": True
            }
        if visualization == PANEL_VISUALIZATION_NUMBER:
            new_panel["numberThresholds"] = {
                "values": [],
                "base": {
                    "severity": "none",
                    "displayText": "",
                }
            }

        dboard["panels"].append(new_panel)
        dboard["layout"].append(new_layout)

        return self.update_dashboard(dboard)

    # TODO COVER
    def remove_dashboard_panel(self, dashboard, panel_id):
        dboard = copy.deepcopy(dashboard)
        dboard["panels"] = [panel for panel in dboard["panels"] if panel["id"] != panel_id]
        dboard["layout"] = [layout for layout in dboard["layout"] if layout["panelId"] != panel_id]

        return self.update_dashboard(dboard)

    def create_dashboard_from_template(self, dashboard_name, template, scope=None, shared=False, public=False):
        if scope is not None:
            if not isinstance(scope, list) and not isinstance(scope, str):
                return [False, 'Invalid scope format: Expected a list, a string or None']
        else:
            scope = []

        #
        # Clean up the dashboard we retireved so it's ready to be pushed
        #
        template['id'] = None
        template['version'] = None
        template['schema'] = 3
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
        template['scopeExpressionList'] = []
        if isinstance(scope, list):
            for s in scope:
                ok, converted_scope = convert_scope_string_to_expression(s)
                if not ok:
                    return ok, converted_scope
                template['scopeExpressionList'].append(converted_scope[0])
        elif isinstance(scope, str):
            ok, converted_scope = convert_scope_string_to_expression(scope)
            if not ok:
                return ok, converted_scope
            template['scopeExpressionList'] = converted_scope

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

    def create_dashboard_from_file(self, dashboard_name, filename, filter=None, shared=False, public=False):
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
                'version': f'v{loaded_object["schema"]}',
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

    def create_dashboard_from_dashboard(self, newdashname, templatename, filter=None, shared=False, public=False):
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
        dashboard = self.http.get(self.url + self._dashboards_api_endpoint, params={"light": "true"}, headers=self.hdrs,
                                  verify=self.ssl_verify)
        if not self._checkResponse(dashboard):
            return [False, self.lasterr]

        j = dashboard.json()

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

        ok, dboard = self.get_dashboard(dboard["id"])
        if not ok:
            return ok, dboard
        #
        # Create the dashboard
        #
        return self.create_dashboard_from_template(newdashname, dboard["dashboard"], filter, shared, public)

    def favorite_dashboard(self, dashboard_id, favorite):
        data = {"dashboard": {"favorite": favorite}}
        res = self.http.patch(self.url + self._dashboards_api_endpoint + "/" + str(dashboard_id), json=data,
                              headers=self.hdrs, verify=self.ssl_verify)
        return self._request_result(res)

    def share_dashboard_with_all_teams(self, dashboard, mode="r"):
        role = "ROLE_RESOURCE_READ" if mode == "r" else "ROLE_RESOURCE_EDIT"
        dboard = copy.deepcopy(dashboard)
        dboard["sharingSettings"] = [
            {
                "member": {
                    "type": "USER_TEAMS",
                },
                "role": role,
            }
        ]
        dboard["shared"] = True

        return self.update_dashboard(dboard)

    def unshare_dashboard(self, dashboard):
        dboard = copy.deepcopy(dashboard)
        dboard["sharingSettings"] = []
        dboard["shared"] = False

        return self.update_dashboard(dboard)

    def share_dashboard_with_team(self, dashboard, team_id, mode="r"):
        role = "ROLE_RESOURCE_READ" if mode == "r" else "ROLE_RESOURCE_EDIT"
        dboard = copy.deepcopy(dashboard)

        if dboard["sharingSettings"] is None:
            dboard["sharingSettings"] = []

        dboard["sharingSettings"].append({
            "member": {
                "type": "TEAM",
                "id": team_id,
            },
            "role": role,
        })
        dboard["shared"] = True

        return self.update_dashboard(dboard)

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

        view = gvres[1]['dashboard']

        view['timeMode'] = {'mode': 1}
        view['time'] = {'last': 2 * 60 * 60 * 1000000, 'sampling': 2 * 60 * 60 * 1000000}

        #
        # Create the new dashboard
        #
        return self.create_dashboard_from_template(newdashname, view, filter, shared, public)

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
