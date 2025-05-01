# sysdig_client.SSOSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sso_settings_v1**](SSOSettingsApi.md#create_sso_settings_v1) | **POST** /platform/v1/sso-settings | Create SSO Settings
[**delete_sso_settings_by_id_v1**](SSOSettingsApi.md#delete_sso_settings_by_id_v1) | **DELETE** /platform/v1/sso-settings/{ssoSettingsId} | Delete SSO Settings
[**get_sso_settings_by_id_v1**](SSOSettingsApi.md#get_sso_settings_by_id_v1) | **GET** /platform/v1/sso-settings/{ssoSettingsId} | Get SSO Settings
[**get_sso_settings_v1**](SSOSettingsApi.md#get_sso_settings_v1) | **GET** /platform/v1/sso-settings | List SSO Settings
[**update_sso_settings_by_id_v1**](SSOSettingsApi.md#update_sso_settings_by_id_v1) | **PUT** /platform/v1/sso-settings/{ssoSettingsId} | Update SSO Settings


# **create_sso_settings_v1**
> SsoSettingsResponseV1 create_sso_settings_v1(create_sso_settings_request_v1=create_sso_settings_request_v1)

Create SSO Settings

Create a new SSO settings.\\ \\ **Required permissions:** _sso-setting.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_sso_settings_request_v1 import CreateSsoSettingsRequestV1
from sysdig_client.models.sso_settings_response_v1 import SsoSettingsResponseV1
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
    api_instance = sysdig_client.SSOSettingsApi(api_client)
    create_sso_settings_request_v1 = sysdig_client.CreateSsoSettingsRequestV1() # CreateSsoSettingsRequestV1 | The payload required to create SSO settings. (optional)

    try:
        # Create SSO Settings
        api_response = api_instance.create_sso_settings_v1(create_sso_settings_request_v1=create_sso_settings_request_v1)
        print("The response of SSOSettingsApi->create_sso_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->create_sso_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sso_settings_request_v1** | [**CreateSsoSettingsRequestV1**](CreateSsoSettingsRequestV1.md)| The payload required to create SSO settings. | [optional] 

### Return type

[**SsoSettingsResponseV1**](SsoSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SSO settings created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sso_settings_by_id_v1**
> delete_sso_settings_by_id_v1(sso_settings_id)

Delete SSO Settings

Delete SSO settings by its ID.\\ \\ **Required permissions:** _sso-settings.edit_ 

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
    api_instance = sysdig_client.SSOSettingsApi(api_client)
    sso_settings_id = 56 # int | SSO settings ID.

    try:
        # Delete SSO Settings
        api_instance.delete_sso_settings_by_id_v1(sso_settings_id)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->delete_sso_settings_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_settings_id** | **int**| SSO settings ID. | 

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
**204** | SSO settings deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_settings_by_id_v1**
> SsoSettingsResponseV1 get_sso_settings_by_id_v1(sso_settings_id)

Get SSO Settings

Return SSO settings by ID.\\ \\ **Required permissions:** _sso-settings.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.sso_settings_response_v1 import SsoSettingsResponseV1
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
    api_instance = sysdig_client.SSOSettingsApi(api_client)
    sso_settings_id = 56 # int | SSO settings ID.

    try:
        # Get SSO Settings
        api_response = api_instance.get_sso_settings_by_id_v1(sso_settings_id)
        print("The response of SSOSettingsApi->get_sso_settings_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->get_sso_settings_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_settings_id** | **int**| SSO settings ID. | 

### Return type

[**SsoSettingsResponseV1**](SsoSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSO settings found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_settings_v1**
> AllSsoSettingsResponseV1 get_sso_settings_v1(filter=filter)

List SSO Settings

Retrieve a paginated list of SSO settings.\\ \\ **Required permissions:** _sso-settings.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.all_sso_settings_response_v1 import AllSsoSettingsResponseV1
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
    api_instance = sysdig_client.SSOSettingsApi(api_client)
    filter = '' # str | The filter by field separated by a colon for the filter value (optional) (default to '')

    try:
        # List SSO Settings
        api_response = api_instance.get_sso_settings_v1(filter=filter)
        print("The response of SSOSettingsApi->get_sso_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->get_sso_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter by field separated by a colon for the filter value | [optional] [default to &#39;&#39;]

### Return type

[**AllSsoSettingsResponseV1**](AllSsoSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all SSO settings response. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sso_settings_by_id_v1**
> SsoSettingsResponseV1 update_sso_settings_by_id_v1(sso_settings_id, update_sso_settings_request_v1=update_sso_settings_request_v1)

Update SSO Settings

Update SSO settings by its ID.\\ \\ **Required permissions:** _sso-settings.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.sso_settings_response_v1 import SsoSettingsResponseV1
from sysdig_client.models.update_sso_settings_request_v1 import UpdateSsoSettingsRequestV1
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
    api_instance = sysdig_client.SSOSettingsApi(api_client)
    sso_settings_id = 56 # int | SSO settings ID.
    update_sso_settings_request_v1 = sysdig_client.UpdateSsoSettingsRequestV1() # UpdateSsoSettingsRequestV1 |  (optional)

    try:
        # Update SSO Settings
        api_response = api_instance.update_sso_settings_by_id_v1(sso_settings_id, update_sso_settings_request_v1=update_sso_settings_request_v1)
        print("The response of SSOSettingsApi->update_sso_settings_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSOSettingsApi->update_sso_settings_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_settings_id** | **int**| SSO settings ID. | 
 **update_sso_settings_request_v1** | [**UpdateSsoSettingsRequestV1**](UpdateSsoSettingsRequestV1.md)|  | [optional] 

### Return type

[**SsoSettingsResponseV1**](SsoSettingsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSO setting updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

