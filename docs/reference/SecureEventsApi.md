# sysdig_client.SecureEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_v1**](SecureEventsApi.md#get_event_v1) | **GET** /secure/events/v1/events/{eventId} | Get event
[**get_events_supported_filters_v1**](SecureEventsApi.md#get_events_supported_filters_v1) | **GET** /secure/events/v1/supported-filters | Get available filters
[**get_events_v1**](SecureEventsApi.md#get_events_v1) | **GET** /secure/events/v1/events | List events


# **get_event_v1**
> Event get_event_v1(event_id)

Get event

Retrieves an event given its id. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.event import Event
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
    api_instance = sysdig_client.SecureEventsApi(api_client)
    event_id = '179854fbe16a1279f2ebeb558f1ebe99' # str | The event id.

    try:
        # Get event
        api_response = api_instance.get_event_v1(event_id)
        print("The response of SecureEventsApi->get_event_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureEventsApi->get_event_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| The event id. | 

### Return type

[**Event**](Event.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The secure event. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Bad request |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_supported_filters_v1**
> SupportedFiltersResponse get_events_supported_filters_v1()

Get available filters

Events can be filtered by a set of attributes. This endpoint returns the list of those for which filtering is supported. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.supported_filters_response import SupportedFiltersResponse
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
    api_instance = sysdig_client.SecureEventsApi(api_client)

    try:
        # Get available filters
        api_response = api_instance.get_events_supported_filters_v1()
        print("The response of SecureEventsApi->get_events_supported_filters_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureEventsApi->get_events_supported_filters_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SupportedFiltersResponse**](SupportedFiltersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of supported attributes for filtering events. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Bad request |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_v1**
> ListEventsResponse get_events_v1(var_from=var_from, to=to, cursor=cursor, zones=zones, filter=filter, limit=limit)

List events

Retrieves the list of events matching the expressed search criteria. The pair `from` and `to` and the `cursor` parameter are mutually exclusive. If you supply a `from` and `to` you must not supply a `cursor` and vice-versa. The time criteria is required and can be specified in two different ways: - Using `from` and `to`, the list of events within the timeframe (max 2 weeks) will be returned, starting from the most recent ones. - Using a `cursor` the events returned will be in the before, after or around the event, depending on the event the cursor is taken from and the cursor type. More details are available in the `cursor` attribute in the response.  The event content can be filtered using `zones`, to select one or more zones, or with the filter, directly expressing a condition on fields and labels. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.list_events_response import ListEventsResponse
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
    api_instance = sysdig_client.SecureEventsApi(api_client)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    zones = [56] # List[int] |  (optional)
    filter = 'filter_example' # str |  (optional)
    limit = 25 # int |  (optional) (default to 25)

    try:
        # List events
        api_response = api_instance.get_events_v1(var_from=var_from, to=to, cursor=cursor, zones=zones, filter=filter, limit=limit)
        print("The response of SecureEventsApi->get_events_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureEventsApi->get_events_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **zones** | [**List[int]**](int.md)|  | [optional] 
 **filter** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 25]

### Return type

[**ListEventsResponse**](ListEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of events. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Bad request |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

