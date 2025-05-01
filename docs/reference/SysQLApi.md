# sysdig_client.SysQLApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sysql_schema**](SysQLApi.md#get_sysql_schema) | **GET** /api/sysql/v2/schema | Get SysQL Schema
[**query_sysql_get**](SysQLApi.md#query_sysql_get) | **GET** /api/sysql/v2/query | Execute SysQL query via GET
[**query_sysql_post**](SysQLApi.md#query_sysql_post) | **POST** /api/sysql/v2/query | Execute SysQL query via POST


# **get_sysql_schema**
> str get_sysql_schema()

Get SysQL Schema

Retrieve the schema information for all entities and their relationships in YAML format. This endpoint returns the graph schema definition that describes available entities, their fields, and relationships. 

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
    api_instance = sysdig_client.SysQLApi(api_client)

    try:
        # Get SysQL Schema
        api_response = api_instance.get_sysql_schema()
        print("The response of SysQLApi->get_sysql_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SysQLApi->get_sysql_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the schema information. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_sysql_get**
> QueryResponse query_sysql_get(q, limit=limit, offset=offset, deterministic_order=deterministic_order)

Execute SysQL query via GET

[DEPRECATED] Retrieve resources from the graph datastore using the GET method.  > The GET method for this endpoint is deprecated and will be removed in future versions. > Please use the POST method instead, which provides better support for complex queries. 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.query_response import QueryResponse
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
    api_instance = sysdig_client.SysQLApi(api_client)
    q = 'MATCH IAMUser AS a WHERE a.customerId = 1234567890 RETURN a.name AS name, a.arn AS arn;' # str | The SysQL statement.
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    deterministic_order = False # bool |  (optional) (default to False)

    try:
        # Execute SysQL query via GET
        api_response = api_instance.query_sysql_get(q, limit=limit, offset=offset, deterministic_order=deterministic_order)
        print("The response of SysQLApi->query_sysql_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SysQLApi->query_sysql_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The SysQL statement. | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **deterministic_order** | **bool**|  | [optional] [default to False]

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved resources from the graph database using the provided SysQL statement.  |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_sysql_post**
> QueryResponse query_sysql_post(query_sysql_post_request)

Execute SysQL query via POST

Retrieve resources from the graph datastore using the POST method.

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.query_response import QueryResponse
from sysdig_client.models.query_sysql_post_request import QuerySysqlPostRequest
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
    api_instance = sysdig_client.SysQLApi(api_client)
    query_sysql_post_request = sysdig_client.QuerySysqlPostRequest() # QuerySysqlPostRequest | 

    try:
        # Execute SysQL query via POST
        api_response = api_instance.query_sysql_post(query_sysql_post_request)
        print("The response of SysQLApi->query_sysql_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SysQLApi->query_sysql_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_sysql_post_request** | [**QuerySysqlPostRequest**](QuerySysqlPostRequest.md)|  | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved resources from the graph database using the provided SysQL statement.  |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

