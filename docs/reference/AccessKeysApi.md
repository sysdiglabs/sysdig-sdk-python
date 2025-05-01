# sysdig_client.AccessKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_key_v1**](AccessKeysApi.md#create_access_key_v1) | **POST** /platform/v1/access-keys | Create Access Key
[**delete_access_key_by_id_v1**](AccessKeysApi.md#delete_access_key_by_id_v1) | **DELETE** /platform/v1/access-keys/{accessKeyId} | Delete Access Key
[**get_access_key_by_id_v1**](AccessKeysApi.md#get_access_key_by_id_v1) | **GET** /platform/v1/access-keys/{accessKeyId} | Get Access Key
[**get_access_keys_v1**](AccessKeysApi.md#get_access_keys_v1) | **GET** /platform/v1/access-keys | List Access Keys
[**update_access_key_by_id_v1**](AccessKeysApi.md#update_access_key_by_id_v1) | **PUT** /platform/v1/access-keys/{accessKeyId} | Update Access Key


# **create_access_key_v1**
> AccessKeyResponseV1 create_access_key_v1(create_access_key_request_v1=create_access_key_request_v1)

Create Access Key

Create a new access key.\\ \\ **Required permissions:** _customer-access-keys.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.access_key_response_v1 import AccessKeyResponseV1
from sysdig_client.models.create_access_key_request_v1 import CreateAccessKeyRequestV1
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
    api_instance = sysdig_client.AccessKeysApi(api_client)
    create_access_key_request_v1 = sysdig_client.CreateAccessKeyRequestV1() # CreateAccessKeyRequestV1 |  (optional)

    try:
        # Create Access Key
        api_response = api_instance.create_access_key_v1(create_access_key_request_v1=create_access_key_request_v1)
        print("The response of AccessKeysApi->create_access_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessKeysApi->create_access_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_access_key_request_v1** | [**CreateAccessKeyRequestV1**](CreateAccessKeyRequestV1.md)|  | [optional] 

### Return type

[**AccessKeyResponseV1**](AccessKeyResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Access key created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_key_by_id_v1**
> delete_access_key_by_id_v1(access_key_id)

Delete Access Key

Delete an access key by id.\\ \\ **Required permissions:** customer-access-keys.edit_ 

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
    api_instance = sysdig_client.AccessKeysApi(api_client)
    access_key_id = 56 # int | The access key id.

    try:
        # Delete Access Key
        api_instance.delete_access_key_by_id_v1(access_key_id)
    except Exception as e:
        print("Exception when calling AccessKeysApi->delete_access_key_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_id** | **int**| The access key id. | 

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
**204** | Access key deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_key_by_id_v1**
> AccessKeyResponseV1 get_access_key_by_id_v1(access_key_id)

Get Access Key

Return an access key by id.\\ \\ **Required permissions:** _customer-access-keys.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.access_key_response_v1 import AccessKeyResponseV1
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
    api_instance = sysdig_client.AccessKeysApi(api_client)
    access_key_id = 56 # int | The access key id.

    try:
        # Get Access Key
        api_response = api_instance.get_access_key_by_id_v1(access_key_id)
        print("The response of AccessKeysApi->get_access_key_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessKeysApi->get_access_key_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_id** | **int**| The access key id. | 

### Return type

[**AccessKeyResponseV1**](AccessKeyResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access key found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_keys_v1**
> GetAccessKeysPaginatedResponseV1 get_access_keys_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)

List Access Keys

Retrieve a paginated list of access keys.\\ \\ **Required permissions:** _customer-access-keys.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_access_keys_paginated_response_v1 import GetAccessKeysPaginatedResponseV1
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
    api_instance = sysdig_client.AccessKeysApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    orderby = '' # str | The order by field separated by a colon for the direction (optional) (default to '')
    filter = [] # List[str] | Filters to apply in the form of `key:value`.\\ Multiple filters can be applied by repeating the `filter` parameter:\\ `&filter=key1:value1&filter=key2:value2`  (optional) (default to [])

    try:
        # List Access Keys
        api_response = api_instance.get_access_keys_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)
        print("The response of AccessKeysApi->get_access_keys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessKeysApi->get_access_keys_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **orderby** | **str**| The order by field separated by a colon for the direction | [optional] [default to &#39;&#39;]
 **filter** | [**List[str]**](str.md)| Filters to apply in the form of &#x60;key:value&#x60;.\\ Multiple filters can be applied by repeating the &#x60;filter&#x60; parameter:\\ &#x60;&amp;filter&#x3D;key1:value1&amp;filter&#x3D;key2:value2&#x60;  | [optional] [default to []]

### Return type

[**GetAccessKeysPaginatedResponseV1**](GetAccessKeysPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access keys page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_key_by_id_v1**
> AccessKeyResponseV1 update_access_key_by_id_v1(access_key_id, update_access_key_request_v1=update_access_key_request_v1)

Update Access Key

Update an access key by id.\\ \\ **Required permissions:** _customer-access-keys.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.access_key_response_v1 import AccessKeyResponseV1
from sysdig_client.models.update_access_key_request_v1 import UpdateAccessKeyRequestV1
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
    api_instance = sysdig_client.AccessKeysApi(api_client)
    access_key_id = 56 # int | The access key id.
    update_access_key_request_v1 = sysdig_client.UpdateAccessKeyRequestV1() # UpdateAccessKeyRequestV1 |  (optional)

    try:
        # Update Access Key
        api_response = api_instance.update_access_key_by_id_v1(access_key_id, update_access_key_request_v1=update_access_key_request_v1)
        print("The response of AccessKeysApi->update_access_key_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessKeysApi->update_access_key_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_id** | **int**| The access key id. | 
 **update_access_key_request_v1** | [**UpdateAccessKeyRequestV1**](UpdateAccessKeyRequestV1.md)|  | [optional] 

### Return type

[**AccessKeyResponseV1**](AccessKeyResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access key updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

