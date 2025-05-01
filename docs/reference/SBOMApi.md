# sysdig_client.SBOMApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sbomv1beta1**](SBOMApi.md#get_sbomv1beta1) | **GET** /secure/vulnerability/v1beta1/sboms | Get SBOM


# **get_sbomv1beta1**
> SbomResultResponse get_sbomv1beta1(asset_id=asset_id, asset_type=asset_type, bom_identifier=bom_identifier)

Get SBOM

Retrieve a SBOM (Software Bill Of Material) in CycloneDX format.

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.sbom_result_response import SbomResultResponse
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
    api_instance = sysdig_client.SBOMApi(api_client)
    asset_id = 'sha256:6147d53c2a3a4d99b8343665430e5d420eb7ee65cb89995b6bea1af2595be53a' # str | The ID of the asset for which we want to retrieve the SBOM. It's the imageId for container-image and the hostId for hosts Provide this with assetType if not providing bomIdentifier  (optional)
    asset_type = 'asset_type_example' # str | The type of the asset for which we want to retrieve the SBOM. Provide this with assetId if not providing bomIdentifier (optional)
    bom_identifier = 'urn:uuid:6536eeee-b8f2-4865-b996-adc991c28202' # str | The ID of a single SBOM. Either provide this or both assetId and assetType (optional)

    try:
        # Get SBOM
        api_response = api_instance.get_sbomv1beta1(asset_id=asset_id, asset_type=asset_type, bom_identifier=bom_identifier)
        print("The response of SBOMApi->get_sbomv1beta1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SBOMApi->get_sbomv1beta1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset for which we want to retrieve the SBOM. It&#39;s the imageId for container-image and the hostId for hosts Provide this with assetType if not providing bomIdentifier  | [optional] 
 **asset_type** | **str**| The type of the asset for which we want to retrieve the SBOM. Provide this with assetId if not providing bomIdentifier | [optional] 
 **bom_identifier** | **str**| The ID of a single SBOM. Either provide this or both assetId and assetType | [optional] 

### Return type

[**SbomResultResponse**](SbomResultResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response, contains the requested SBOM. |  * Content-Type -  <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**406** | Server can&#39;t produce a response in the content-type requested by the client |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

