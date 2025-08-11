# sysdig_client.PrometheusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_admin_tsdb_clean_tombstones_v1**](PrometheusApi.md#get_admin_tsdb_clean_tombstones_v1) | **POST** /prometheus/api/v1/admin/tsdb/clean_tombstones | Clean Tombstones
[**get_admin_tsdb_delete_series_v1**](PrometheusApi.md#get_admin_tsdb_delete_series_v1) | **POST** /prometheus/api/v1/admin/tsdb/delete_series | Delete Series
[**get_admin_tsdb_snapshot_v1**](PrometheusApi.md#get_admin_tsdb_snapshot_v1) | **POST** /prometheus/api/v1/admin/tsdb/snapshot | Snapshot
[**get_alert_managers_v1**](PrometheusApi.md#get_alert_managers_v1) | **GET** /prometheus/api/v1//alertmanagers | Alertmanagers
[**get_alerts_v1**](PrometheusApi.md#get_alerts_v1) | **GET** /prometheus/api/v1/alerts | Alerts
[**get_exemplars_v1**](PrometheusApi.md#get_exemplars_v1) | **GET** /prometheus/api/v1/query_exemplars | Query Exemplars
[**get_format_query_v1**](PrometheusApi.md#get_format_query_v1) | **GET** /prometheus/api/v1/format_query | Format Query
[**get_label_values_v1**](PrometheusApi.md#get_label_values_v1) | **GET** /prometheus/api/v1/label/{labelName}/values | Labels Values Query
[**get_labels_v1**](PrometheusApi.md#get_labels_v1) | **GET** /prometheus/api/v1/labels | Labels Query
[**get_live_notifications_v1**](PrometheusApi.md#get_live_notifications_v1) | **GET** /prometheus/api/v1/notifications/live | Live Notifications
[**get_metadata_v1**](PrometheusApi.md#get_metadata_v1) | **GET** /prometheus/api/v1/metadata | Querying metric metadata
[**get_notifications_v1**](PrometheusApi.md#get_notifications_v1) | **GET** /prometheus/api/v1/notifications | Active Notifications
[**get_parse_query_v1**](PrometheusApi.md#get_parse_query_v1) | **GET** /prometheus/api/v1/parse_query | Parse Query
[**get_query_range_v1**](PrometheusApi.md#get_query_range_v1) | **GET** /prometheus/api/v1/query_range | Range Query
[**get_query_v1**](PrometheusApi.md#get_query_v1) | **GET** /prometheus/api/v1/query | Instant Query
[**get_rules_v1**](PrometheusApi.md#get_rules_v1) | **GET** /prometheus/api/v1/rules | Rules
[**get_series_v1**](PrometheusApi.md#get_series_v1) | **GET** /prometheus/api/v1/series | Series Query
[**get_status_build_info_v1**](PrometheusApi.md#get_status_build_info_v1) | **GET** /prometheus/api/v1/status/buildinfo | Build Information
[**get_status_config_v1**](PrometheusApi.md#get_status_config_v1) | **GET** /prometheus/api/v1/status/config | Config
[**get_status_flags_v1**](PrometheusApi.md#get_status_flags_v1) | **GET** /prometheus/api/v1/status/flags | Flags
[**get_status_runtime_info_v1**](PrometheusApi.md#get_status_runtime_info_v1) | **GET** /prometheus/api/v1/status/runtimeinfo | Runtime Information
[**get_status_tsdb_v1**](PrometheusApi.md#get_status_tsdb_v1) | **GET** /prometheus/api/v1/status/tsdb | TSDB Stats
[**get_status_wal_replay_v1**](PrometheusApi.md#get_status_wal_replay_v1) | **GET** /prometheus/api/v1/status/walreplay | WAL Replay
[**get_targets_metadata_v1**](PrometheusApi.md#get_targets_metadata_v1) | **GET** /prometheus/api/v1/targets/metadata | Querying target metadata
[**get_targets_v1**](PrometheusApi.md#get_targets_v1) | **GET** /prometheus/api/v1/targets | Targets
[**post_admin_tsdb_clean_tombstones_v1**](PrometheusApi.md#post_admin_tsdb_clean_tombstones_v1) | **PUT** /prometheus/api/v1/admin/tsdb/clean_tombstones | Clean Tombstones
[**post_admin_tsdb_delete_series_v1**](PrometheusApi.md#post_admin_tsdb_delete_series_v1) | **PUT** /prometheus/api/v1/admin/tsdb/delete_series | Delete Series
[**post_admin_tsdb_snapshot_v1**](PrometheusApi.md#post_admin_tsdb_snapshot_v1) | **PUT** /prometheus/api/v1/admin/tsdb/snapshot | Snapshot
[**post_exemplars_v1**](PrometheusApi.md#post_exemplars_v1) | **POST** /prometheus/api/v1/query_exemplars | Query Exemplars
[**post_format_query_v1**](PrometheusApi.md#post_format_query_v1) | **POST** /prometheus/api/v1/format_query | Format Query
[**post_labels_v1**](PrometheusApi.md#post_labels_v1) | **POST** /prometheus/api/v1/labels | Labels Query
[**post_parse_query_v1**](PrometheusApi.md#post_parse_query_v1) | **POST** /prometheus/api/v1/parse_query | Parse Query
[**post_query_range_v1**](PrometheusApi.md#post_query_range_v1) | **POST** /prometheus/api/v1/query_range | Range Query
[**post_query_v1**](PrometheusApi.md#post_query_v1) | **POST** /prometheus/api/v1/query | Instant Query
[**post_series_v1**](PrometheusApi.md#post_series_v1) | **POST** /prometheus/api/v1/series | Series Query
[**remote_write_v1**](PrometheusApi.md#remote_write_v1) | **POST** /prometheus/api/v1/write | Ingest metric data (remote write)


# **get_admin_tsdb_clean_tombstones_v1**
> get_admin_tsdb_clean_tombstones_v1()

Clean Tombstones

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Clean Tombstones
        api_instance.get_admin_tsdb_clean_tombstones_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_admin_tsdb_clean_tombstones_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_tsdb_delete_series_v1**
> get_admin_tsdb_delete_series_v1()

Delete Series

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Delete Series
        api_instance.get_admin_tsdb_delete_series_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_admin_tsdb_delete_series_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_tsdb_snapshot_v1**
> get_admin_tsdb_snapshot_v1()

Snapshot

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Snapshot
        api_instance.get_admin_tsdb_snapshot_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_admin_tsdb_snapshot_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_managers_v1**
> get_alert_managers_v1()

Alertmanagers

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Alertmanagers
        api_instance.get_alert_managers_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_alert_managers_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_v1**
> AlertsResponseV1 get_alerts_v1()

Alerts

Returns a list of active alerts that are currently firing in Prometheus.
\
**Required permissions:** _alerts.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.alerts_response_v1 import AlertsResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Alerts
        api_response = api_instance.get_alerts_v1()
        print("The response of PrometheusApi->get_alerts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_alerts_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertsResponseV1**](AlertsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of alerts. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exemplars_v1**
> get_exemplars_v1()

Query Exemplars

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Query Exemplars
        api_instance.get_exemplars_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_exemplars_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_format_query_v1**
> get_format_query_v1()

Format Query

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Format Query
        api_instance.get_format_query_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_format_query_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_label_values_v1**
> LabelValuesResponseV1 get_label_values_v1(label_name, start=start, end=end, match=match, limit=limit)

Labels Values Query

The following endpoint returns a list of label names:
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.label_values_response_v1 import LabelValuesResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    label_name = 'job' # str | The name of the label to retrieve values for.
    start = sysdig_client.QueryTime() # QueryTime | <b>UNSUPPORTED</b> - This parameter is not supported due to the Sysdig's specific implementation. (optional)
    end = sysdig_client.QueryTime() # QueryTime | <b>UNSUPPORTED</b> - Sysdig does not support this parameter. (optional)
    match = ['[\"{job=\\\"prometheus\\\"}\"]'] # List[str] | A repeated series selector argument that specifies the series from which to read the label values. (optional)
    limit = 56 # int | The maximum number of returned labels. This is 5,000 by default. To disable the limit, set the value to 0. (optional)

    try:
        # Labels Values Query
        api_response = api_instance.get_label_values_v1(label_name, start=start, end=end, match=match, limit=limit)
        print("The response of PrometheusApi->get_label_values_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_label_values_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_name** | **str**| The name of the label to retrieve values for. |
 **start** | [**QueryTime**](.md)| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - This parameter is not supported due to the Sysdig&#39;s specific implementation. | [optional]
 **end** | [**QueryTime**](.md)| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - Sysdig does not support this parameter. | [optional]
 **match** | [**List[str]**](str.md)| A repeated series selector argument that specifies the series from which to read the label values. | [optional]
 **limit** | **int**| The maximum number of returned labels. This is 5,000 by default. To disable the limit, set the value to 0. | [optional]

### Return type

[**LabelValuesResponseV1**](LabelValuesResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of labels. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_labels_v1**
> LabelsResponseV1 get_labels_v1(start=start, end=end, match=match, limit=limit)

Labels Query

The following endpoint returns a list of label names:
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.labels_response_v1 import LabelsResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    start = sysdig_client.QueryTime() # QueryTime | <b>UNSUPPORTED</b> - This parameter is not supported due to the Sysdig's specific implementation. (optional)
    end = sysdig_client.QueryTime() # QueryTime | <b>UNSUPPORTED</b> - Sysdig does not support this parameter. (optional)
    match = ['[\"{job=\\\"prometheus\\\"}\"]'] # List[str] | A repeated series selector argument that specifies the series from which to read the label names. (optional)
    limit = 56 # int | The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. (optional)

    try:
        # Labels Query
        api_response = api_instance.get_labels_v1(start=start, end=end, match=match, limit=limit)
        print("The response of PrometheusApi->get_labels_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_labels_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**QueryTime**](.md)| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - This parameter is not supported due to the Sysdig&#39;s specific implementation. | [optional]
 **end** | [**QueryTime**](.md)| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - Sysdig does not support this parameter. | [optional]
 **match** | [**List[str]**](str.md)| A repeated series selector argument that specifies the series from which to read the label names. | [optional]
 **limit** | **int**| The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. | [optional]

### Return type

[**LabelsResponseV1**](LabelsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of labels. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_notifications_v1**
> get_live_notifications_v1()

Live Notifications

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Live Notifications
        api_instance.get_live_notifications_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_live_notifications_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_v1**
> MetadataResponseV1 get_metadata_v1(limit_per_metric=limit_per_metric, limit=limit, metric=metric)

Querying metric metadata

The following endpoint returns a list of label names:
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.metadata_response_v1 import MetadataResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    limit_per_metric = 56 # int | <b>UNSUPPORTED</b> - Sysdig does not support this parameter. (optional)
    limit = 56 # int | The maximum number of metrics to return. To disable the limit, set the value to 0. (optional)
    metric = 'up' # str | A specific metric name to filter metadata for. If omitted, metadata for all metrics is retrieved. (optional)

    try:
        # Querying metric metadata
        api_response = api_instance.get_metadata_v1(limit_per_metric=limit_per_metric, limit=limit, metric=metric)
        print("The response of PrometheusApi->get_metadata_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_metadata_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_per_metric** | **int**| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - Sysdig does not support this parameter. | [optional]
 **limit** | **int**| The maximum number of metrics to return. To disable the limit, set the value to 0. | [optional]
 **metric** | **str**| A specific metric name to filter metadata for. If omitted, metadata for all metrics is retrieved. | [optional]

### Return type

[**MetadataResponseV1**](MetadataResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_v1**
> get_notifications_v1()

Active Notifications

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Active Notifications
        api_instance.get_notifications_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_notifications_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parse_query_v1**
> get_parse_query_v1()

Parse Query

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Parse Query
        api_instance.get_parse_query_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_parse_query_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_range_v1**
> QueryResponseV1 get_query_range_v1(query, start, end, step, timeout=timeout, limit=limit)

Range Query

This endpoint evaluates an expression query over a specified time range.
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.query_response_v1 import QueryResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    query = 'up' # str | The Prometheus expression query string.
    start = sysdig_client.QueryTime() # QueryTime | The inclusive start timestamp of the query range as RFC3339 or a unix timestamp.
    end = sysdig_client.QueryTime() # QueryTime | The inclusive end timestamp of the query range as RFC3339 or a unix timestamp.
    step = sysdig_client.GetQueryRangeV1StepParameter() # GetQueryRangeV1StepParameter | The query resolution step width, specified as a duration or a floating-point number of seconds.
    timeout = 'timeout_example' # str | The evaluation timeout. The default is 2 minutes. (optional)
    limit = 56 # int | The maximum number of returned series. To disable the limit, set the value to 0. (optional)

    try:
        # Range Query
        api_response = api_instance.get_query_range_v1(query, start, end, step, timeout=timeout, limit=limit)
        print("The response of PrometheusApi->get_query_range_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_query_range_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The Prometheus expression query string. |
 **start** | [**QueryTime**](.md)| The inclusive start timestamp of the query range as RFC3339 or a unix timestamp. |
 **end** | [**QueryTime**](.md)| The inclusive end timestamp of the query range as RFC3339 or a unix timestamp. |
 **step** | [**GetQueryRangeV1StepParameter**](.md)| The query resolution step width, specified as a duration or a floating-point number of seconds. |
 **timeout** | **str**| The evaluation timeout. The default is 2 minutes. | [optional]
 **limit** | **int**| The maximum number of returned series. To disable the limit, set the value to 0. | [optional]

### Return type

[**QueryResponseV1**](QueryResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Range query result. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Operation failed due to unprocessable entity. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_v1**
> QueryResponseV1 get_query_v1(query, time=time, timeout=timeout, limit=limit)

Instant Query

This endpoint evaluates an instant query at a single point in time.
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.query_response_v1 import QueryResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    query = 'up' # str | The Prometheus expression query string.
    time = sysdig_client.QueryTime() # QueryTime | The evaluation timestamp as RFC3339 or a unix timestamp. If omitted, the current server time is used. (optional)
    timeout = 'timeout_example' # str | The evaluation timeout. The default is 2 minutes. (optional)
    limit = 56 # int | The maximum number of returned series. To disable the limit, set the value to 0. (optional)

    try:
        # Instant Query
        api_response = api_instance.get_query_v1(query, time=time, timeout=timeout, limit=limit)
        print("The response of PrometheusApi->get_query_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_query_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The Prometheus expression query string. |
 **time** | [**QueryTime**](.md)| The evaluation timestamp as RFC3339 or a unix timestamp. If omitted, the current server time is used. | [optional]
 **timeout** | **str**| The evaluation timeout. The default is 2 minutes. | [optional]
 **limit** | **int**| The maximum number of returned series. To disable the limit, set the value to 0. | [optional]

### Return type

[**QueryResponseV1**](QueryResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instant query result. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_v1**
> RulesResponseV1 get_rules_v1(type=type, rule_name=rule_name, rule_group=rule_group, file=file, exclude_alerts=exclude_alerts, match=match, group_limit=group_limit, group_next_token=group_next_token)

Rules

The /rules API endpoint returns the list of alerting rules. It also returns the currently active alerts fired by the Prometheus instance of each alerting rule.
\
Sysdig currently does not support recording rules.
\
**Required permissions:** _alerts.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.rules_response_v1 import RulesResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    type = 'type_example' # str | This endpoint only returns alerting rules (`type=alert`). When absent or empty, only alerting rules are returned. (optional)
    rule_name = ['rule_name_example'] # List[str] | Only return rules with the given rule name. If repeated, rules with any of the provided names are returned. (optional)
    rule_group = ['rule_group_example'] # List[str] | Only return rules with the given rule group name. If repeated, rules with any of the provided group names are returned. (optional)
    file = ['file_example'] # List[str] | <b>UNSUPPORTED</b> - Sysdig does not support this parameter. (optional)
    exclude_alerts = True # bool | This endpoint supports only returning alerting rules (`exclude_alerts=true`). (optional)
    match = ['match_example'] # List[str] | Only return rules with configured labels that satisfy the label selectors. (optional)
    group_limit = 56 # int | Limit the number of rule groups returned in a single response. (optional)
    group_next_token = 'group_next_token_example' # str | <b>UNSUPPORTED</b> - This parameter is not supported due to the Sysdig's specific implementation. (optional)

    try:
        # Rules
        api_response = api_instance.get_rules_v1(type=type, rule_name=rule_name, rule_group=rule_group, file=file, exclude_alerts=exclude_alerts, match=match, group_limit=group_limit, group_next_token=group_next_token)
        print("The response of PrometheusApi->get_rules_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_rules_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| This endpoint only returns alerting rules (&#x60;type&#x3D;alert&#x60;). When absent or empty, only alerting rules are returned. | [optional]
 **rule_name** | [**List[str]**](str.md)| Only return rules with the given rule name. If repeated, rules with any of the provided names are returned. | [optional]
 **rule_group** | [**List[str]**](str.md)| Only return rules with the given rule group name. If repeated, rules with any of the provided group names are returned. | [optional]
 **file** | [**List[str]**](str.md)| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - Sysdig does not support this parameter. | [optional]
 **exclude_alerts** | **bool**| This endpoint supports only returning alerting rules (&#x60;exclude_alerts&#x3D;true&#x60;). | [optional]
 **match** | [**List[str]**](str.md)| Only return rules with configured labels that satisfy the label selectors. | [optional]
 **group_limit** | **int**| Limit the number of rule groups returned in a single response. | [optional]
 **group_next_token** | **str**| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - This parameter is not supported due to the Sysdig&#39;s specific implementation. | [optional]

### Return type

[**RulesResponseV1**](RulesResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of rules. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series_v1**
> SeriesResponseV1 get_series_v1(match, start=start, end=end, limit=limit)

Series Query

The following endpoint returns the list of time series that match a specified label set.
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.series_response_v1 import SeriesResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    match = ['[\"up\",\"process_start_time_seconds{job=\\\"prometheus\\\"}\"]'] # List[str] | A repeated series selector argument that specifies the series to return. You must provide at least one match[] parameter.
    start = sysdig_client.QueryTime() # QueryTime | The inclusive start timestamp of the series query as RFC3339 or a unix timestamp. (optional)
    end = sysdig_client.QueryTime() # QueryTime | The inclusive end timestamp of the series query as RFC3339 or a unix timestamp. (optional)
    limit = 56 # int | The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. (optional)

    try:
        # Series Query
        api_response = api_instance.get_series_v1(match, start=start, end=end, limit=limit)
        print("The response of PrometheusApi->get_series_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->get_series_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match** | [**List[str]**](str.md)| A repeated series selector argument that specifies the series to return. You must provide at least one match[] parameter. |
 **start** | [**QueryTime**](.md)| The inclusive start timestamp of the series query as RFC3339 or a unix timestamp. | [optional]
 **end** | [**QueryTime**](.md)| The inclusive end timestamp of the series query as RFC3339 or a unix timestamp. | [optional]
 **limit** | **int**| The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. | [optional]

### Return type

[**SeriesResponseV1**](SeriesResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of time series. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Operation failed due to unprocessable entity. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_build_info_v1**
> get_status_build_info_v1()

Build Information

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Build Information
        api_instance.get_status_build_info_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_status_build_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_config_v1**
> get_status_config_v1()

Config

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Config
        api_instance.get_status_config_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_status_config_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_flags_v1**
> get_status_flags_v1()

Flags

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Flags
        api_instance.get_status_flags_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_status_flags_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_runtime_info_v1**
> get_status_runtime_info_v1()

Runtime Information

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Runtime Information
        api_instance.get_status_runtime_info_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_status_runtime_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_tsdb_v1**
> get_status_tsdb_v1()

TSDB Stats

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # TSDB Stats
        api_instance.get_status_tsdb_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_status_tsdb_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_wal_replay_v1**
> get_status_wal_replay_v1()

WAL Replay

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # WAL Replay
        api_instance.get_status_wal_replay_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_status_wal_replay_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_targets_metadata_v1**
> get_targets_metadata_v1()

Querying target metadata

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Querying target metadata
        api_instance.get_targets_metadata_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_targets_metadata_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_targets_v1**
> get_targets_v1()

Targets

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Targets
        api_instance.get_targets_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->get_targets_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_admin_tsdb_clean_tombstones_v1**
> post_admin_tsdb_clean_tombstones_v1()

Clean Tombstones

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Clean Tombstones
        api_instance.post_admin_tsdb_clean_tombstones_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->post_admin_tsdb_clean_tombstones_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_admin_tsdb_delete_series_v1**
> post_admin_tsdb_delete_series_v1()

Delete Series

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Delete Series
        api_instance.post_admin_tsdb_delete_series_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->post_admin_tsdb_delete_series_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_admin_tsdb_snapshot_v1**
> post_admin_tsdb_snapshot_v1()

Snapshot

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Snapshot
        api_instance.post_admin_tsdb_snapshot_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->post_admin_tsdb_snapshot_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_exemplars_v1**
> post_exemplars_v1()

Query Exemplars

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Query Exemplars
        api_instance.post_exemplars_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->post_exemplars_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_format_query_v1**
> post_format_query_v1()

Format Query

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Format Query
        api_instance.post_format_query_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->post_format_query_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_labels_v1**
> LabelsResponseV1 post_labels_v1(start=start, end=end, match=match, limit=limit)

Labels Query

The following endpoint returns a list of label names:
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.labels_response_v1 import LabelsResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    start = sysdig_client.QueryTime() # QueryTime | <b>UNSUPPORTED</b> - This parameter is not supported due to the Sysdig's specific implementation. (optional)
    end = sysdig_client.QueryTime() # QueryTime | <b>UNSUPPORTED</b> - Sysdig does not support this parameter. (optional)
    match = ['[\"{job=\\\"prometheus\\\"}\"]'] # List[str] | A repeated series selector argument that specifies the series from which to read the label names. (optional)
    limit = 56 # int | The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. (optional)

    try:
        # Labels Query
        api_response = api_instance.post_labels_v1(start=start, end=end, match=match, limit=limit)
        print("The response of PrometheusApi->post_labels_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->post_labels_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**QueryTime**](.md)| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - This parameter is not supported due to the Sysdig&#39;s specific implementation. | [optional]
 **end** | [**QueryTime**](.md)| &lt;b&gt;UNSUPPORTED&lt;/b&gt; - Sysdig does not support this parameter. | [optional]
 **match** | [**List[str]**](str.md)| A repeated series selector argument that specifies the series from which to read the label names. | [optional]
 **limit** | **int**| The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. | [optional]

### Return type

[**LabelsResponseV1**](LabelsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of labels. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_parse_query_v1**
> post_parse_query_v1()

Parse Query

This endpoint is NOT SUPPORTED.


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)

    try:
        # Parse Query
        api_instance.post_parse_query_v1()
    except Exception as e:
        print("Exception when calling PrometheusApi->post_parse_query_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_query_range_v1**
> QueryResponseV1 post_query_range_v1(query, start, end, step, timeout=timeout, limit=limit)

Range Query

This endpoint evaluates an expression query over a specified time range.
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.query_response_v1 import QueryResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    query = 'up' # str | The Prometheus expression query string.
    start = sysdig_client.QueryTime() # QueryTime | The inclusive start timestamp of the query range as RFC3339 or a unix timestamp.
    end = sysdig_client.QueryTime() # QueryTime | The inclusive end timestamp of the query range as RFC3339 or a unix timestamp.
    step = sysdig_client.GetQueryRangeV1StepParameter() # GetQueryRangeV1StepParameter | The query resolution step width, specified as a duration or a floating-point number of seconds.
    timeout = 'timeout_example' # str | The evaluation timeout. The default is 2 minutes. (optional)
    limit = 56 # int | The maximum number of returned series. To disable the limit, set the value to 0. (optional)

    try:
        # Range Query
        api_response = api_instance.post_query_range_v1(query, start, end, step, timeout=timeout, limit=limit)
        print("The response of PrometheusApi->post_query_range_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->post_query_range_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The Prometheus expression query string. |
 **start** | [**QueryTime**](.md)| The inclusive start timestamp of the query range as RFC3339 or a unix timestamp. |
 **end** | [**QueryTime**](.md)| The inclusive end timestamp of the query range as RFC3339 or a unix timestamp. |
 **step** | [**GetQueryRangeV1StepParameter**](.md)| The query resolution step width, specified as a duration or a floating-point number of seconds. |
 **timeout** | **str**| The evaluation timeout. The default is 2 minutes. | [optional]
 **limit** | **int**| The maximum number of returned series. To disable the limit, set the value to 0. | [optional]

### Return type

[**QueryResponseV1**](QueryResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Range query result. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Operation failed due to unprocessable entity. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_query_v1**
> QueryResponseV1 post_query_v1(query, time=time, timeout=timeout, limit=limit)

Instant Query

This endpoint evaluates an instant query at a single point in time.
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.query_response_v1 import QueryResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    query = 'up' # str | The Prometheus expression query string.
    time = sysdig_client.QueryTime() # QueryTime | The evaluation timestamp as RFC3339 or a unix timestamp. If omitted, the current server time is used. (optional)
    timeout = 'timeout_example' # str | The evaluation timeout. The default is 2 minutes. (optional)
    limit = 56 # int | The maximum number of returned series. To disable the limit, set the value to 0. (optional)

    try:
        # Instant Query
        api_response = api_instance.post_query_v1(query, time=time, timeout=timeout, limit=limit)
        print("The response of PrometheusApi->post_query_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->post_query_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The Prometheus expression query string. |
 **time** | [**QueryTime**](.md)| The evaluation timestamp as RFC3339 or a unix timestamp. If omitted, the current server time is used. | [optional]
 **timeout** | **str**| The evaluation timeout. The default is 2 minutes. | [optional]
 **limit** | **int**| The maximum number of returned series. To disable the limit, set the value to 0. | [optional]

### Return type

[**QueryResponseV1**](QueryResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instant query result. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_series_v1**
> SeriesResponseV1 post_series_v1(match, start=start, end=end, limit=limit)

Series Query

The following endpoint returns the list of time series that match a specified label set.
\
**Required permissions:** _metrics-data.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.series_response_v1 import SeriesResponseV1
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    match = ['[\"up\",\"process_start_time_seconds{job=\\\"prometheus\\\"}\"]'] # List[str] | A repeated series selector argument that specifies the series to return. You must provide at least one match[] parameter.
    start = sysdig_client.QueryTime() # QueryTime | The inclusive start timestamp of the series query as RFC3339 or a unix timestamp. (optional)
    end = sysdig_client.QueryTime() # QueryTime | The inclusive end timestamp of the series query as RFC3339 or a unix timestamp. (optional)
    limit = 56 # int | The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. (optional)

    try:
        # Series Query
        api_response = api_instance.post_series_v1(match, start=start, end=end, limit=limit)
        print("The response of PrometheusApi->post_series_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->post_series_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match** | [**List[str]**](str.md)| A repeated series selector argument that specifies the series to return. You must provide at least one match[] parameter. |
 **start** | [**QueryTime**](.md)| The inclusive start timestamp of the series query as RFC3339 or a unix timestamp. | [optional]
 **end** | [**QueryTime**](.md)| The inclusive end timestamp of the series query as RFC3339 or a unix timestamp. | [optional]
 **limit** | **int**| The maximum number of returned series. The limit is capped at 10,000. To disable the limit, set the value to 0. | [optional]

### Return type

[**SeriesResponseV1**](SeriesResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of time series. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Operation failed due to unprocessable entity. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_write_v1**
> str remote_write_v1(body)

Ingest metric data (remote write)

Accepts a Protobuf-encoded Snappy-compressed request containing time series data. Used for remote write integrations.
\
**Required permissions:** _ingest.prws_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.PrometheusApi(api_client)
    body = None # bytearray |

    try:
        # Ingest metric data (remote write)
        api_response = api_instance.remote_write_v1(body)
        print("The response of PrometheusApi->remote_write_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrometheusApi->remote_write_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  |

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-protobuf
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation message. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

