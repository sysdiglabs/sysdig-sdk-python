# sysdig_client.CertificatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_csrv1**](CertificatesApi.md#create_csrv1) | **POST** /secure/certman/v1/csr | Create CSR
[**delete_certificate_v1**](CertificatesApi.md#delete_certificate_v1) | **DELETE** /secure/certman/v1/certificates/{certId} | Delete Certificate
[**get_certificate_registration_v1**](CertificatesApi.md#get_certificate_registration_v1) | **GET** /secure/certman/v1/certificates/{certId}/services | List Services
[**get_certificate_v1**](CertificatesApi.md#get_certificate_v1) | **GET** /secure/certman/v1/certificates/{certId} | Get Certificate
[**get_certificates_v1**](CertificatesApi.md#get_certificates_v1) | **GET** /secure/certman/v1/certificates | List Certificates
[**upload_certificate_v1**](CertificatesApi.md#upload_certificate_v1) | **POST** /secure/certman/v1/certificates | Upload Certificate


# **create_csrv1**
> str create_csrv1()

Create CSR

Creates a Certificate Signing Request generated from the customer unique private key. The CSR is generated on the fly.\\ \\ **Required permissions:** _certman.read_ 

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
    api_instance = sysdig_client.CertificatesApi(api_client)

    try:
        # Create CSR
        api_response = api_instance.create_csrv1()
        print("The response of CertificatesApi->create_csrv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->create_csrv1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Certificate Signing Request plaintext content |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate_v1**
> delete_certificate_v1(cert_id)

Delete Certificate

Deletes a certificate given its id.  A certificate cannot be deleted if it's being used (i.e. by the events forwarder to connect to third parties).\\ \\ **Required permissions:** _certman.edit_ 

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
    api_instance = sysdig_client.CertificatesApi(api_client)
    cert_id = 'cert_id_example' # str | ID of the certificate

    try:
        # Delete Certificate
        api_instance.delete_certificate_v1(cert_id)
    except Exception as e:
        print("Exception when calling CertificatesApi->delete_certificate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| ID of the certificate | 

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
**204** | The certificate has been deleted successfully. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | The certificate cannot be deleted because it&#39;s currently being used.  |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_registration_v1**
> ServicesResponse get_certificate_registration_v1(cert_id)

List Services

Returns he list of integrations using this certificate.\\ \\ **Required permissions:** _certman.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.services_response import ServicesResponse
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
    api_instance = sysdig_client.CertificatesApi(api_client)
    cert_id = 'cert_id_example' # str | ID of the certificate

    try:
        # List Services
        api_response = api_instance.get_certificate_registration_v1(cert_id)
        print("The response of CertificatesApi->get_certificate_registration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_certificate_registration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| ID of the certificate | 

### Return type

[**ServicesResponse**](ServicesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of certificates registrations. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Invalid certificate ID |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_v1**
> Certificate get_certificate_v1(cert_id)

Get Certificate

Get a single certificate.\\ \\ **Required permissions:** _certman.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.certificate import Certificate
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
    api_instance = sysdig_client.CertificatesApi(api_client)
    cert_id = 'cert_id_example' # str | ID of the certificate

    try:
        # Get Certificate
        api_response = api_instance.get_certificate_v1(cert_id)
        print("The response of CertificatesApi->get_certificate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_certificate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| ID of the certificate | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The certificate. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Invalid certificate ID |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificates_v1**
> CertificatesResponse get_certificates_v1()

List Certificates

Returns the list of certificates.\\ \\ **Required permissions:** _certman.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.certificates_response import CertificatesResponse
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
    api_instance = sysdig_client.CertificatesApi(api_client)

    try:
        # List Certificates
        api_response = api_instance.get_certificates_v1()
        print("The response of CertificatesApi->get_certificates_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_certificates_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CertificatesResponse**](CertificatesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of certificates. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_certificate_v1**
> Certificate upload_certificate_v1(certificate_file_name, name)

Upload Certificate

Uploads a certificate that has been created by signing a CSR obtained via Certificates Management.\\ \\ **Required permissions:** _certman.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.certificate import Certificate
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
    api_instance = sysdig_client.CertificatesApi(api_client)
    certificate_file_name = None # bytearray | The certificate file to be uploaded
    name = 'name_example' # str | The name of the certificate that is being uploaded

    try:
        # Upload Certificate
        api_response = api_instance.upload_certificate_v1(certificate_file_name, name)
        print("The response of CertificatesApi->upload_certificate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->upload_certificate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_file_name** | **bytearray**| The certificate file to be uploaded | 
 **name** | **str**| The name of the certificate that is being uploaded | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The certificate has been upload correctly. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid certificate |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

