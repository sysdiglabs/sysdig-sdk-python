import copy

from sdcclient.monitor.dashboard_converters._dashboard_scope import convert_scope_string_to_expression


def _convert_dashboard_v1_to_v2(dashboard):
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

    def drop_it(prop_name=None, old_obj=None, new_obj=None):
        pass

    def ignore(prop_name=None, old_obj=None, new_obj=None):
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
        scope_conversion = convert_scope_string_to_expression(scope)

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
            worst_value = None
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
                migrated.append({'id': metric['metric']})

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
            timestamp_key = [m for m in migrated_metrics
                             if m['id'] == 'timestamp' and
                             not ('timeAggregation' in m) or
                             not (m['timeAggregation'] is not None)
                             ]
            no_timestamp_keys = [m for m in migrated_metrics
                                 if m['id'] != 'timestamp' and
                                 not ('timeAggregation' in m) or
                                 not (m['timeAggregation'] is not None)
                                 ]
            values = [m for m in migrated_metrics
                      if 'timeAggregation' in m and
                      m['timeAggregation'] is not None
                      ]
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
        'scopeExpressionList': ignore,  # scope will be generated from 'filterExpression'
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


_DASHBOARD_CONVERTERS = {
    'v2': {
        'v1': _convert_dashboard_v1_to_v2
    }
}


def convert_dashboard_between_versions(dashboard, version_from, version_to):
    '''
    **Description**
        Converts a dashboard from a version to another version.
        Current conversions supported:
        - v1 -> v2

    **Arguments**
        - **version_from**: the version of the original dashboard to convert from
        - **version_to**: the version of the wanted dashboard

    **Success Return Value**
        A dashboard transformed between versions.
    '''
    converters_to = _DASHBOARD_CONVERTERS.get(version_to, None)
    if converters_to is None:
        return False, f'unexpected error: no dashboard converters from version {version_to} are supported'

    converter = converters_to.get(version_from, None)

    if converter is None:
        return False, 'dashboard version {} cannot be converted to {}'.format(version_from, version_to)

    try:
        return converter(dashboard)
    except Exception as err:
        return False, str(err)
