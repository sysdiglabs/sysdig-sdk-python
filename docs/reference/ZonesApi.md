# sysdig_client.ZonesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zone_v1**](ZonesApi.md#create_zone_v1) | **POST** /platform/v1/zones | Create Zone
[**delete_zone_v1**](ZonesApi.md#delete_zone_v1) | **DELETE** /platform/v1/zones/{zoneId} | Delete Zone
[**edit_zone_v1**](ZonesApi.md#edit_zone_v1) | **PUT** /platform/v1/zones/{zoneId} | Update Zone
[**get_zone_by_id_v1**](ZonesApi.md#get_zone_by_id_v1) | **GET** /platform/v1/zones/{zoneId} | Get Zone
[**list_zones_v1**](ZonesApi.md#list_zones_v1) | **GET** /platform/v1/zones | List Zones


# **create_zone_v1**
> ZoneResponseV1 create_zone_v1(create_zone_request_v1)

Create Zone

Create a new Zone.\\ \\ **Required permissions:** zones.edit 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_zone_request_v1 import CreateZoneRequestV1
from sysdig_client.models.zone_response_v1 import ZoneResponseV1
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
    api_instance = sysdig_client.ZonesApi(api_client)
    create_zone_request_v1 = sysdig_client.CreateZoneRequestV1() # CreateZoneRequestV1 | Request body for creating a new Zone

    try:
        # Create Zone
        api_response = api_instance.create_zone_v1(create_zone_request_v1)
        print("The response of ZonesApi->create_zone_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->create_zone_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_zone_request_v1** | [**CreateZoneRequestV1**](CreateZoneRequestV1.md)| Request body for creating a new Zone | 

### Return type

[**ZoneResponseV1**](ZoneResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Single Zone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone_v1**
> delete_zone_v1(zone_id)

Delete Zone

Delete a Zone by its ID.\\ \\ **Required permissions:** zones.edit 

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
    api_instance = sysdig_client.ZonesApi(api_client)
    zone_id = 56 # int | 

    try:
        # Delete Zone
        api_instance.delete_zone_v1(zone_id)
    except Exception as e:
        print("Exception when calling ZonesApi->delete_zone_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**|  | 

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
**204** | Zone successfully deleted |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_zone_v1**
> ZoneResponseV1 edit_zone_v1(zone_id, create_zone_request_v1)

Update Zone

Update an existing Zone by its ID.\\ \\ **Required permissions:** zones.edit 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_zone_request_v1 import CreateZoneRequestV1
from sysdig_client.models.zone_response_v1 import ZoneResponseV1
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
    api_instance = sysdig_client.ZonesApi(api_client)
    zone_id = 56 # int | 
    create_zone_request_v1 = sysdig_client.CreateZoneRequestV1() # CreateZoneRequestV1 | Request body for editing an existing zone

    try:
        # Update Zone
        api_response = api_instance.edit_zone_v1(zone_id, create_zone_request_v1)
        print("The response of ZonesApi->edit_zone_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->edit_zone_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**|  | 
 **create_zone_request_v1** | [**CreateZoneRequestV1**](CreateZoneRequestV1.md)| Request body for editing an existing zone | 

### Return type

[**ZoneResponseV1**](ZoneResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Single Zone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_by_id_v1**
> ZoneResponseV1 get_zone_by_id_v1(zone_id)

Get Zone

Retrieve a single Zone by ID.\\ \\ **Required permissions:** zones.read 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.zone_response_v1 import ZoneResponseV1
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
    api_instance = sysdig_client.ZonesApi(api_client)
    zone_id = 56 # int | 

    try:
        # Get Zone
        api_response = api_instance.get_zone_by_id_v1(zone_id)
        print("The response of ZonesApi->get_zone_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->get_zone_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**|  | 

### Return type

[**ZoneResponseV1**](ZoneResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Single Zone |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zones_v1**
> ListZonesResponseV1 list_zones_v1(filter=filter, limit=limit, offset=offset, orderby=orderby)

List Zones

Retrieve a paginated list of Zones.\\ \\ **Required permissions:** zones.read or teams.edit 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.list_zones_response_v1 import ListZonesResponseV1
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
    api_instance = sysdig_client.ZonesApi(api_client)
    filter = [] # List[str] | Filters to apply in the form of `key:value`.\\ Multiple filters can be applied by repeating the `filter` parameter:\\ `&filter=key1:value1&filter=key2:value2`  (optional) (default to [])
    limit = 25 # int | The number of items to return (optional) (default to 25)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    orderby = ["id:desc"] # List[str] | Ordering to apply in the form of `field:direction` where `direction` can either be `asc` or `desc`.\\ Multiple orderings can be applied by repeating the `orderby` parameter:\\ `&orderby=key1:direction1&orderby=key2:direction2`  (optional) (default to ["id:desc"])

    try:
        # List Zones
        api_response = api_instance.list_zones_v1(filter=filter, limit=limit, offset=offset, orderby=orderby)
        print("The response of ZonesApi->list_zones_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->list_zones_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**List[str]**](str.md)| Filters to apply in the form of &#x60;key:value&#x60;.\\ Multiple filters can be applied by repeating the &#x60;filter&#x60; parameter:\\ &#x60;&amp;filter&#x3D;key1:value1&amp;filter&#x3D;key2:value2&#x60;  | [optional] [default to []]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **orderby** | [**List[str]**](str.md)| Ordering to apply in the form of &#x60;field:direction&#x60; where &#x60;direction&#x60; can either be &#x60;asc&#x60; or &#x60;desc&#x60;.\\ Multiple orderings can be applied by repeating the &#x60;orderby&#x60; parameter:\\ &#x60;&amp;orderby&#x3D;key1:direction1&amp;orderby&#x3D;key2:direction2&#x60;  | [optional] [default to [&quot;id:desc&quot;]]

### Return type

[**ListZonesResponseV1**](ListZonesResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Zones |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

