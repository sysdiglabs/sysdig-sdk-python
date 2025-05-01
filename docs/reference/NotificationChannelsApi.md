# sysdig_client.NotificationChannelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel**](NotificationChannelsApi.md#create_notification_channel) | **POST** /platform/v1/notification-channels | Create Notification Channel
[**delete_notification_channel_by_id**](NotificationChannelsApi.md#delete_notification_channel_by_id) | **DELETE** /platform/v1/notification-channels/{notificationChannelId} | Delete Notification Channel
[**get_notification_channel_by_id**](NotificationChannelsApi.md#get_notification_channel_by_id) | **GET** /platform/v1/notification-channels/{notificationChannelId} | Get Notification Channel
[**get_notification_channels**](NotificationChannelsApi.md#get_notification_channels) | **GET** /platform/v1/notification-channels | List Notification Channels
[**update_notification_channel_by_id**](NotificationChannelsApi.md#update_notification_channel_by_id) | **PUT** /platform/v1/notification-channels/{notificationChannelId} | Update Notification Channel


# **create_notification_channel**
> NotificationChannelResponseV1 create_notification_channel(create_notification_channel_request_v1)

Create Notification Channel

Create a notification channel.\\ \\ **Required permissions:** _notification-channels.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_notification_channel_request_v1 import CreateNotificationChannelRequestV1
from sysdig_client.models.notification_channel_response_v1 import NotificationChannelResponseV1
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
    api_instance = sysdig_client.NotificationChannelsApi(api_client)
    create_notification_channel_request_v1 = sysdig_client.CreateNotificationChannelRequestV1() # CreateNotificationChannelRequestV1 | The payload required to create a notification channel

    try:
        # Create Notification Channel
        api_response = api_instance.create_notification_channel(create_notification_channel_request_v1)
        print("The response of NotificationChannelsApi->create_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelsApi->create_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_notification_channel_request_v1** | [**CreateNotificationChannelRequestV1**](CreateNotificationChannelRequestV1.md)| The payload required to create a notification channel | 

### Return type

[**NotificationChannelResponseV1**](NotificationChannelResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notification Channel created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel_by_id**
> delete_notification_channel_by_id(notification_channel_id)

Delete Notification Channel

Delete a notification channel by its ID.\\ \\ **Required permissions:** _notification-channels.edit_ 

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
    api_instance = sysdig_client.NotificationChannelsApi(api_client)
    notification_channel_id = 56 # int | The Notification Channel Identifier

    try:
        # Delete Notification Channel
        api_instance.delete_notification_channel_by_id(notification_channel_id)
    except Exception as e:
        print("Exception when calling NotificationChannelsApi->delete_notification_channel_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**| The Notification Channel Identifier | 

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
**204** | Notification Channel deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_channel_by_id**
> NotificationChannelResponseV1 get_notification_channel_by_id(notification_channel_id)

Get Notification Channel

Returns a specific notification channel by its ID.\\ \\ **Required permissions:** _notification-channels.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.notification_channel_response_v1 import NotificationChannelResponseV1
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
    api_instance = sysdig_client.NotificationChannelsApi(api_client)
    notification_channel_id = 56 # int | The Notification Channel Identifier

    try:
        # Get Notification Channel
        api_response = api_instance.get_notification_channel_by_id(notification_channel_id)
        print("The response of NotificationChannelsApi->get_notification_channel_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelsApi->get_notification_channel_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**| The Notification Channel Identifier | 

### Return type

[**NotificationChannelResponseV1**](NotificationChannelResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification Channel found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_channels**
> GetNotificationChannelsPaginatedResponseV1 get_notification_channels(offset=offset, limit=limit)

List Notification Channels

Retrieve a paginated list of notification channels.\\ \\ **Required permissions:** _notification-channels.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_notification_channels_paginated_response_v1 import GetNotificationChannelsPaginatedResponseV1
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
    api_instance = sysdig_client.NotificationChannelsApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)

    try:
        # List Notification Channels
        api_response = api_instance.get_notification_channels(offset=offset, limit=limit)
        print("The response of NotificationChannelsApi->get_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelsApi->get_notification_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]

### Return type

[**GetNotificationChannelsPaginatedResponseV1**](GetNotificationChannelsPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of notification channels. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_channel_by_id**
> NotificationChannelResponseV1 update_notification_channel_by_id(notification_channel_id, update_notification_channel_request_v1)

Update Notification Channel

Update a notification channel by its ID.\\ \\ **Required permissions:** _notification-channels.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.notification_channel_response_v1 import NotificationChannelResponseV1
from sysdig_client.models.update_notification_channel_request_v1 import UpdateNotificationChannelRequestV1
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
    api_instance = sysdig_client.NotificationChannelsApi(api_client)
    notification_channel_id = 56 # int | The Notification Channel Identifier
    update_notification_channel_request_v1 = sysdig_client.UpdateNotificationChannelRequestV1() # UpdateNotificationChannelRequestV1 | The payload required to update the notification channel

    try:
        # Update Notification Channel
        api_response = api_instance.update_notification_channel_by_id(notification_channel_id, update_notification_channel_request_v1)
        print("The response of NotificationChannelsApi->update_notification_channel_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelsApi->update_notification_channel_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**| The Notification Channel Identifier | 
 **update_notification_channel_request_v1** | [**UpdateNotificationChannelRequestV1**](UpdateNotificationChannelRequestV1.md)| The payload required to update the notification channel | 

### Return type

[**NotificationChannelResponseV1**](NotificationChannelResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification channel updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

