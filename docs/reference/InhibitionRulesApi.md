# sysdig_client.InhibitionRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inhibition_rule**](InhibitionRulesApi.md#create_inhibition_rule) | **POST** /monitor/alerts/v1/inhibition-rules | Create Inhibition Rule
[**delete_inhibition_rule_by_id**](InhibitionRulesApi.md#delete_inhibition_rule_by_id) | **DELETE** /monitor/alerts/v1/inhibition-rules/{inhibitionRuleId} | Delete Inhibition Rule
[**get_inhibition_rule_by_id**](InhibitionRulesApi.md#get_inhibition_rule_by_id) | **GET** /monitor/alerts/v1/inhibition-rules/{inhibitionRuleId} | Get Inhibition Rule
[**get_inhibition_rules**](InhibitionRulesApi.md#get_inhibition_rules) | **GET** /monitor/alerts/v1/inhibition-rules | List Inhibition Rules
[**update_inhibition_rule**](InhibitionRulesApi.md#update_inhibition_rule) | **PUT** /monitor/alerts/v1/inhibition-rules/{inhibitionRuleId} | Update Inhibition Rule


# **create_inhibition_rule**
> InhibitionRuleResponseV1 create_inhibition_rule(create_inhibition_rule_request_v1)

Create Inhibition Rule

Create an inhibition rule.\\ \\ **Required permissions:** _inhibition-rules.edit_ or _alerts.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_inhibition_rule_request_v1 import CreateInhibitionRuleRequestV1
from sysdig_client.models.inhibition_rule_response_v1 import InhibitionRuleResponseV1
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
    api_instance = sysdig_client.InhibitionRulesApi(api_client)
    create_inhibition_rule_request_v1 = sysdig_client.CreateInhibitionRuleRequestV1() # CreateInhibitionRuleRequestV1 | The inhibition rule to be created.

    try:
        # Create Inhibition Rule
        api_response = api_instance.create_inhibition_rule(create_inhibition_rule_request_v1)
        print("The response of InhibitionRulesApi->create_inhibition_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InhibitionRulesApi->create_inhibition_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inhibition_rule_request_v1** | [**CreateInhibitionRuleRequestV1**](CreateInhibitionRuleRequestV1.md)| The inhibition rule to be created. | 

### Return type

[**InhibitionRuleResponseV1**](InhibitionRuleResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Inhibition rule created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inhibition_rule_by_id**
> delete_inhibition_rule_by_id(inhibition_rule_id)

Delete Inhibition Rule

Delete an inhibition rule by its ID.\\ \\ **Required permissions:** _inhibition-rules.edit_ or _alerts.edit_ 

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
    api_instance = sysdig_client.InhibitionRulesApi(api_client)
    inhibition_rule_id = 56 # int | The inhibition rule ID.

    try:
        # Delete Inhibition Rule
        api_instance.delete_inhibition_rule_by_id(inhibition_rule_id)
    except Exception as e:
        print("Exception when calling InhibitionRulesApi->delete_inhibition_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inhibition_rule_id** | **int**| The inhibition rule ID. | 

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
**204** | Inhibition rule deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inhibition_rule_by_id**
> InhibitionRuleResponseV1 get_inhibition_rule_by_id(inhibition_rule_id)

Get Inhibition Rule

Retrieve an inhibition rule by ID.\\ \\ **Required permissions:** _inhibition-rules.read_ or _alerts.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.inhibition_rule_response_v1 import InhibitionRuleResponseV1
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
    api_instance = sysdig_client.InhibitionRulesApi(api_client)
    inhibition_rule_id = 56 # int | The inhibition rule ID.

    try:
        # Get Inhibition Rule
        api_response = api_instance.get_inhibition_rule_by_id(inhibition_rule_id)
        print("The response of InhibitionRulesApi->get_inhibition_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InhibitionRulesApi->get_inhibition_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inhibition_rule_id** | **int**| The inhibition rule ID. | 

### Return type

[**InhibitionRuleResponseV1**](InhibitionRuleResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inhibition rule found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inhibition_rules**
> GetInhibitionRulesPaginatedResponseV1 get_inhibition_rules(offset=offset, limit=limit)

List Inhibition Rules

Retrieve the list of inhibition rules.\\ \\ **Required permissions:** _inhibition-rules.read_ or _alerts.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_inhibition_rules_paginated_response_v1 import GetInhibitionRulesPaginatedResponseV1
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
    api_instance = sysdig_client.InhibitionRulesApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)

    try:
        # List Inhibition Rules
        api_response = api_instance.get_inhibition_rules(offset=offset, limit=limit)
        print("The response of InhibitionRulesApi->get_inhibition_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InhibitionRulesApi->get_inhibition_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]

### Return type

[**GetInhibitionRulesPaginatedResponseV1**](GetInhibitionRulesPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of inhibition rules. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inhibition_rule**
> InhibitionRuleResponseV1 update_inhibition_rule(inhibition_rule_id, update_inhibition_rule_request_v1)

Update Inhibition Rule

Update an inhibition rule.\\ \\ **Required permissions:** _inhibition-rules.edit_ or _alerts.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.inhibition_rule_response_v1 import InhibitionRuleResponseV1
from sysdig_client.models.update_inhibition_rule_request_v1 import UpdateInhibitionRuleRequestV1
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
    api_instance = sysdig_client.InhibitionRulesApi(api_client)
    inhibition_rule_id = 56 # int | The inhibition rule ID.
    update_inhibition_rule_request_v1 = sysdig_client.UpdateInhibitionRuleRequestV1() # UpdateInhibitionRuleRequestV1 | The new version of the inhibition rule.

    try:
        # Update Inhibition Rule
        api_response = api_instance.update_inhibition_rule(inhibition_rule_id, update_inhibition_rule_request_v1)
        print("The response of InhibitionRulesApi->update_inhibition_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InhibitionRulesApi->update_inhibition_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inhibition_rule_id** | **int**| The inhibition rule ID. | 
 **update_inhibition_rule_request_v1** | [**UpdateInhibitionRuleRequestV1**](UpdateInhibitionRuleRequestV1.md)| The new version of the inhibition rule. | 

### Return type

[**InhibitionRuleResponseV1**](InhibitionRuleResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inhibition rule updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

