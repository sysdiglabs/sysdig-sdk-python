# sysdig_client.MetricsCollectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_disabled_metrics_by_job_v1**](MetricsCollectionApi.md#get_disabled_metrics_by_job_v1) | **GET** /monitor/prometheus-jobs/v1/disabled-metrics | List disabled metrics collection for Jobs.
[**post_disabled_metrics_v1**](MetricsCollectionApi.md#post_disabled_metrics_v1) | **POST** /monitor/prometheus-jobs/v1/disabled-metrics | Disable or re-enable metrics collection for Jobs


# **get_disabled_metrics_by_job_v1**
> ResponseListDisabledMetricsV1 get_disabled_metrics_by_job_v1(job_name=job_name, metric_name=metric_name)

List disabled metrics collection for Jobs.

List all disabled metrics per Job.\\ \\ **Required permissions:** Integrations Read 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.response_list_disabled_metrics_v1 import ResponseListDisabledMetricsV1
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
    api_instance = sysdig_client.MetricsCollectionApi(api_client)
    job_name = 'job-name-default' # str | The name of the Prometheus Job whose excluded metrics are to be listed.  (optional)
    metric_name = 'apache_accesses_total' # str | The exact name of the metric to be filtered.  (optional)

    try:
        # List disabled metrics collection for Jobs.
        api_response = api_instance.get_disabled_metrics_by_job_v1(job_name=job_name, metric_name=metric_name)
        print("The response of MetricsCollectionApi->get_disabled_metrics_by_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->get_disabled_metrics_by_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| The name of the Prometheus Job whose excluded metrics are to be listed.  | [optional] 
 **metric_name** | **str**| The exact name of the metric to be filtered.  | [optional] 

### Return type

[**ResponseListDisabledMetricsV1**](ResponseListDisabledMetricsV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of disabled metrics associated with the specified Job. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_disabled_metrics_v1**
> ResponseListDisabledMetricsV1 post_disabled_metrics_v1(request_body_disabled_metrics_v1=request_body_disabled_metrics_v1)

Disable or re-enable metrics collection for Jobs

Disable specific metric collection for a specified Job. \\ This API supports specifying multiple Jobs, each with its own list of metrics to be disabled. \\ Additionally, you can use the same API to re-enable metrics that were previously disabled.\\ \\ **Required permissions:**  Integrations Full Access 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.request_body_disabled_metrics_v1 import RequestBodyDisabledMetricsV1
from sysdig_client.models.response_list_disabled_metrics_v1 import ResponseListDisabledMetricsV1
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
    api_instance = sysdig_client.MetricsCollectionApi(api_client)
    request_body_disabled_metrics_v1 = sysdig_client.RequestBodyDisabledMetricsV1() # RequestBodyDisabledMetricsV1 |  (optional)

    try:
        # Disable or re-enable metrics collection for Jobs
        api_response = api_instance.post_disabled_metrics_v1(request_body_disabled_metrics_v1=request_body_disabled_metrics_v1)
        print("The response of MetricsCollectionApi->post_disabled_metrics_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->post_disabled_metrics_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body_disabled_metrics_v1** | [**RequestBodyDisabledMetricsV1**](RequestBodyDisabledMetricsV1.md)|  | [optional] 

### Return type

[**ResponseListDisabledMetricsV1**](ResponseListDisabledMetricsV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All Jobs and metrics have been disabled/re-enabled successfully. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**207** | Some metrics could not be disabled/re-enabled. Check the error information for further explanation. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

