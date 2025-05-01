# sysdig_client.GroupMappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_mapping_v1**](GroupMappingsApi.md#create_group_mapping_v1) | **POST** /platform/v1/group-mappings | Create Group Mapping
[**delete_group_mapping_by_id_v1**](GroupMappingsApi.md#delete_group_mapping_by_id_v1) | **DELETE** /platform/v1/group-mappings/{groupMappingId} | Delete Group Mapping
[**get_group_mapping_by_id_v1**](GroupMappingsApi.md#get_group_mapping_by_id_v1) | **GET** /platform/v1/group-mappings/{groupMappingId} | Get Group Mapping
[**get_group_mapping_settings_v1**](GroupMappingsApi.md#get_group_mapping_settings_v1) | **GET** /platform/v1/group-mappings-settings | Get Group Mappings Settings
[**get_group_mappings_v1**](GroupMappingsApi.md#get_group_mappings_v1) | **GET** /platform/v1/group-mappings | List Group Mappings
[**save_group_mapping_settings_v1**](GroupMappingsApi.md#save_group_mapping_settings_v1) | **PUT** /platform/v1/group-mappings-settings | Save Group Mapping settings
[**update_group_mapping_by_id_v1**](GroupMappingsApi.md#update_group_mapping_by_id_v1) | **PUT** /platform/v1/group-mappings/{groupMappingId} | Update Group Mapping


# **create_group_mapping_v1**
> GroupMappingResponseV1 create_group_mapping_v1(create_group_mapping_request_v1=create_group_mapping_request_v1)

Create Group Mapping

Create a new group mapping.\\ \\ **Required permissions:** _group-mappings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_group_mapping_request_v1 import CreateGroupMappingRequestV1
from sysdig_client.models.group_mapping_response_v1 import GroupMappingResponseV1
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
    api_instance = sysdig_client.GroupMappingsApi(api_client)
    create_group_mapping_request_v1 = sysdig_client.CreateGroupMappingRequestV1() # CreateGroupMappingRequestV1 | The payload required to create group mapping. (optional)

    try:
        # Create Group Mapping
        api_response = api_instance.create_group_mapping_v1(create_group_mapping_request_v1=create_group_mapping_request_v1)
        print("The response of GroupMappingsApi->create_group_mapping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMappingsApi->create_group_mapping_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_mapping_request_v1** | [**CreateGroupMappingRequestV1**](CreateGroupMappingRequestV1.md)| The payload required to create group mapping. | [optional] 

### Return type

[**GroupMappingResponseV1**](GroupMappingResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Group Mapping created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_mapping_by_id_v1**
> delete_group_mapping_by_id_v1(group_mapping_id)

Delete Group Mapping

Delete a group mapping by its ID.\\ \\ **Required permissions:** _group-mappings.edit_ 

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
    api_instance = sysdig_client.GroupMappingsApi(api_client)
    group_mapping_id = 56 # int | The group mapping ID.

    try:
        # Delete Group Mapping
        api_instance.delete_group_mapping_by_id_v1(group_mapping_id)
    except Exception as e:
        print("Exception when calling GroupMappingsApi->delete_group_mapping_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_mapping_id** | **int**| The group mapping ID. | 

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
**204** | Group mapping deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_mapping_by_id_v1**
> GroupMappingResponseV1 get_group_mapping_by_id_v1(group_mapping_id)

Get Group Mapping

Return a group mapping by its ID.\\ \\ **Required permissions:** _group-mappings.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.group_mapping_response_v1 import GroupMappingResponseV1
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
    api_instance = sysdig_client.GroupMappingsApi(api_client)
    group_mapping_id = 56 # int | The group mapping ID.

    try:
        # Get Group Mapping
        api_response = api_instance.get_group_mapping_by_id_v1(group_mapping_id)
        print("The response of GroupMappingsApi->get_group_mapping_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMappingsApi->get_group_mapping_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_mapping_id** | **int**| The group mapping ID. | 

### Return type

[**GroupMappingResponseV1**](GroupMappingResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group Mapping found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_mapping_settings_v1**
> GroupMappingSettingsV1 get_group_mapping_settings_v1()

Get Group Mappings Settings

Retrieves your group mapping settings.\\ \\ **Required permissions:** _group-mappings.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.group_mapping_settings_v1 import GroupMappingSettingsV1
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
    api_instance = sysdig_client.GroupMappingsApi(api_client)

    try:
        # Get Group Mappings Settings
        api_response = api_instance.get_group_mapping_settings_v1()
        print("The response of GroupMappingsApi->get_group_mapping_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMappingsApi->get_group_mapping_settings_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GroupMappingSettingsV1**](GroupMappingSettingsV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group mappings page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_mappings_v1**
> GroupMappingsPaginatedResponseV1 get_group_mappings_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)

List Group Mappings

Retrieve a paginated list of group mappings.\\ \\ **Required permissions:** _group-mappings.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.group_mappings_paginated_response_v1 import GroupMappingsPaginatedResponseV1
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
    api_instance = sysdig_client.GroupMappingsApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    orderby = '' # str | The order by field separated by a colon for the direction (optional) (default to '')
    filter = '' # str | The filter by field separated by a colon for the filter value (optional) (default to '')

    try:
        # List Group Mappings
        api_response = api_instance.get_group_mappings_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)
        print("The response of GroupMappingsApi->get_group_mappings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMappingsApi->get_group_mappings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **orderby** | **str**| The order by field separated by a colon for the direction | [optional] [default to &#39;&#39;]
 **filter** | **str**| The filter by field separated by a colon for the filter value | [optional] [default to &#39;&#39;]

### Return type

[**GroupMappingsPaginatedResponseV1**](GroupMappingsPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group mappings paginated response. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_group_mapping_settings_v1**
> GroupMappingSettingsV1 save_group_mapping_settings_v1(group_mapping_settings_v1=group_mapping_settings_v1)

Save Group Mapping settings

Saves your group mapping settings.\\ \\ **Required permissions:** _group-mappings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.group_mapping_settings_v1 import GroupMappingSettingsV1
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
    api_instance = sysdig_client.GroupMappingsApi(api_client)
    group_mapping_settings_v1 = sysdig_client.GroupMappingSettingsV1() # GroupMappingSettingsV1 | The payload required to save group mapping settings. (optional)

    try:
        # Save Group Mapping settings
        api_response = api_instance.save_group_mapping_settings_v1(group_mapping_settings_v1=group_mapping_settings_v1)
        print("The response of GroupMappingsApi->save_group_mapping_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMappingsApi->save_group_mapping_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_mapping_settings_v1** | [**GroupMappingSettingsV1**](GroupMappingSettingsV1.md)| The payload required to save group mapping settings. | [optional] 

### Return type

[**GroupMappingSettingsV1**](GroupMappingSettingsV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group Mapping settings saved. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_mapping_by_id_v1**
> GroupMappingResponseV1 update_group_mapping_by_id_v1(group_mapping_id, update_group_mapping_request_v1=update_group_mapping_request_v1)

Update Group Mapping

Update a group mapping by its ID.\\ \\ **Required permissions:** _group-mappings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.group_mapping_response_v1 import GroupMappingResponseV1
from sysdig_client.models.update_group_mapping_request_v1 import UpdateGroupMappingRequestV1
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
    api_instance = sysdig_client.GroupMappingsApi(api_client)
    group_mapping_id = 56 # int | The group mapping ID.
    update_group_mapping_request_v1 = sysdig_client.UpdateGroupMappingRequestV1() # UpdateGroupMappingRequestV1 |  (optional)

    try:
        # Update Group Mapping
        api_response = api_instance.update_group_mapping_by_id_v1(group_mapping_id, update_group_mapping_request_v1=update_group_mapping_request_v1)
        print("The response of GroupMappingsApi->update_group_mapping_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupMappingsApi->update_group_mapping_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_mapping_id** | **int**| The group mapping ID. | 
 **update_group_mapping_request_v1** | [**UpdateGroupMappingRequestV1**](UpdateGroupMappingRequestV1.md)|  | [optional] 

### Return type

[**GroupMappingResponseV1**](GroupMappingResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group Mapping updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

