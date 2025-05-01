# sysdig_client.EventsForwarderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_efo_inegration_v1**](EventsForwarderApi.md#create_efo_inegration_v1) | **POST** /secure/events-forwarder/v1/integrations | Create Integration
[**delete_efo_integration_by_idv1**](EventsForwarderApi.md#delete_efo_integration_by_idv1) | **DELETE** /secure/events-forwarder/v1/integrations/{integrationId} | Delete Integration
[**get_efo_integration_by_id_v1**](EventsForwarderApi.md#get_efo_integration_by_id_v1) | **GET** /secure/events-forwarder/v1/integrations/{integrationId} | Get Integration
[**list_efo_channels_by_integration_v1**](EventsForwarderApi.md#list_efo_channels_by_integration_v1) | **GET** /secure/events-forwarder/v1/channels | List Channels
[**list_efo_integrations_types_v1**](EventsForwarderApi.md#list_efo_integrations_types_v1) | **GET** /secure/events-forwarder/v1/types | List Integrations types
[**list_efo_integrations_v1**](EventsForwarderApi.md#list_efo_integrations_v1) | **GET** /secure/events-forwarder/v1/integrations | List Integrations
[**update_efo_integration_by_id_v1**](EventsForwarderApi.md#update_efo_integration_by_id_v1) | **PUT** /secure/events-forwarder/v1/integrations/{integrationId} | Update Integration


# **create_efo_inegration_v1**
> IntegrationResponse create_efo_inegration_v1(create_integration_request)

Create Integration

Configures a new integration to forward a data type to a destination, given the specified connection parameters

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_integration_request import CreateIntegrationRequest
from sysdig_client.models.integration_response import IntegrationResponse
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
    api_instance = sysdig_client.EventsForwarderApi(api_client)
    create_integration_request = sysdig_client.CreateIntegrationRequest() # CreateIntegrationRequest | Configuration for the new integration

    try:
        # Create Integration
        api_response = api_instance.create_efo_inegration_v1(create_integration_request)
        print("The response of EventsForwarderApi->create_efo_inegration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsForwarderApi->create_efo_inegration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_integration_request** | [**CreateIntegrationRequest**](CreateIntegrationRequest.md)| Configuration for the new integration | 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Integration created successfully |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_efo_integration_by_idv1**
> delete_efo_integration_by_idv1(integration_id)

Delete Integration

Delete an integration

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
    api_instance = sysdig_client.EventsForwarderApi(api_client)
    integration_id = 56 # int | ID of the integration to return

    try:
        # Delete Integration
        api_instance.delete_efo_integration_by_idv1(integration_id)
    except Exception as e:
        print("Exception when calling EventsForwarderApi->delete_efo_integration_by_idv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| ID of the integration to return | 

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
**204** | Integration deleted successfully |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Integration not found |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_efo_integration_by_id_v1**
> IntegrationResponse get_efo_integration_by_id_v1(integration_id)

Get Integration

Returns the configuration for an integration

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.integration_response import IntegrationResponse
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
    api_instance = sysdig_client.EventsForwarderApi(api_client)
    integration_id = 56 # int | ID of the integration to return

    try:
        # Get Integration
        api_response = api_instance.get_efo_integration_by_id_v1(integration_id)
        print("The response of EventsForwarderApi->get_efo_integration_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsForwarderApi->get_efo_integration_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| ID of the integration to return | 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An integration is returned |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Integration not found with the specified ID |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_efo_channels_by_integration_v1**
> IntegrationChannelsResponse list_efo_channels_by_integration_v1(type)

List Channels

Returns the list of supported Channels (Data types) for a given integration type

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.integration_channels_response import IntegrationChannelsResponse
from sysdig_client.models.integration_type import IntegrationType
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
    api_instance = sysdig_client.EventsForwarderApi(api_client)
    type = sysdig_client.IntegrationType() # IntegrationType | the Events Forwarder Integration Type

    try:
        # List Channels
        api_response = api_instance.list_efo_channels_by_integration_v1(type)
        print("The response of EventsForwarderApi->list_efo_channels_by_integration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsForwarderApi->list_efo_channels_by_integration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**IntegrationType**](.md)| the Events Forwarder Integration Type | 

### Return type

[**IntegrationChannelsResponse**](IntegrationChannelsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of supported Events Forwarder integrations channels in Sysdig Secure |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_efo_integrations_types_v1**
> IntegrationTypesResponse list_efo_integrations_types_v1()

List Integrations types

Returns the list of supported integrations, to which Events Forwarder can send data

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.integration_types_response import IntegrationTypesResponse
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
    api_instance = sysdig_client.EventsForwarderApi(api_client)

    try:
        # List Integrations types
        api_response = api_instance.list_efo_integrations_types_v1()
        print("The response of EventsForwarderApi->list_efo_integrations_types_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsForwarderApi->list_efo_integrations_types_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IntegrationTypesResponse**](IntegrationTypesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of supported Events Forwarder integrations in Sysdig Secure |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_efo_integrations_v1**
> ListIntegrationsResponse list_efo_integrations_v1()

List Integrations

Returns the Events Forwarder integrations set up

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.list_integrations_response import ListIntegrationsResponse
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
    api_instance = sysdig_client.EventsForwarderApi(api_client)

    try:
        # List Integrations
        api_response = api_instance.list_efo_integrations_v1()
        print("The response of EventsForwarderApi->list_efo_integrations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsForwarderApi->list_efo_integrations_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListIntegrationsResponse**](ListIntegrationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Events Forwarder Integrations |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_efo_integration_by_id_v1**
> IntegrationResponse update_efo_integration_by_id_v1(integration_id, update_integration_request)

Update Integration

Updates an integration, replacing its configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.integration_response import IntegrationResponse
from sysdig_client.models.update_integration_request import UpdateIntegrationRequest
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
    api_instance = sysdig_client.EventsForwarderApi(api_client)
    integration_id = 56 # int | ID of the integration to return
    update_integration_request = sysdig_client.UpdateIntegrationRequest() # UpdateIntegrationRequest | Update an  events forwarder integration in Sysdig Secure

    try:
        # Update Integration
        api_response = api_instance.update_efo_integration_by_id_v1(integration_id, update_integration_request)
        print("The response of EventsForwarderApi->update_efo_integration_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsForwarderApi->update_efo_integration_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| ID of the integration to return | 
 **update_integration_request** | [**UpdateIntegrationRequest**](UpdateIntegrationRequest.md)| Update an  events forwarder integration in Sysdig Secure | 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration updated successfully |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Integration not found |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

