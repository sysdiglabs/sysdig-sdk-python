# sysdig_client.ServiceAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_service_account_v1**](ServiceAccountsApi.md#create_global_service_account_v1) | **POST** /platform/v1/service-accounts | Create a Global Service Account
[**create_team_service_account_v1**](ServiceAccountsApi.md#create_team_service_account_v1) | **POST** /platform/v1/teams/{teamId}/service-accounts | Create a Team Service Account
[**delete_global_service_account_by_id_v1**](ServiceAccountsApi.md#delete_global_service_account_by_id_v1) | **DELETE** /platform/v1/service-accounts/{serviceAccountId} | Delete a Global Service Account
[**delete_team_service_account_by_id_v1**](ServiceAccountsApi.md#delete_team_service_account_by_id_v1) | **DELETE** /platform/v1/teams/{teamId}/service-accounts/{serviceAccountId} | Delete a Team Service Account
[**get_global_service_account_by_id_v1**](ServiceAccountsApi.md#get_global_service_account_by_id_v1) | **GET** /platform/v1/service-accounts/{serviceAccountId} | Get a Global Service Account
[**get_global_service_accounts_v1**](ServiceAccountsApi.md#get_global_service_accounts_v1) | **GET** /platform/v1/service-accounts | List Global Service Accounts
[**get_team_service_account_by_id_v1**](ServiceAccountsApi.md#get_team_service_account_by_id_v1) | **GET** /platform/v1/teams/{teamId}/service-accounts/{serviceAccountId} | Get a Team Service Account
[**get_team_service_accounts_v1**](ServiceAccountsApi.md#get_team_service_accounts_v1) | **GET** /platform/v1/teams/{teamId}/service-accounts | List Team Service Accounts


# **create_global_service_account_v1**
> ServiceAccountWithKeyResponseV1 create_global_service_account_v1(create_global_service_account_request_v1=create_global_service_account_request_v1)

Create a Global Service Account

Create a new global service account.\\ \\ **Required permissions:** _global-service-accounts.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_global_service_account_request_v1 import CreateGlobalServiceAccountRequestV1
from sysdig_client.models.service_account_with_key_response_v1 import ServiceAccountWithKeyResponseV1
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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    create_global_service_account_request_v1 = sysdig_client.CreateGlobalServiceAccountRequestV1() # CreateGlobalServiceAccountRequestV1 | The payload required to create a new global service account. (optional)

    try:
        # Create a Global Service Account
        api_response = api_instance.create_global_service_account_v1(create_global_service_account_request_v1=create_global_service_account_request_v1)
        print("The response of ServiceAccountsApi->create_global_service_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->create_global_service_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_global_service_account_request_v1** | [**CreateGlobalServiceAccountRequestV1**](CreateGlobalServiceAccountRequestV1.md)| The payload required to create a new global service account. | [optional] 

### Return type

[**ServiceAccountWithKeyResponseV1**](ServiceAccountWithKeyResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Global service account created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team_service_account_v1**
> ServiceAccountWithKeyResponseV1 create_team_service_account_v1(team_id, create_team_service_account_request_v1=create_team_service_account_request_v1)

Create a Team Service Account

Create a new team service account.\\ \\ **Required permissions:** _team-service-accounts.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_team_service_account_request_v1 import CreateTeamServiceAccountRequestV1
from sysdig_client.models.service_account_with_key_response_v1 import ServiceAccountWithKeyResponseV1
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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    team_id = 56 # int | The team ID.
    create_team_service_account_request_v1 = sysdig_client.CreateTeamServiceAccountRequestV1() # CreateTeamServiceAccountRequestV1 | The payload required to create a new team service account. (optional)

    try:
        # Create a Team Service Account
        api_response = api_instance.create_team_service_account_v1(team_id, create_team_service_account_request_v1=create_team_service_account_request_v1)
        print("The response of ServiceAccountsApi->create_team_service_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->create_team_service_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **create_team_service_account_request_v1** | [**CreateTeamServiceAccountRequestV1**](CreateTeamServiceAccountRequestV1.md)| The payload required to create a new team service account. | [optional] 

### Return type

[**ServiceAccountWithKeyResponseV1**](ServiceAccountWithKeyResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Team service account created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_service_account_by_id_v1**
> delete_global_service_account_by_id_v1(service_account_id)

Delete a Global Service Account

Delete a global service account by ID.\\ \\ **Required permissions:** _global-service-accounts.edit_ 

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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    service_account_id = 56 # int | The service account ID.

    try:
        # Delete a Global Service Account
        api_instance.delete_global_service_account_by_id_v1(service_account_id)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->delete_global_service_account_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **int**| The service account ID. | 

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
**204** | Global service account deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_service_account_by_id_v1**
> delete_team_service_account_by_id_v1(team_id, service_account_id)

Delete a Team Service Account

Delete a team service account by ID.\\ \\ **Required permissions:** _team-service-accounts.edit_ 

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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    team_id = 56 # int | The team ID.
    service_account_id = 56 # int | The service account ID.

    try:
        # Delete a Team Service Account
        api_instance.delete_team_service_account_by_id_v1(team_id, service_account_id)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->delete_team_service_account_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **service_account_id** | **int**| The service account ID. | 

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
**204** | Team service account deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_service_account_by_id_v1**
> ServiceAccountResponseV1 get_global_service_account_by_id_v1(service_account_id)

Get a Global Service Account

Return a global service account by ID.\\ \\ **Required permissions:** _global-service-accounts.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.service_account_response_v1 import ServiceAccountResponseV1
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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    service_account_id = 56 # int | The service account ID.

    try:
        # Get a Global Service Account
        api_response = api_instance.get_global_service_account_by_id_v1(service_account_id)
        print("The response of ServiceAccountsApi->get_global_service_account_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->get_global_service_account_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **int**| The service account ID. | 

### Return type

[**ServiceAccountResponseV1**](ServiceAccountResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Global service account found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_service_accounts_v1**
> GetServiceAccountsPaginatedResponseV1 get_global_service_accounts_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)

List Global Service Accounts

Retrieve a paginated list of all service accounts.\\ \\ **Required permissions:** _global-service-accounts.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_service_accounts_paginated_response_v1 import GetServiceAccountsPaginatedResponseV1
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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    orderby = '' # str | The order by field separated by a colon for the direction (optional) (default to '')
    filter = [] # List[str] | Filters to apply in the form of `key:value`.\\ Multiple filters can be applied by repeating the `filter` parameter:\\ `&filter=key1:value1&filter=key2:value2`  (optional) (default to [])

    try:
        # List Global Service Accounts
        api_response = api_instance.get_global_service_accounts_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)
        print("The response of ServiceAccountsApi->get_global_service_accounts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->get_global_service_accounts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **orderby** | **str**| The order by field separated by a colon for the direction | [optional] [default to &#39;&#39;]
 **filter** | [**List[str]**](str.md)| Filters to apply in the form of &#x60;key:value&#x60;.\\ Multiple filters can be applied by repeating the &#x60;filter&#x60; parameter:\\ &#x60;&amp;filter&#x3D;key1:value1&amp;filter&#x3D;key2:value2&#x60;  | [optional] [default to []]

### Return type

[**GetServiceAccountsPaginatedResponseV1**](GetServiceAccountsPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service accounts page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_service_account_by_id_v1**
> ServiceAccountResponseV1 get_team_service_account_by_id_v1(team_id, service_account_id)

Get a Team Service Account

Return a team service account by ID.\\ \\ **Required permissions:** _team-service-accounts.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.service_account_response_v1 import ServiceAccountResponseV1
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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    team_id = 56 # int | The team ID.
    service_account_id = 56 # int | The service account ID.

    try:
        # Get a Team Service Account
        api_response = api_instance.get_team_service_account_by_id_v1(team_id, service_account_id)
        print("The response of ServiceAccountsApi->get_team_service_account_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->get_team_service_account_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **service_account_id** | **int**| The service account ID. | 

### Return type

[**ServiceAccountResponseV1**](ServiceAccountResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team service account found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_service_accounts_v1**
> GetServiceAccountsPaginatedResponseV1 get_team_service_accounts_v1(team_id, offset=offset, limit=limit, orderby=orderby, filter=filter)

List Team Service Accounts

Retrieve a paginated list of team service accounts.\\ \\ **Required permissions:** _team-service-accounts.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_service_accounts_paginated_response_v1 import GetServiceAccountsPaginatedResponseV1
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
    api_instance = sysdig_client.ServiceAccountsApi(api_client)
    team_id = 56 # int | The team ID.
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    orderby = '' # str | The order by field separated by a colon for the direction (optional) (default to '')
    filter = [] # List[str] | Filters to apply in the form of `key:value`.\\ Multiple filters can be applied by repeating the `filter` parameter:\\ `&filter=key1:value1&filter=key2:value2`  (optional) (default to [])

    try:
        # List Team Service Accounts
        api_response = api_instance.get_team_service_accounts_v1(team_id, offset=offset, limit=limit, orderby=orderby, filter=filter)
        print("The response of ServiceAccountsApi->get_team_service_accounts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->get_team_service_accounts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **orderby** | **str**| The order by field separated by a colon for the direction | [optional] [default to &#39;&#39;]
 **filter** | [**List[str]**](str.md)| Filters to apply in the form of &#x60;key:value&#x60;.\\ Multiple filters can be applied by repeating the &#x60;filter&#x60; parameter:\\ &#x60;&amp;filter&#x3D;key1:value1&amp;filter&#x3D;key2:value2&#x60;  | [optional] [default to []]

### Return type

[**GetServiceAccountsPaginatedResponseV1**](GetServiceAccountsPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The team service accounts page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

