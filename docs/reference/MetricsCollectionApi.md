# sysdig_client.MetricsCollectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_prometheus_job_v1**](MetricsCollectionApi.md#create_custom_prometheus_job_v1) | **POST** /monitor/prometheus-jobs/v1alpha1/custom-jobs/{jobName} | Create Custom Prometheus job
[**delete_custom_prometheus_job_by_id_v1**](MetricsCollectionApi.md#delete_custom_prometheus_job_by_id_v1) | **DELETE** /monitor/prometheus-jobs/v1alpha1/custom-jobs/{jobName} | Delete Custom Prometheus job
[**get_custom_prometheus_job_by_name_v1**](MetricsCollectionApi.md#get_custom_prometheus_job_by_name_v1) | **GET** /monitor/prometheus-jobs/v1alpha1/custom-jobs/{jobName} | Get Custom Prometheus Job
[**get_custom_prometheus_job_enablement_v1**](MetricsCollectionApi.md#get_custom_prometheus_job_enablement_v1) | **GET** /monitor/prometheus-jobs/v1alpha1/custom-jobs/{jobName}/enablement | Get Custom Prometheus Job enablement
[**get_custom_prometheus_jobs_v1**](MetricsCollectionApi.md#get_custom_prometheus_jobs_v1) | **GET** /monitor/prometheus-jobs/v1alpha1/custom-jobs | List Custom Prometheus jobs
[**get_disabled_metrics_by_job_v1**](MetricsCollectionApi.md#get_disabled_metrics_by_job_v1) | **GET** /monitor/prometheus-jobs/v1/disabled-metrics | List disabled metrics collection for Jobs.
[**post_disabled_metrics_v1**](MetricsCollectionApi.md#post_disabled_metrics_v1) | **POST** /monitor/prometheus-jobs/v1/disabled-metrics | Disable or re-enable metrics collection for Jobs
[**update_custom_prometheus_job_by_id_v1**](MetricsCollectionApi.md#update_custom_prometheus_job_by_id_v1) | **PUT** /monitor/prometheus-jobs/v1alpha1/custom-jobs/{jobName} | Update Custom Prometheus Job
[**update_custom_prometheus_job_enablement_v1**](MetricsCollectionApi.md#update_custom_prometheus_job_enablement_v1) | **PUT** /monitor/prometheus-jobs/v1alpha1/custom-jobs/{jobName}/enablement | Update Custom Prometheus Job enablement


# **create_custom_prometheus_job_v1**
> str create_custom_prometheus_job_v1(job_name, body=body)

Create Custom Prometheus job

Create a custom Prometheus job.
\
The body of the request must be a valid `scrape_config` as defined here: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config\
\
The custom job will be disabled by default and must be enabled with the `/monitor/prometheus-jobs/v1alpha1/custom-jobs/{jobName}/enablement` api.
\
You can override the standard Sysdig integration jobs using the same job name. The job names are available here: https://docs.sysdig.com/en/docs/sysdig-monitor/integrations/monitoring-integrations/configure-default-integrations/#supported-monitoring-integrations
\
**CAUTION**: the content of the job must be validated according to the Prometheus Scrape Config job definition. Any misconfiguration here can lead the Agent to fail the job parsing and stop sending custom metrics for all jobs.
\
**Required permissions:**  _promcat.integrations.admin_


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
    api_instance = sysdig_client.MetricsCollectionApi(api_client)
    job_name = 'my-custom-job' # str | The custom Prometheus job name.
    body = 'body_example' # str | The payload to create a custom job. Content must be a valid Prometheus `scrape_config`. (optional)

    try:
        # Create Custom Prometheus job
        api_response = api_instance.create_custom_prometheus_job_v1(job_name, body=body)
        print("The response of MetricsCollectionApi->create_custom_prometheus_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->create_custom_prometheus_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| The custom Prometheus job name. |
 **body** | **str**| The payload to create a custom job. Content must be a valid Prometheus &#x60;scrape_config&#x60;. | [optional]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/yaml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom Prometheus job created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_prometheus_job_by_id_v1**
> delete_custom_prometheus_job_by_id_v1(job_name)

Delete Custom Prometheus job

Delete a custom Prometheus job by its name.\
\
**Required permissions:**  _promcat.integrations.admin_


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
    api_instance = sysdig_client.MetricsCollectionApi(api_client)
    job_name = 'my-custom-job' # str | The custom Prometheus job name.

    try:
        # Delete Custom Prometheus job
        api_instance.delete_custom_prometheus_job_by_id_v1(job_name)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->delete_custom_prometheus_job_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| The custom Prometheus job name. |

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
**204** | Custom Prometheus job deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_prometheus_job_by_name_v1**
> str get_custom_prometheus_job_by_name_v1(job_name)

Get Custom Prometheus Job

Retrieve a custom Prometheus job by its name.\
\
**Required permissions:**  _promcat.integrations.read_


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
    api_instance = sysdig_client.MetricsCollectionApi(api_client)
    job_name = 'my-custom-job' # str | The custom Prometheus job name.

    try:
        # Get Custom Prometheus Job
        api_response = api_instance.get_custom_prometheus_job_by_name_v1(job_name)
        print("The response of MetricsCollectionApi->get_custom_prometheus_job_by_name_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->get_custom_prometheus_job_by_name_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| The custom Prometheus job name. |

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Prometheus Job found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_prometheus_job_enablement_v1**
> CustomJobsEnablementV1 get_custom_prometheus_job_enablement_v1(job_name)

Get Custom Prometheus Job enablement

Retrieve the enablement state of a custom Prometheus job by its name.\
\
**Required permissions:**  _promcat.integrations.admin_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.custom_jobs_enablement_v1 import CustomJobsEnablementV1
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
    job_name = 'my-custom-job' # str | The custom Prometheus job name.

    try:
        # Get Custom Prometheus Job enablement
        api_response = api_instance.get_custom_prometheus_job_enablement_v1(job_name)
        print("The response of MetricsCollectionApi->get_custom_prometheus_job_enablement_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->get_custom_prometheus_job_enablement_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| The custom Prometheus job name. |

### Return type

[**CustomJobsEnablementV1**](CustomJobsEnablementV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Prometheus job found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_prometheus_jobs_v1**
> GetCustomJobsPaginatedResponseV1 get_custom_prometheus_jobs_v1(offset=offset, limit=limit)

List Custom Prometheus jobs

Retrieve a paginated list of custom Prometheus jobs.\
\
**Required permissions:** _promcat.integrations.read_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_custom_jobs_paginated_response_v1 import GetCustomJobsPaginatedResponseV1
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
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)

    try:
        # List Custom Prometheus jobs
        api_response = api_instance.get_custom_prometheus_jobs_v1(offset=offset, limit=limit)
        print("The response of MetricsCollectionApi->get_custom_prometheus_jobs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->get_custom_prometheus_jobs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]

### Return type

[**GetCustomJobsPaginatedResponseV1**](GetCustomJobsPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custom jobs page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disabled_metrics_by_job_v1**
> ResponseListDisabledMetricsV1 get_disabled_metrics_by_job_v1(job_name=job_name, metric_name=metric_name)

List disabled metrics collection for Jobs.

List all disabled metrics per Job.\
\
**Required permissions:** Integrations Read


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

Disable specific metric collection for a specified Job. \
This API supports specifying multiple Jobs, each with its own list of metrics to be disabled. \
Additionally, you can use the same API to re-enable metrics that were previously disabled.\
\
**Required permissions:**  Integrations Full Access


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

# **update_custom_prometheus_job_by_id_v1**
> str update_custom_prometheus_job_by_id_v1(job_name, body=body)

Update Custom Prometheus Job

Update a custom Prometheus job.
\
The body of the request must be a valid `scrape_config` as defined here: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config\
\
You can override the standard Sysdig integration jobs using the same job name. The job names are available here: https://docs.sysdig.com/en/docs/sysdig-monitor/integrations/monitoring-integrations/configure-default-integrations/#supported-monitoring-integrations
\
**CAUTION**: the content of the job must be validated according to the Prometheus Scrape Config job definition. Any misconfiguration here can lead the Agent to fail the job parsing and stop sending custom metrics for all jobs.
\
**Required permissions:**  _promcat.integrations.admin_


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
    api_instance = sysdig_client.MetricsCollectionApi(api_client)
    job_name = 'my-custom-job' # str | The custom Prometheus job name.
    body = 'body_example' # str | The custom Prometheus job yaml content (optional)

    try:
        # Update Custom Prometheus Job
        api_response = api_instance.update_custom_prometheus_job_by_id_v1(job_name, body=body)
        print("The response of MetricsCollectionApi->update_custom_prometheus_job_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->update_custom_prometheus_job_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| The custom Prometheus job name. |
 **body** | **str**| The custom Prometheus job yaml content | [optional]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/yaml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Prometheus job updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_prometheus_job_enablement_v1**
> CustomJobsEnablementV1 update_custom_prometheus_job_enablement_v1(job_name, custom_jobs_enablement_v1=custom_jobs_enablement_v1)

Update Custom Prometheus Job enablement

Update the enablement state of a custom Prometheus job by its name.\
\
**Required permissions:** _promcat.integrations.admin_


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.custom_jobs_enablement_v1 import CustomJobsEnablementV1
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
    job_name = 'my-custom-job' # str | The custom Prometheus job name.
    custom_jobs_enablement_v1 = sysdig_client.CustomJobsEnablementV1() # CustomJobsEnablementV1 | The payload required to enable the custom Prometheus job. (optional)

    try:
        # Update Custom Prometheus Job enablement
        api_response = api_instance.update_custom_prometheus_job_enablement_v1(job_name, custom_jobs_enablement_v1=custom_jobs_enablement_v1)
        print("The response of MetricsCollectionApi->update_custom_prometheus_job_enablement_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsCollectionApi->update_custom_prometheus_job_enablement_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| The custom Prometheus job name. |
 **custom_jobs_enablement_v1** | [**CustomJobsEnablementV1**](CustomJobsEnablementV1.md)| The payload required to enable the custom Prometheus job. | [optional]

### Return type

[**CustomJobsEnablementV1**](CustomJobsEnablementV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Prometheus job enablement updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

