# sysdig_client.IPFilteringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_filter_v1**](IPFilteringApi.md#create_ip_filter_v1) | **POST** /platform/v1/ip-filters | Create IP Filter
[**delete_ip_filter_by_id_v1**](IPFilteringApi.md#delete_ip_filter_by_id_v1) | **DELETE** /platform/v1/ip-filters/{ipFilterId} | Delete IP Filter
[**get_ip_filter_by_id_v1**](IPFilteringApi.md#get_ip_filter_by_id_v1) | **GET** /platform/v1/ip-filters/{ipFilterId} | Get IP Filter by ID
[**get_ip_filters_settings_v1**](IPFilteringApi.md#get_ip_filters_settings_v1) | **GET** /platform/v1/ip-filters-settings | Get IP Filters Settings
[**get_ip_filters_v1**](IPFilteringApi.md#get_ip_filters_v1) | **GET** /platform/v1/ip-filters | List IP Filters
[**save_ip_filters_settings_v1**](IPFilteringApi.md#save_ip_filters_settings_v1) | **PUT** /platform/v1/ip-filters-settings | Save IP Filters settings
[**update_ip_filter_v1**](IPFilteringApi.md#update_ip_filter_v1) | **PUT** /platform/v1/ip-filters/{ipFilterId} | Update IP Filter


# **create_ip_filter_v1**
> IpFilterResponseV1 create_ip_filter_v1(create_ip_filter_v1=create_ip_filter_v1)

Create IP Filter

Create a new IP filter.\\ \\ **Required permissions:** _ip-filters.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_ip_filter_v1 import CreateIpFilterV1
from sysdig_client.models.ip_filter_response_v1 import IpFilterResponseV1
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
    api_instance = sysdig_client.IPFilteringApi(api_client)
    create_ip_filter_v1 = sysdig_client.CreateIpFilterV1() # CreateIpFilterV1 | The payload required to create IP filter. (optional)

    try:
        # Create IP Filter
        api_response = api_instance.create_ip_filter_v1(create_ip_filter_v1=create_ip_filter_v1)
        print("The response of IPFilteringApi->create_ip_filter_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->create_ip_filter_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ip_filter_v1** | [**CreateIpFilterV1**](CreateIpFilterV1.md)| The payload required to create IP filter. | [optional] 

### Return type

[**IpFilterResponseV1**](IpFilterResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IP filter created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_filter_by_id_v1**
> delete_ip_filter_by_id_v1(ip_filter_id)

Delete IP Filter

Delete IP filter by its ID.\\ \\ **Required permissions:** _ip-filters.edit_ 

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
    api_instance = sysdig_client.IPFilteringApi(api_client)
    ip_filter_id = 56 # int | IP Filter ID.

    try:
        # Delete IP Filter
        api_instance.delete_ip_filter_by_id_v1(ip_filter_id)
    except Exception as e:
        print("Exception when calling IPFilteringApi->delete_ip_filter_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filter_id** | **int**| IP Filter ID. | 

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
**204** | IP filter deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_filter_by_id_v1**
> IpFilterResponseV1 get_ip_filter_by_id_v1(ip_filter_id)

Get IP Filter by ID

Get IP Filter by ID.\\ \\ **Required permissions:** _ip-filters.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.ip_filter_response_v1 import IpFilterResponseV1
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
    api_instance = sysdig_client.IPFilteringApi(api_client)
    ip_filter_id = 56 # int | IP Filter ID.

    try:
        # Get IP Filter by ID
        api_response = api_instance.get_ip_filter_by_id_v1(ip_filter_id)
        print("The response of IPFilteringApi->get_ip_filter_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->get_ip_filter_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filter_id** | **int**| IP Filter ID. | 

### Return type

[**IpFilterResponseV1**](IpFilterResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP filter found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_filters_settings_v1**
> IpFiltersSettingsV1 get_ip_filters_settings_v1()

Get IP Filters Settings

Retrieves your IP filters settings.\\ \\ **Required permissions:** _ip-filters.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.ip_filters_settings_v1 import IpFiltersSettingsV1
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
    api_instance = sysdig_client.IPFilteringApi(api_client)

    try:
        # Get IP Filters Settings
        api_response = api_instance.get_ip_filters_settings_v1()
        print("The response of IPFilteringApi->get_ip_filters_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->get_ip_filters_settings_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IpFiltersSettingsV1**](IpFiltersSettingsV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP filters settings. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_filters_v1**
> IpFiltersPaginatedResponseV1 get_ip_filters_v1(offset=offset, limit=limit, filter=filter)

List IP Filters

Retrieve a paginated list of IP filters.\\ \\ **Required permissions:** _ip-filters.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.ip_filters_paginated_response_v1 import IpFiltersPaginatedResponseV1
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
    api_instance = sysdig_client.IPFilteringApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    filter = '' # str | The filter by field separated by a colon for the filter value (optional) (default to '')

    try:
        # List IP Filters
        api_response = api_instance.get_ip_filters_v1(offset=offset, limit=limit, filter=filter)
        print("The response of IPFilteringApi->get_ip_filters_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->get_ip_filters_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **filter** | **str**| The filter by field separated by a colon for the filter value | [optional] [default to &#39;&#39;]

### Return type

[**IpFiltersPaginatedResponseV1**](IpFiltersPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all IP filters response. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_ip_filters_settings_v1**
> IpFiltersSettingsV1 save_ip_filters_settings_v1(ip_filters_settings_v1=ip_filters_settings_v1)

Save IP Filters settings

Saves your IP filters settings.\\ \\ **Required permissions:** _ip-filters.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.ip_filters_settings_v1 import IpFiltersSettingsV1
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
    api_instance = sysdig_client.IPFilteringApi(api_client)
    ip_filters_settings_v1 = sysdig_client.IpFiltersSettingsV1() # IpFiltersSettingsV1 | The payload required to save IP filters settings. (optional)

    try:
        # Save IP Filters settings
        api_response = api_instance.save_ip_filters_settings_v1(ip_filters_settings_v1=ip_filters_settings_v1)
        print("The response of IPFilteringApi->save_ip_filters_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->save_ip_filters_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filters_settings_v1** | [**IpFiltersSettingsV1**](IpFiltersSettingsV1.md)| The payload required to save IP filters settings. | [optional] 

### Return type

[**IpFiltersSettingsV1**](IpFiltersSettingsV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP filters settings saved. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_filter_v1**
> IpFilterResponseV1 update_ip_filter_v1(ip_filter_id, update_ip_filter_v1)

Update IP Filter

Update IP filter by its ID. \\ \\ **Required permissions:** _ip-filters.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.ip_filter_response_v1 import IpFilterResponseV1
from sysdig_client.models.update_ip_filter_v1 import UpdateIpFilterV1
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
    api_instance = sysdig_client.IPFilteringApi(api_client)
    ip_filter_id = 56 # int | IP Filter ID.
    update_ip_filter_v1 = sysdig_client.UpdateIpFilterV1() # UpdateIpFilterV1 | 

    try:
        # Update IP Filter
        api_response = api_instance.update_ip_filter_v1(ip_filter_id, update_ip_filter_v1)
        print("The response of IPFilteringApi->update_ip_filter_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->update_ip_filter_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filter_id** | **int**| IP Filter ID. | 
 **update_ip_filter_v1** | [**UpdateIpFilterV1**](UpdateIpFilterV1.md)|  | 

### Return type

[**IpFilterResponseV1**](IpFilterResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP filter updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

