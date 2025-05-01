# sysdig_client.CostAdvisorCustomPricingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_v1**](CostAdvisorCustomPricingApi.md#create_pricing_v1) | **POST** /monitor/cost-advisor/v1/pricing | Create Pricing
[**delete_pricing_by_id_v1**](CostAdvisorCustomPricingApi.md#delete_pricing_by_id_v1) | **DELETE** /monitor/cost-advisor/v1/pricing/{pricingId} | Delete Pricing
[**get_pricing_by_id_v1**](CostAdvisorCustomPricingApi.md#get_pricing_by_id_v1) | **GET** /monitor/cost-advisor/v1/pricing/{pricingId} | Get Pricing
[**get_pricing_projected_costs_v1**](CostAdvisorCustomPricingApi.md#get_pricing_projected_costs_v1) | **GET** /monitor/cost-advisor/v1/pricing/{pricingId}/projected-costs | Get Pricing Projected Costs
[**get_pricing_v1**](CostAdvisorCustomPricingApi.md#get_pricing_v1) | **GET** /monitor/cost-advisor/v1/pricing | List Pricing
[**update_pricing_by_id_v1**](CostAdvisorCustomPricingApi.md#update_pricing_by_id_v1) | **PUT** /monitor/cost-advisor/v1/pricing/{pricingId} | Update Pricing


# **create_pricing_v1**
> PricingResponseV1 create_pricing_v1(create_pricing_request_v1=create_pricing_request_v1)

Create Pricing

Change a new pricing to use as default (for cloud providers that Cost Advisor doesn't automatically support) or for a specific Kubernetes cluster.\\ \\ You need to specify hourly costs for 1 CPU, 1GB of RAM and 1GB of storage. \\ Different CPU and RAM costs can be specified for spot instances; to enable Cost Advisor to identify the spot node, a label and spot value must also be set. \\ \\ Cluster hourly cost = sum(node hourly costs) + (total storage * storage unit cost). \\ Node hourly cost = (total CPUs * CPU unit cost) + (total RAM * RAM unit cost) \\ \\ **Required permissions:** _cost-advisor.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_pricing_request_v1 import CreatePricingRequestV1
from sysdig_client.models.pricing_response_v1 import PricingResponseV1
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
    api_instance = sysdig_client.CostAdvisorCustomPricingApi(api_client)
    create_pricing_request_v1 = sysdig_client.CreatePricingRequestV1() # CreatePricingRequestV1 | The payload to create pricing. Use the type field to create a default pricing or pricing for a specific Kubernetes cluster. (optional)

    try:
        # Create Pricing
        api_response = api_instance.create_pricing_v1(create_pricing_request_v1=create_pricing_request_v1)
        print("The response of CostAdvisorCustomPricingApi->create_pricing_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAdvisorCustomPricingApi->create_pricing_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pricing_request_v1** | [**CreatePricingRequestV1**](CreatePricingRequestV1.md)| The payload to create pricing. Use the type field to create a default pricing or pricing for a specific Kubernetes cluster. | [optional] 

### Return type

[**PricingResponseV1**](PricingResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Pricing created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pricing_by_id_v1**
> delete_pricing_by_id_v1(pricing_id)

Delete Pricing

Delete a pricing by its ID. If the pricing deleted is the DEFAULT one. Cost Advisor will continue to compute costs for the unsupported Kubernetes cluster using the Sysdig default pricing.\\ \\ **Required permissions:** _cost-advisor.edit_ 

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
    api_instance = sysdig_client.CostAdvisorCustomPricingApi(api_client)
    pricing_id = 56 # int | The pricing ID.

    try:
        # Delete Pricing
        api_instance.delete_pricing_by_id_v1(pricing_id)
    except Exception as e:
        print("Exception when calling CostAdvisorCustomPricingApi->delete_pricing_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_id** | **int**| The pricing ID. | 

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
**204** | Pricing deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_by_id_v1**
> PricingResponseV1 get_pricing_by_id_v1(pricing_id)

Get Pricing

Retrieve a pricing by ID.\\ \\ **Required permissions:** _cost-advisor.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.pricing_response_v1 import PricingResponseV1
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
    api_instance = sysdig_client.CostAdvisorCustomPricingApi(api_client)
    pricing_id = 56 # int | The pricing ID.

    try:
        # Get Pricing
        api_response = api_instance.get_pricing_by_id_v1(pricing_id)
        print("The response of CostAdvisorCustomPricingApi->get_pricing_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAdvisorCustomPricingApi->get_pricing_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_id** | **int**| The pricing ID. | 

### Return type

[**PricingResponseV1**](PricingResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_projected_costs_v1**
> GetPricingProjectedPaginatedResponseV1 get_pricing_projected_costs_v1(pricing_id, offset=offset, limit=limit)

Get Pricing Projected Costs

Retrieve the monthly projected costs for the clusters using the specified pricing.\\ The computation is done using the total CPU and RAM for the current cluster's nodes and the total storage used by the cluster.\\ \\ Projected monthly cost = 730 * (total CPUs * CPU unit cost) + (total RAM * RAM unit cost) + (total storage * storage unit cost). \\ \\ **Required permissions:** _cost-advisor.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_pricing_projected_paginated_response_v1 import GetPricingProjectedPaginatedResponseV1
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
    api_instance = sysdig_client.CostAdvisorCustomPricingApi(api_client)
    pricing_id = 56 # int | The pricing ID.
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)

    try:
        # Get Pricing Projected Costs
        api_response = api_instance.get_pricing_projected_costs_v1(pricing_id, offset=offset, limit=limit)
        print("The response of CostAdvisorCustomPricingApi->get_pricing_projected_costs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAdvisorCustomPricingApi->get_pricing_projected_costs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_id** | **int**| The pricing ID. | 
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]

### Return type

[**GetPricingProjectedPaginatedResponseV1**](GetPricingProjectedPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Montlhy projected costs. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_v1**
> GetPricingPaginatedResponseV1 get_pricing_v1(offset=offset, limit=limit, cluster_name=cluster_name, type=type)

List Pricing

Retrieve a paginated list of pricing.\\ \\ **Required permissions:** _cost-advisor.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_pricing_paginated_response_v1 import GetPricingPaginatedResponseV1
from sysdig_client.models.pricing_type import PricingType
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
    api_instance = sysdig_client.CostAdvisorCustomPricingApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    cluster_name = 'prod-us-1' # str | The name of the Kubernetes cluster for which you want to retrive the pricing.  (optional)
    type = sysdig_client.PricingType() # PricingType | The type of pricing to find.  (optional)

    try:
        # List Pricing
        api_response = api_instance.get_pricing_v1(offset=offset, limit=limit, cluster_name=cluster_name, type=type)
        print("The response of CostAdvisorCustomPricingApi->get_pricing_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAdvisorCustomPricingApi->get_pricing_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **cluster_name** | **str**| The name of the Kubernetes cluster for which you want to retrive the pricing.  | [optional] 
 **type** | [**PricingType**](.md)| The type of pricing to find.  | [optional] 

### Return type

[**GetPricingPaginatedResponseV1**](GetPricingPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pricing page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pricing_by_id_v1**
> PricingResponseV1 update_pricing_by_id_v1(pricing_id, update_pricing_request_v1=update_pricing_request_v1)

Update Pricing

The pricing payload containing the changes you want to apply to the pricing.\\ \\ **Required permissions:** _cost-advisor.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.pricing_response_v1 import PricingResponseV1
from sysdig_client.models.update_pricing_request_v1 import UpdatePricingRequestV1
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
    api_instance = sysdig_client.CostAdvisorCustomPricingApi(api_client)
    pricing_id = 56 # int | The pricing ID.
    update_pricing_request_v1 = sysdig_client.UpdatePricingRequestV1() # UpdatePricingRequestV1 | The payload required to create the pricing. (optional)

    try:
        # Update Pricing
        api_response = api_instance.update_pricing_by_id_v1(pricing_id, update_pricing_request_v1=update_pricing_request_v1)
        print("The response of CostAdvisorCustomPricingApi->update_pricing_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAdvisorCustomPricingApi->update_pricing_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_id** | **int**| The pricing ID. | 
 **update_pricing_request_v1** | [**UpdatePricingRequestV1**](UpdatePricingRequestV1.md)| The payload required to create the pricing. | [optional] 

### Return type

[**PricingResponseV1**](PricingResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pricing updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

