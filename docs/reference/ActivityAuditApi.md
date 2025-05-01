# sysdig_client.ActivityAuditApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity_audit_entries_supported_filters_v1**](ActivityAuditApi.md#get_activity_audit_entries_supported_filters_v1) | **GET** /secure/activity-audit/v1/supported-filters | Get available filters
[**get_activity_audit_entries_v1**](ActivityAuditApi.md#get_activity_audit_entries_v1) | **GET** /secure/activity-audit/v1/entries | List entries
[**get_activity_audit_entry_v1**](ActivityAuditApi.md#get_activity_audit_entry_v1) | **GET** /secure/activity-audit/v1/entries/{entryId} | Get entry


# **get_activity_audit_entries_supported_filters_v1**
> AuditSupportedFiltersResponse get_activity_audit_entries_supported_filters_v1()

Get available filters

Activity Audit entries can be filtered by a set of attributes. This endpoint returns the list of those for which filtering is supported. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.audit_supported_filters_response import AuditSupportedFiltersResponse
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
    api_instance = sysdig_client.ActivityAuditApi(api_client)

    try:
        # Get available filters
        api_response = api_instance.get_activity_audit_entries_supported_filters_v1()
        print("The response of ActivityAuditApi->get_activity_audit_entries_supported_filters_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAuditApi->get_activity_audit_entries_supported_filters_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditSupportedFiltersResponse**](AuditSupportedFiltersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of supported attributes for filtering Activity Audit entries. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Bad request |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_audit_entries_v1**
> EntriesResponse get_activity_audit_entries_v1(var_from=var_from, to=to, cursor=cursor, zones=zones, filter=filter, limit=limit, types=types)

List entries

Retrieves the list of entries matching the expressed search criteria. The pair `from` and `to` and the `cursor` parameter are mutually exclusive. If you supply a `from` and `to` you must not supply a `cursor` and vice-versa. The time criteria is required and can be specified in two different ways: - Using `from` and `to`, the list of entries within the timeframe (max 2 weeks) will be returned, starting from the most recent ones. - Using a `cursor` the entries returned will be in the before, after or around the entry, depending on the entry the cursor is taken from and the cursor type. More details are available in the `cursor` attribute in the response. The entry content can be filtered using `zones`, to select one or more zones, or with the filter, directly expressing a condition on fields and labels.  **Required permissions:** _commands.read_ | _connections.read_ | _fileaccesses.read_ | _kubernetes.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.entries_response import EntriesResponse
from sysdig_client.models.types import Types
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
    api_instance = sysdig_client.ActivityAuditApi(api_client)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    zones = [56] # List[int] |  (optional)
    filter = 'filter_example' # str |  (optional)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    types = sysdig_client.Types() # Types |  (optional)

    try:
        # List entries
        api_response = api_instance.get_activity_audit_entries_v1(var_from=var_from, to=to, cursor=cursor, zones=zones, filter=filter, limit=limit, types=types)
        print("The response of ActivityAuditApi->get_activity_audit_entries_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAuditApi->get_activity_audit_entries_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **zones** | [**List[int]**](int.md)|  | [optional] 
 **filter** | **str**|  | [optional] 
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **types** | [**Types**](.md)|  | [optional] 

### Return type

[**EntriesResponse**](EntriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of entries. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_audit_entry_v1**
> EntryResponse get_activity_audit_entry_v1(entry_id)

Get entry

Retrieves an Actvity Audit entry given its id. **Required permissions:** _commands.read_ | _connections.read_ | _fileaccesses.read_ | _kubernetes.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.entry_response import EntryResponse
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
    api_instance = sysdig_client.ActivityAuditApi(api_client)
    entry_id = 'entry_id_example' # str | 

    try:
        # Get entry
        api_response = api_instance.get_activity_audit_entry_v1(entry_id)
        print("The response of ActivityAuditApi->get_activity_audit_entry_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAuditApi->get_activity_audit_entry_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 

### Return type

[**EntryResponse**](EntryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Activity Audit entry. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

