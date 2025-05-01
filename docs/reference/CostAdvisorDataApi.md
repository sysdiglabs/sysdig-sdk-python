# sysdig_client.CostAdvisorDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workload_cost_data_v1**](CostAdvisorDataApi.md#get_workload_cost_data_v1) | **POST** /monitor/cost-advisor/v1alpha1/data/workload-cost-trends | Workload Cost Trends Data


# **get_workload_cost_data_v1**
> WorkloadCostTrendsDataResponse get_workload_cost_data_v1(workload_cost_trends_data_request)

Workload Cost Trends Data

Returns workload cost trends data for a specified trend range, pivot date, optional scope, and optional grouping. The response includes cost totals for both current and previous periods, along with the date ranges for each period. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.workload_cost_trends_data_request import WorkloadCostTrendsDataRequest
from sysdig_client.models.workload_cost_trends_data_response import WorkloadCostTrendsDataResponse
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
    api_instance = sysdig_client.CostAdvisorDataApi(api_client)
    workload_cost_trends_data_request = sysdig_client.WorkloadCostTrendsDataRequest() # WorkloadCostTrendsDataRequest | 

    try:
        # Workload Cost Trends Data
        api_response = api_instance.get_workload_cost_data_v1(workload_cost_trends_data_request)
        print("The response of CostAdvisorDataApi->get_workload_cost_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAdvisorDataApi->get_workload_cost_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_cost_trends_data_request** | [**WorkloadCostTrendsDataRequest**](WorkloadCostTrendsDataRequest.md)|  | 

### Return type

[**WorkloadCostTrendsDataResponse**](WorkloadCostTrendsDataResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workload Cost Trend data |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

