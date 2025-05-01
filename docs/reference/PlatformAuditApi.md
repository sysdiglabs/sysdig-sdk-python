# sysdig_client.PlatformAuditApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platform_audit_events_v1**](PlatformAuditApi.md#get_platform_audit_events_v1) | **GET** /platform/v1/platform-audit-events | Get Platform Audit Events


# **get_platform_audit_events_v1**
> ListAuditEventsResponse get_platform_audit_events_v1(var_from=var_from, to=to, cursor=cursor, filter=filter, limit=limit)

Get Platform Audit Events

Retrieve a paginated list of Platform Audit Events.\\ \\ **Required permissions:** _audit-trail-events.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.list_audit_events_response import ListAuditEventsResponse
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
    api_instance = sysdig_client.PlatformAuditApi(api_client)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Platform Audit Events
        api_response = api_instance.get_platform_audit_events_v1(var_from=var_from, to=to, cursor=cursor, filter=filter, limit=limit)
        print("The response of PlatformAuditApi->get_platform_audit_events_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformAuditApi->get_platform_audit_events_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ListAuditEventsResponse**](ListAuditEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Platform Audit Events. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

