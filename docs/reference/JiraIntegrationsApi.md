# sysdig_client.JiraIntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_jira_integration_v1**](JiraIntegrationsApi.md#create_jira_integration_v1) | **POST** /platform/jira/v1/integrations | Create Jira integration
[**create_jira_issue_type_v1**](JiraIntegrationsApi.md#create_jira_issue_type_v1) | **POST** /platform/jira/v1/integrations/{integrationId}/issue-types | Create Jira issue type
[**delete_jira_integration_v1**](JiraIntegrationsApi.md#delete_jira_integration_v1) | **DELETE** /platform/jira/v1/integrations/{integrationId} | Delete Jira integration
[**delete_jira_issue_type_v1**](JiraIntegrationsApi.md#delete_jira_issue_type_v1) | **DELETE** /platform/jira/v1/integrations/{integrationId}/issue-types/{issueTypeId} | Delete Jira issue type
[**get_jira_integration_v1**](JiraIntegrationsApi.md#get_jira_integration_v1) | **GET** /platform/jira/v1/integrations/{integrationId} | Get Jira integration
[**get_jira_integrations_v1**](JiraIntegrationsApi.md#get_jira_integrations_v1) | **GET** /platform/jira/v1/integrations | List Jira integrations
[**get_jira_issue_type_v1**](JiraIntegrationsApi.md#get_jira_issue_type_v1) | **GET** /platform/jira/v1/integrations/{integrationId}/issue-types/{issueTypeId} | Get Jira issue type
[**get_jira_issue_types_v1**](JiraIntegrationsApi.md#get_jira_issue_types_v1) | **GET** /platform/jira/v1/integrations/{integrationId}/issue-types | List Jira issue types
[**update_jira_integration_v1**](JiraIntegrationsApi.md#update_jira_integration_v1) | **PUT** /platform/jira/v1/integrations/{integrationId} | Update Jira integration
[**update_jira_issue_type_v1**](JiraIntegrationsApi.md#update_jira_issue_type_v1) | **PUT** /platform/jira/v1/integrations/{integrationId}/issue-types/{issueTypeId} | Update Jira issue type


# **create_jira_integration_v1**
> IntegrationResponseV1 create_jira_integration_v1(create_integration_request_v1)

Create Jira integration

This operation creates a Jira integration on the Sysdig platform.  **Required permissions:** *ticketing-integration.write* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_integration_request_v1 import CreateIntegrationRequestV1
from sysdig_client.models.integration_response_v1 import IntegrationResponseV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    create_integration_request_v1 = sysdig_client.CreateIntegrationRequestV1() # CreateIntegrationRequestV1 | A Jira integration to create

    try:
        # Create Jira integration
        api_response = api_instance.create_jira_integration_v1(create_integration_request_v1)
        print("The response of JiraIntegrationsApi->create_jira_integration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->create_jira_integration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_integration_request_v1** | [**CreateIntegrationRequestV1**](CreateIntegrationRequestV1.md)| A Jira integration to create | 

### Return type

[**IntegrationResponseV1**](IntegrationResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Jira integration |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_jira_issue_type_v1**
> IssueTypeResponseV1 create_jira_issue_type_v1(integration_id, create_issue_type_request_v1)

Create Jira issue type

This operation creates a Jira issue type on the Sysdig platform for the particular Jira integration.  **Required permissions:** *ticketing-integration.write* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_issue_type_request_v1 import CreateIssueTypeRequestV1
from sysdig_client.models.issue_type_response_v1 import IssueTypeResponseV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier
    create_issue_type_request_v1 = sysdig_client.CreateIssueTypeRequestV1() # CreateIssueTypeRequestV1 | A Jira issue type to create

    try:
        # Create Jira issue type
        api_response = api_instance.create_jira_issue_type_v1(integration_id, create_issue_type_request_v1)
        print("The response of JiraIntegrationsApi->create_jira_issue_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->create_jira_issue_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 
 **create_issue_type_request_v1** | [**CreateIssueTypeRequestV1**](CreateIssueTypeRequestV1.md)| A Jira issue type to create | 

### Return type

[**IssueTypeResponseV1**](IssueTypeResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Jira issue type |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jira_integration_v1**
> delete_jira_integration_v1(integration_id)

Delete Jira integration

This operation deletes a specific Jira integration on the Sysdig platform.  **Required permissions:** *ticketing-integration.write* 

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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier

    try:
        # Delete Jira integration
        api_instance.delete_jira_integration_v1(integration_id)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->delete_jira_integration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 

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
**204** | Jira integration deleted successfully |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jira_issue_type_v1**
> delete_jira_issue_type_v1(integration_id, issue_type_id)

Delete Jira issue type

This operation deletes a specific Jira issue type on the Sysdig platform.  **Required permissions:** *ticketing-integration.write* 

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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier
    issue_type_id = 56 # int | Jira issue type identifier

    try:
        # Delete Jira issue type
        api_instance.delete_jira_issue_type_v1(integration_id, issue_type_id)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->delete_jira_issue_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 
 **issue_type_id** | **int**| Jira issue type identifier | 

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
**204** | Jira issue type deleted successfully |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jira_integration_v1**
> IntegrationResponseV1 get_jira_integration_v1(integration_id)

Get Jira integration

This operation returns a specific Jira integration from the Sysdig platform.  **Required permissions:** *ticketing-integration.read* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.integration_response_v1 import IntegrationResponseV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier

    try:
        # Get Jira integration
        api_response = api_instance.get_jira_integration_v1(integration_id)
        print("The response of JiraIntegrationsApi->get_jira_integration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->get_jira_integration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 

### Return type

[**IntegrationResponseV1**](IntegrationResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific Jira integration |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jira_integrations_v1**
> PaginatedIntegrationsResponseV1 get_jira_integrations_v1(limit=limit, offset=offset, enabled=enabled)

List Jira integrations

This operation returns a paginated list of Jira integrations from the Sysdig platform.  **Required permissions:** *ticketing-integration.read* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.paginated_integrations_response_v1 import PaginatedIntegrationsResponseV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    enabled = false # bool | Enabled status of the integration (optional)

    try:
        # List Jira integrations
        api_response = api_instance.get_jira_integrations_v1(limit=limit, offset=offset, enabled=enabled)
        print("The response of JiraIntegrationsApi->get_jira_integrations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->get_jira_integrations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **enabled** | **bool**| Enabled status of the integration | [optional] 

### Return type

[**PaginatedIntegrationsResponseV1**](PaginatedIntegrationsResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Jira integrations |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jira_issue_type_v1**
> IssueTypeResponseV1 get_jira_issue_type_v1(integration_id, issue_type_id)

Get Jira issue type

This operation returns a specific Jira issue type from the Sysdig platform.  **Required permissions:** *ticketing-integration.read* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.issue_type_response_v1 import IssueTypeResponseV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier
    issue_type_id = 56 # int | Jira issue type identifier

    try:
        # Get Jira issue type
        api_response = api_instance.get_jira_issue_type_v1(integration_id, issue_type_id)
        print("The response of JiraIntegrationsApi->get_jira_issue_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->get_jira_issue_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 
 **issue_type_id** | **int**| Jira issue type identifier | 

### Return type

[**IssueTypeResponseV1**](IssueTypeResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific Jira issue type |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jira_issue_types_v1**
> IssueTypesResponseV1 get_jira_issue_types_v1(integration_id)

List Jira issue types

This operation returns a list of Jira issue types from the Sysdig platform, associated with a particular Jira integration.  **Required permissions:** *ticketing-integration.read* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.issue_types_response_v1 import IssueTypesResponseV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier

    try:
        # List Jira issue types
        api_response = api_instance.get_jira_issue_types_v1(integration_id)
        print("The response of JiraIntegrationsApi->get_jira_issue_types_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->get_jira_issue_types_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 

### Return type

[**IssueTypesResponseV1**](IssueTypesResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Jira issue types for the particular Jira integration |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jira_integration_v1**
> IntegrationResponseV1 update_jira_integration_v1(integration_id, update_integration_request_v1=update_integration_request_v1)

Update Jira integration

This operation updates a specific Jira integration on the Sysdig platform.  **Required permissions:** *ticketing-integration.write* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.integration_response_v1 import IntegrationResponseV1
from sysdig_client.models.update_integration_request_v1 import UpdateIntegrationRequestV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier
    update_integration_request_v1 = sysdig_client.UpdateIntegrationRequestV1() # UpdateIntegrationRequestV1 | The Jira integration to update (optional)

    try:
        # Update Jira integration
        api_response = api_instance.update_jira_integration_v1(integration_id, update_integration_request_v1=update_integration_request_v1)
        print("The response of JiraIntegrationsApi->update_jira_integration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->update_jira_integration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 
 **update_integration_request_v1** | [**UpdateIntegrationRequestV1**](UpdateIntegrationRequestV1.md)| The Jira integration to update | [optional] 

### Return type

[**IntegrationResponseV1**](IntegrationResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Jira integration |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jira_issue_type_v1**
> IssueTypeResponseV1 update_jira_issue_type_v1(integration_id, issue_type_id, update_issue_type_request_v1=update_issue_type_request_v1)

Update Jira issue type

This operation updates a specific Jira issue type on the Sysdig platform.  **Required permissions:** *ticketing-integration.write* 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.issue_type_response_v1 import IssueTypeResponseV1
from sysdig_client.models.update_issue_type_request_v1 import UpdateIssueTypeRequestV1
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
    api_instance = sysdig_client.JiraIntegrationsApi(api_client)
    integration_id = 56 # int | Jira integration identifier
    issue_type_id = 56 # int | Jira issue type identifier
    update_issue_type_request_v1 = sysdig_client.UpdateIssueTypeRequestV1() # UpdateIssueTypeRequestV1 | A Jira issue type to update (optional)

    try:
        # Update Jira issue type
        api_response = api_instance.update_jira_issue_type_v1(integration_id, issue_type_id, update_issue_type_request_v1=update_issue_type_request_v1)
        print("The response of JiraIntegrationsApi->update_jira_issue_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JiraIntegrationsApi->update_jira_issue_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Jira integration identifier | 
 **issue_type_id** | **int**| Jira issue type identifier | 
 **update_issue_type_request_v1** | [**UpdateIssueTypeRequestV1**](UpdateIssueTypeRequestV1.md)| A Jira issue type to update | [optional] 

### Return type

[**IssueTypeResponseV1**](IssueTypeResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Jira issue type |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

