# sysdig_client.MonitorEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_monitor_events_v1**](MonitorEventsApi.md#get_monitor_events_v1) | **GET** /monitor/events/v1/events | Get Events


# **get_monitor_events_v1**
> ListMonitorEventsResponse get_monitor_events_v1(var_from=var_from, to=to, cursor=cursor, filter=filter, limit=limit)

Get Events

Retrieves the list of events matching the expressed search criteria.
The pair `from` and `to` and the `cursor` parameter are mutually exclusive. If you supply a `from` and `to` you must not supply a `cursor` and vice-versa.
The time criteria is required and can be specified in two different ways:
- Using `from` and `to`, the list of events within the timeframe (max 2 weeks) will be returned, starting from the most recent ones.
- Using a `cursor` the events returned will be in the before or after the event, depending on the cursor type. More details are available in the `cursor` attribute in the response.\
\
**Required permissions:**
- _alert-events.read_ for alert events to be included in the response
- _custom-events.read_ for custom events to be included in the response


### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.list_monitor_events_response import ListMonitorEventsResponse
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
    api_instance = sysdig_client.MonitorEventsApi(api_client)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    limit = 25 # int | The number of items to return (optional) (default to 25)

    try:
        # Get Events
        api_response = api_instance.get_monitor_events_v1(var_from=var_from, to=to, cursor=cursor, filter=filter, limit=limit)
        print("The response of MonitorEventsApi->get_monitor_events_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorEventsApi->get_monitor_events_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional]
 **to** | **int**|  | [optional]
 **cursor** | **str**|  | [optional]
 **filter** | **str**|  | [optional]
 **limit** | **int**| The number of items to return | [optional] [default to 25]

### Return type

[**ListMonitorEventsResponse**](ListMonitorEventsResponse.md)

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

