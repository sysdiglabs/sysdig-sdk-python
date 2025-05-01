# sysdig_client.ServiceAccountsNotificationSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#create_global_service_accounts_notification_settings_v1) | **POST** /platform/v1/service-accounts/notification-settings | Create Global Service Accounts Notification Settings
[**create_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#create_service_accounts_notification_settings_v1) | **POST** /platform/v1/teams/{teamId}/service-accounts/notification-settings | Create Service Accounts Notification Settings
[**delete_global_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#delete_global_service_accounts_notification_settings_v1) | **DELETE** /platform/v1/service-accounts/notification-settings | Delete Global Service Accounts Notification Settings
[**delete_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#delete_service_accounts_notification_settings_v1) | **DELETE** /platform/v1/teams/{teamId}/service-accounts/notification-settings | Delete Service Accounts Notification Settings
[**get_global_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#get_global_service_accounts_notification_settings_v1) | **GET** /platform/v1/service-accounts/notification-settings | Get Global Service Accounts Notification Settings
[**get_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#get_service_accounts_notification_settings_v1) | **GET** /platform/v1/teams/{teamId}/service-accounts/notification-settings | Get Service Accounts Notification Settings
[**update_global_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#update_global_service_accounts_notification_settings_v1) | **PUT** /platform/v1/service-accounts/notification-settings | Update Global Service Accounts Notification Settings
[**update_service_accounts_notification_settings_v1**](ServiceAccountsNotificationSettingsApi.md#update_service_accounts_notification_settings_v1) | **PUT** /platform/v1/teams/{teamId}/service-accounts/notification-settings | Update Service Accounts Notification Settings


# **create_global_service_accounts_notification_settings_v1**
> ServiceAccountsNotificationSettingsResponseV1 create_global_service_accounts_notification_settings_v1(create_service_accounts_notification_settings_request_v1=create_service_accounts_notification_settings_request_v1)

Create Global Service Accounts Notification Settings

Create a new Notification Settings for Global Service Accounts.\\ \\ **Required permissions:** _global-service-accounts-notification-settings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_service_accounts_notification_settings_request_v1 import CreateServiceAccountsNotificationSettingsRequestV1
from sysdig_client.models.service_accounts_notification_settings_response_v1 import ServiceAccountsNotificationSettingsResponseV1
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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)
    create_service_accounts_notification_settings_request_v1 = sysdig_client.CreateServiceAccountsNotificationSettingsRequestV1() # CreateServiceAccountsNotificationSettingsRequestV1 | The payload required to create Service Accounts Notification Settings. (optional)

    try:
        # Create Global Service Accounts Notification Settings
        api_response = api_instance.create_global_service_accounts_notification_settings_v1(create_service_accounts_notification_settings_request_v1=create_service_accounts_notification_settings_request_v1)
        print("The response of ServiceAccountsNotificationSettingsApi->create_global_service_accounts_notification_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->create_global_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_service_accounts_notification_settings_request_v1** | [**CreateServiceAccountsNotificationSettingsRequestV1**](CreateServiceAccountsNotificationSettingsRequestV1.md)| The payload required to create Service Accounts Notification Settings. | [optional] 

### Return type

[**ServiceAccountsNotificationSettingsResponseV1**](ServiceAccountsNotificationSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Service Accounts Notification Settings created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_accounts_notification_settings_v1**
> ServiceAccountsNotificationSettingsResponseV1 create_service_accounts_notification_settings_v1(team_id, create_service_accounts_notification_settings_request_v1=create_service_accounts_notification_settings_request_v1)

Create Service Accounts Notification Settings

Create a new Notification Settings for Service Accounts which belong to a specific team.\\ \\ **Required permissions:** _service-accounts-notification-settings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_service_accounts_notification_settings_request_v1 import CreateServiceAccountsNotificationSettingsRequestV1
from sysdig_client.models.service_accounts_notification_settings_response_v1 import ServiceAccountsNotificationSettingsResponseV1
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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)
    team_id = 56 # int | The team ID.
    create_service_accounts_notification_settings_request_v1 = sysdig_client.CreateServiceAccountsNotificationSettingsRequestV1() # CreateServiceAccountsNotificationSettingsRequestV1 | The payload required to create Service Accounts Notification Settings. (optional)

    try:
        # Create Service Accounts Notification Settings
        api_response = api_instance.create_service_accounts_notification_settings_v1(team_id, create_service_accounts_notification_settings_request_v1=create_service_accounts_notification_settings_request_v1)
        print("The response of ServiceAccountsNotificationSettingsApi->create_service_accounts_notification_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->create_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **create_service_accounts_notification_settings_request_v1** | [**CreateServiceAccountsNotificationSettingsRequestV1**](CreateServiceAccountsNotificationSettingsRequestV1.md)| The payload required to create Service Accounts Notification Settings. | [optional] 

### Return type

[**ServiceAccountsNotificationSettingsResponseV1**](ServiceAccountsNotificationSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Service Accounts Notification Settings created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_service_accounts_notification_settings_v1**
> delete_global_service_accounts_notification_settings_v1()

Delete Global Service Accounts Notification Settings

Delete Notification Settings for Global Service Accounts.\\ \\ **Required permissions:** _global-service-accounts-notification-settings.edit_ 

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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)

    try:
        # Delete Global Service Accounts Notification Settings
        api_instance.delete_global_service_accounts_notification_settings_v1()
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->delete_global_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Service Accounts Notification Settings deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_accounts_notification_settings_v1**
> delete_service_accounts_notification_settings_v1(team_id)

Delete Service Accounts Notification Settings

Delete Service Accounts Notification Settings for a given team.\\ \\ **Required permissions:** _service-accounts-notification-settings.edit_ 

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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)
    team_id = 56 # int | The team ID.

    try:
        # Delete Service Accounts Notification Settings
        api_instance.delete_service_accounts_notification_settings_v1(team_id)
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->delete_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 

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
**204** | Service Accounts Notification Settings deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_service_accounts_notification_settings_v1**
> ServiceAccountsNotificationSettingsResponseV1 get_global_service_accounts_notification_settings_v1()

Get Global Service Accounts Notification Settings

Return Notification Settings for Global Service Accounts.\\ \\ **Required permissions:** _global-service-accounts-notification-settings.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.service_accounts_notification_settings_response_v1 import ServiceAccountsNotificationSettingsResponseV1
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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)

    try:
        # Get Global Service Accounts Notification Settings
        api_response = api_instance.get_global_service_accounts_notification_settings_v1()
        print("The response of ServiceAccountsNotificationSettingsApi->get_global_service_accounts_notification_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->get_global_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceAccountsNotificationSettingsResponseV1**](ServiceAccountsNotificationSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service Accounts Notification Settings found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_accounts_notification_settings_v1**
> ServiceAccountsNotificationSettingsResponseV1 get_service_accounts_notification_settings_v1(team_id)

Get Service Accounts Notification Settings

Return Service Accounts Notification Settings for a given team.\\ \\ **Required permissions:** _service-accounts-notification-settings.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.service_accounts_notification_settings_response_v1 import ServiceAccountsNotificationSettingsResponseV1
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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)
    team_id = 56 # int | The team ID.

    try:
        # Get Service Accounts Notification Settings
        api_response = api_instance.get_service_accounts_notification_settings_v1(team_id)
        print("The response of ServiceAccountsNotificationSettingsApi->get_service_accounts_notification_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->get_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 

### Return type

[**ServiceAccountsNotificationSettingsResponseV1**](ServiceAccountsNotificationSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service Accounts Notification Settings found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_service_accounts_notification_settings_v1**
> ServiceAccountsNotificationSettingsResponseV1 update_global_service_accounts_notification_settings_v1(update_service_accounts_notification_settings_request_v1=update_service_accounts_notification_settings_request_v1)

Update Global Service Accounts Notification Settings

Update Notification Settings for Global Service Accounts.\\ \\ **Required permissions:** _global-service-accounts-notification-settings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.service_accounts_notification_settings_response_v1 import ServiceAccountsNotificationSettingsResponseV1
from sysdig_client.models.update_service_accounts_notification_settings_request_v1 import UpdateServiceAccountsNotificationSettingsRequestV1
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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)
    update_service_accounts_notification_settings_request_v1 = sysdig_client.UpdateServiceAccountsNotificationSettingsRequestV1() # UpdateServiceAccountsNotificationSettingsRequestV1 |  (optional)

    try:
        # Update Global Service Accounts Notification Settings
        api_response = api_instance.update_global_service_accounts_notification_settings_v1(update_service_accounts_notification_settings_request_v1=update_service_accounts_notification_settings_request_v1)
        print("The response of ServiceAccountsNotificationSettingsApi->update_global_service_accounts_notification_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->update_global_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_service_accounts_notification_settings_request_v1** | [**UpdateServiceAccountsNotificationSettingsRequestV1**](UpdateServiceAccountsNotificationSettingsRequestV1.md)|  | [optional] 

### Return type

[**ServiceAccountsNotificationSettingsResponseV1**](ServiceAccountsNotificationSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service Accounts Notification Settings updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_accounts_notification_settings_v1**
> ServiceAccountsNotificationSettingsResponseV1 update_service_accounts_notification_settings_v1(team_id, update_service_accounts_notification_settings_request_v1=update_service_accounts_notification_settings_request_v1)

Update Service Accounts Notification Settings

Update Service Accounts Notification Settings for a given team.\\ \\ **Required permissions:** _service-accounts-notification-settings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.service_accounts_notification_settings_response_v1 import ServiceAccountsNotificationSettingsResponseV1
from sysdig_client.models.update_service_accounts_notification_settings_request_v1 import UpdateServiceAccountsNotificationSettingsRequestV1
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
    api_instance = sysdig_client.ServiceAccountsNotificationSettingsApi(api_client)
    team_id = 56 # int | The team ID.
    update_service_accounts_notification_settings_request_v1 = sysdig_client.UpdateServiceAccountsNotificationSettingsRequestV1() # UpdateServiceAccountsNotificationSettingsRequestV1 |  (optional)

    try:
        # Update Service Accounts Notification Settings
        api_response = api_instance.update_service_accounts_notification_settings_v1(team_id, update_service_accounts_notification_settings_request_v1=update_service_accounts_notification_settings_request_v1)
        print("The response of ServiceAccountsNotificationSettingsApi->update_service_accounts_notification_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsNotificationSettingsApi->update_service_accounts_notification_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **update_service_accounts_notification_settings_request_v1** | [**UpdateServiceAccountsNotificationSettingsRequestV1**](UpdateServiceAccountsNotificationSettingsRequestV1.md)|  | [optional] 

### Return type

[**ServiceAccountsNotificationSettingsResponseV1**](ServiceAccountsNotificationSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service Accounts Notification Settings updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

