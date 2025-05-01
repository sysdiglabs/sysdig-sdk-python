# sysdig_client.CaptureStorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_capture_storage_configuration_v1**](CaptureStorageApi.md#get_capture_storage_configuration_v1) | **GET** /platform/v1/configuration/capture-storage | Get Capture Storage Configuration
[**update_capture_storage_configuration_v1**](CaptureStorageApi.md#update_capture_storage_configuration_v1) | **PUT** /platform/v1/configuration/capture-storage | Update or Create Capture Storage Configuration


# **get_capture_storage_configuration_v1**
> CaptureStorageConfigurationResponseV1 get_capture_storage_configuration_v1()

Get Capture Storage Configuration

Retrieve the capture storage configuration.\\ \\ **Required permissions:** _sysdig-storage.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.capture_storage_configuration_response_v1 import CaptureStorageConfigurationResponseV1
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
    api_instance = sysdig_client.CaptureStorageApi(api_client)

    try:
        # Get Capture Storage Configuration
        api_response = api_instance.get_capture_storage_configuration_v1()
        print("The response of CaptureStorageApi->get_capture_storage_configuration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaptureStorageApi->get_capture_storage_configuration_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CaptureStorageConfigurationResponseV1**](CaptureStorageConfigurationResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Display the Capture Storage Configuration. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_capture_storage_configuration_v1**
> CaptureStorageConfigurationResponseV1 update_capture_storage_configuration_v1(save_capture_storage_configuration_request_v1=save_capture_storage_configuration_request_v1)

Update or Create Capture Storage Configuration

Update or Create Capture Storage configuration.\\ \\ **Required permissions:** _sysdig-storage.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.capture_storage_configuration_response_v1 import CaptureStorageConfigurationResponseV1
from sysdig_client.models.save_capture_storage_configuration_request_v1 import SaveCaptureStorageConfigurationRequestV1
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
    api_instance = sysdig_client.CaptureStorageApi(api_client)
    save_capture_storage_configuration_request_v1 = sysdig_client.SaveCaptureStorageConfigurationRequestV1() # SaveCaptureStorageConfigurationRequestV1 |  (optional)

    try:
        # Update or Create Capture Storage Configuration
        api_response = api_instance.update_capture_storage_configuration_v1(save_capture_storage_configuration_request_v1=save_capture_storage_configuration_request_v1)
        print("The response of CaptureStorageApi->update_capture_storage_configuration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaptureStorageApi->update_capture_storage_configuration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_capture_storage_configuration_request_v1** | [**SaveCaptureStorageConfigurationRequestV1**](SaveCaptureStorageConfigurationRequestV1.md)|  | [optional] 

### Return type

[**CaptureStorageConfigurationResponseV1**](CaptureStorageConfigurationResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Capture Storage updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

