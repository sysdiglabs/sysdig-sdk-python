# sysdig_client.ReportingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_jobs_v1**](ReportingApi.md#list_jobs_v1) | **GET** /platform/reporting/v1/jobs | List Report Job Runs
[**list_schedules_v1**](ReportingApi.md#list_schedules_v1) | **GET** /platform/reporting/v1/schedules | List Report Schedules


# **list_jobs_v1**
> ListJobs list_jobs_v1(schedule_id, report_id=report_id, is_report_template=is_report_template, completed_on=completed_on, job_type=job_type, status=status, kind=kind, policies=policies, zones=zones)

List Report Job Runs

Retrieve a list of Report Job runs.\\ \\ **Required permissions:** platform.reporting.report-downloads.read 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.list_jobs import ListJobs
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
    api_instance = sysdig_client.ReportingApi(api_client)
    schedule_id = '2pUnGeLvrOo5qoWuvXg5H9nEH2g' # str | ID of the Schedule
    report_id = 1 # int | ID of the Report (optional)
    is_report_template = 'true' # str | Indicates whether the report is a template. (optional)
    completed_on = 56 # int | Date the job was completed in epoch milliseconds. (optional)
    job_type = 'SCHEDULED' # str | Type of the job. (optional)
    status = 'COMPLETED' # str | Status of the job. (optional)
    kind = 'compliance_readiness' # str | Kind of the report. (optional)
    policies = '[1,2,3]' # str | List of policy IDs in string format. (optional)
    zones = '[1,2,3]' # str | List of zone IDs in string format. (optional)

    try:
        # List Report Job Runs
        api_response = api_instance.list_jobs_v1(schedule_id, report_id=report_id, is_report_template=is_report_template, completed_on=completed_on, job_type=job_type, status=status, kind=kind, policies=policies, zones=zones)
        print("The response of ReportingApi->list_jobs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->list_jobs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**| ID of the Schedule | 
 **report_id** | **int**| ID of the Report | [optional] 
 **is_report_template** | **str**| Indicates whether the report is a template. | [optional] 
 **completed_on** | **int**| Date the job was completed in epoch milliseconds. | [optional] 
 **job_type** | **str**| Type of the job. | [optional] 
 **status** | **str**| Status of the job. | [optional] 
 **kind** | **str**| Kind of the report. | [optional] 
 **policies** | **str**| List of policy IDs in string format. | [optional] 
 **zones** | **str**| List of zone IDs in string format. | [optional] 

### Return type

[**ListJobs**](ListJobs.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Report job runs. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedules_v1**
> ListSchedules list_schedules_v1()

List Report Schedules

Retrieve a paginated list of Report Schedules.\\ \\ **Required permissions:** platform.reporting.schedules.read 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.list_schedules import ListSchedules
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
    api_instance = sysdig_client.ReportingApi(api_client)

    try:
        # List Report Schedules
        api_response = api_instance.list_schedules_v1()
        print("The response of ReportingApi->list_schedules_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->list_schedules_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListSchedules**](ListSchedules.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Report schedules |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

