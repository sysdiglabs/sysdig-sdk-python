# sysdig_client.ResponseActionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_execution_file_acquire_v1**](ResponseActionsApi.md#get_action_execution_file_acquire_v1) | **GET** /secure/response-actions/v1alpha1/action-executions/{actionExecutionId}/acquired-file | Get Acquired File
[**get_action_execution_v1**](ResponseActionsApi.md#get_action_execution_v1) | **GET** /secure/response-actions/v1alpha1/action-executions/{actionExecutionId} | Get Action Execution
[**get_action_executionsv1**](ResponseActionsApi.md#get_action_executionsv1) | **GET** /secure/response-actions/v1alpha1/action-executions | Returns the list of Response Actions executions. You can filter them with the available query parameters.
[**get_actions_v1**](ResponseActionsApi.md#get_actions_v1) | **GET** /secure/response-actions/v1alpha1/actions | Get All Response Actions
[**submit_action_executionv1**](ResponseActionsApi.md#submit_action_executionv1) | **POST** /secure/response-actions/v1alpha1/action-executions | Submit the execution of an action
[**undo_action_execution_v1**](ResponseActionsApi.md#undo_action_execution_v1) | **DELETE** /secure/response-actions/v1alpha1/action-executions/{actionExecutionId} | Undoes an Action Execution


# **get_action_execution_file_acquire_v1**
> bytearray get_action_execution_file_acquire_v1(action_execution_id)

Get Acquired File

Download a Capture file created by an executed \"File Acquire\" Response Action.\\ \\ **Required permissions:** _data-gathering-response-actions.read_ 

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
    api_instance = sysdig_client.ResponseActionsApi(api_client)
    action_execution_id = '1234567890123456789012345678901234567890123456789012345678901234' # str | ID of the action execution

    try:
        # Get Acquired File
        api_response = api_instance.get_action_execution_file_acquire_v1(action_execution_id)
        print("The response of ResponseActionsApi->get_action_execution_file_acquire_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResponseActionsApi->get_action_execution_file_acquire_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_execution_id** | **str**| ID of the action execution | 

### Return type

**bytearray**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The content of the capture file created by a \&quot;File Acquire\&quot; response action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_execution_v1**
> ActionExecution get_action_execution_v1(action_execution_id)

Get Action Execution

Get an action execution.\\ \\ **Required permissions:** _containment-response-actions.read_ or _data-gathering-response-actions.read_, depending on the action type. Results will include the executions of the Response Actions you are allowed to see. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.action_execution import ActionExecution
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
    api_instance = sysdig_client.ResponseActionsApi(api_client)
    action_execution_id = '1234567890123456789012345678901234567890123456789012345678901234' # str | ID of the action execution

    try:
        # Get Action Execution
        api_response = api_instance.get_action_execution_v1(action_execution_id)
        print("The response of ResponseActionsApi->get_action_execution_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResponseActionsApi->get_action_execution_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_execution_id** | **str**| ID of the action execution | 

### Return type

[**ActionExecution**](ActionExecution.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The action execution. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_executionsv1**
> ActionExecutions get_action_executionsv1(caller_id=caller_id, filter=filter, limit=limit, offset=offset, var_from=var_from, to=to)

Returns the list of Response Actions executions. You can filter them with the available query parameters.

Returns a list of action executions. **Required permissions:** _containment-response-actions.read_ or _data-gathering-response-actions.read_, depending on the action type. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.action_executions import ActionExecutions
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
    api_instance = sysdig_client.ResponseActionsApi(api_client)
    caller_id = 'caller_id_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)

    try:
        # Returns the list of Response Actions executions. You can filter them with the available query parameters.
        api_response = api_instance.get_action_executionsv1(caller_id=caller_id, filter=filter, limit=limit, offset=offset, var_from=var_from, to=to)
        print("The response of ResponseActionsApi->get_action_executionsv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResponseActionsApi->get_action_executionsv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **caller_id** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 

### Return type

[**ActionExecutions**](ActionExecutions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The executions list has been returned correctly. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid or inconsistent parameters. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_v1**
> Actions get_actions_v1(context=context)

Get All Response Actions

Get the list of available executable Response Actions.\\ \\ **Required permissions:** _containment-response-actions.exec_ or _data-gathering-response-actions.exec_, depending on the action type. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.actions import Actions
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
    api_instance = sysdig_client.ResponseActionsApi(api_client)
    context = {'key': 'context_example'} # Dict[str, str] |  (optional)

    try:
        # Get All Response Actions
        api_response = api_instance.get_actions_v1(context=context)
        print("The response of ResponseActionsApi->get_actions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResponseActionsApi->get_actions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | [**Dict[str, str]**](str.md)|  | [optional] 

### Return type

[**Actions**](Actions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The action execution. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_action_executionv1**
> ActionExecution submit_action_executionv1(submit_action_execution_request)

Submit the execution of an action

Submits the execution of an action. The action will be executed asynchronously and the response will contain the action execution ID.\\ **Required permissions:** _containment-response-actions.exec_ or _data-gathering-response-actions.exec_, depending on the action type. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.action_execution import ActionExecution
from sysdig_client.models.submit_action_execution_request import SubmitActionExecutionRequest
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
    api_instance = sysdig_client.ResponseActionsApi(api_client)
    submit_action_execution_request = sysdig_client.SubmitActionExecutionRequest() # SubmitActionExecutionRequest | Configuration for the new integration

    try:
        # Submit the execution of an action
        api_response = api_instance.submit_action_executionv1(submit_action_execution_request)
        print("The response of ResponseActionsApi->submit_action_executionv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResponseActionsApi->submit_action_executionv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_action_execution_request** | [**SubmitActionExecutionRequest**](SubmitActionExecutionRequest.md)| Configuration for the new integration | 

### Return type

[**ActionExecution**](ActionExecution.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Response Action execution request has been submitted correctly. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid or inconsistent parameters |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undo_action_execution_v1**
> ActionExecution undo_action_execution_v1(action_execution_id, submit_undo_action_execution_request=submit_undo_action_execution_request)

Undoes an Action Execution

Undoes an action execution.\\ \\ **Required permissions:** _containment-response-actions.exec_ or _data-gathering-response-actions.exec_, depending on the action type. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.action_execution import ActionExecution
from sysdig_client.models.submit_undo_action_execution_request import SubmitUndoActionExecutionRequest
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
    api_instance = sysdig_client.ResponseActionsApi(api_client)
    action_execution_id = '1234567890123456789012345678901234567890123456789012345678901234' # str | ID of the action execution
    submit_undo_action_execution_request = sysdig_client.SubmitUndoActionExecutionRequest() # SubmitUndoActionExecutionRequest | Metadata for the undo action execution. (optional)

    try:
        # Undoes an Action Execution
        api_response = api_instance.undo_action_execution_v1(action_execution_id, submit_undo_action_execution_request=submit_undo_action_execution_request)
        print("The response of ResponseActionsApi->undo_action_execution_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResponseActionsApi->undo_action_execution_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_execution_id** | **str**| ID of the action execution | 
 **submit_undo_action_execution_request** | [**SubmitUndoActionExecutionRequest**](SubmitUndoActionExecutionRequest.md)| Metadata for the undo action execution. | [optional] 

### Return type

[**ActionExecution**](ActionExecution.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The undo action execution. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

