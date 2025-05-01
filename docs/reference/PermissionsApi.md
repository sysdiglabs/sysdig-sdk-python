# sysdig_client.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissions_v1**](PermissionsApi.md#get_permissions_v1) | **GET** /platform/v1/permissions | Get Customer Permissions


# **get_permissions_v1**
> GetPermissionsResponseV1 get_permissions_v1(filter=filter)

Get Customer Permissions

Retrieve a list of permissions that are used in custom roles.\\ \\ **Required permissions:** _permissions.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_permissions_response_v1 import GetPermissionsResponseV1
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
    api_instance = sysdig_client.PermissionsApi(api_client)
    filter = '' # str | Filter by products when getting permissions for custom roles.\\ Avaliable products are: SDS, SDC.\\ You can specify a single product or a list of products separated by commas.\\ Product names are case-sensitive.\\ If not specified, all permissions are returned.  (optional) (default to '')

    try:
        # Get Customer Permissions
        api_response = api_instance.get_permissions_v1(filter=filter)
        print("The response of PermissionsApi->get_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter by products when getting permissions for custom roles.\\ Avaliable products are: SDS, SDC.\\ You can specify a single product or a list of products separated by commas.\\ Product names are case-sensitive.\\ If not specified, all permissions are returned.  | [optional] [default to &#39;&#39;]

### Return type

[**GetPermissionsResponseV1**](GetPermissionsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Display Permissions. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

