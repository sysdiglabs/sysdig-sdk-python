# sysdig_client.TeamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team_v1**](TeamsApi.md#create_team_v1) | **POST** /platform/v1/teams | Create Team
[**delete_team_by_id_v1**](TeamsApi.md#delete_team_by_id_v1) | **DELETE** /platform/v1/teams/{teamId} | Delete Team
[**delete_team_user_by_id_v1**](TeamsApi.md#delete_team_user_by_id_v1) | **DELETE** /platform/v1/teams/{teamId}/users/{userId} | Delete Membership
[**get_team_by_id_v1**](TeamsApi.md#get_team_by_id_v1) | **GET** /platform/v1/teams/{teamId} | Get Team
[**get_team_user_by_id_v1**](TeamsApi.md#get_team_user_by_id_v1) | **GET** /platform/v1/teams/{teamId}/users/{userId} | Get Membership
[**get_team_users_v1**](TeamsApi.md#get_team_users_v1) | **GET** /platform/v1/teams/{teamId}/users | List Memberships
[**get_teams_v1**](TeamsApi.md#get_teams_v1) | **GET** /platform/v1/teams | List Teams
[**save_team_user_v1**](TeamsApi.md#save_team_user_v1) | **PUT** /platform/v1/teams/{teamId}/users/{userId} | Save Membership
[**update_team_by_id_v1**](TeamsApi.md#update_team_by_id_v1) | **PUT** /platform/v1/teams/{teamId} | Update Team


# **create_team_v1**
> TeamResponseV1 create_team_v1(create_team_request_v1=create_team_request_v1)

Create Team

Create a new team.\\ \\ **Required permissions:** _teams.create_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.create_team_request_v1 import CreateTeamRequestV1
from sysdig_client.models.team_response_v1 import TeamResponseV1
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
    api_instance = sysdig_client.TeamsApi(api_client)
    create_team_request_v1 = sysdig_client.CreateTeamRequestV1() # CreateTeamRequestV1 | The payload required to create a new team. (optional)

    try:
        # Create Team
        api_response = api_instance.create_team_v1(create_team_request_v1=create_team_request_v1)
        print("The response of TeamsApi->create_team_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->create_team_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_team_request_v1** | [**CreateTeamRequestV1**](CreateTeamRequestV1.md)| The payload required to create a new team. | [optional] 

### Return type

[**TeamResponseV1**](TeamResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Team created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_by_id_v1**
> delete_team_by_id_v1(team_id)

Delete Team

Delete a team by its ID.\\ \\ **Required permissions:** _teams.edit_ 

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
    api_instance = sysdig_client.TeamsApi(api_client)
    team_id = 56 # int | The team ID.

    try:
        # Delete Team
        api_instance.delete_team_by_id_v1(team_id)
    except Exception as e:
        print("Exception when calling TeamsApi->delete_team_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 

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
**204** | Team deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_user_by_id_v1**
> delete_team_user_by_id_v1(team_id, user_id)

Delete Membership

Delete a membership defined by its ID.\\ \\ **Required permissions:** _memberships.edit_ 

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
    api_instance = sysdig_client.TeamsApi(api_client)
    team_id = 56 # int | The team ID.
    user_id = 56 # int | The user ID.

    try:
        # Delete Membership
        api_instance.delete_team_user_by_id_v1(team_id, user_id)
    except Exception as e:
        print("Exception when calling TeamsApi->delete_team_user_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **user_id** | **int**| The user ID. | 

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
**204** | Membership deleted. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_by_id_v1**
> TeamResponseV1 get_team_by_id_v1(team_id)

Get Team

Return a team by ID.\\ \\ **Required permissions:** _customer-teams.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.team_response_v1 import TeamResponseV1
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
    api_instance = sysdig_client.TeamsApi(api_client)
    team_id = 56 # int | The team ID.

    try:
        # Get Team
        api_response = api_instance.get_team_by_id_v1(team_id)
        print("The response of TeamsApi->get_team_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 

### Return type

[**TeamResponseV1**](TeamResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_user_by_id_v1**
> TeamUserResponseV1 get_team_user_by_id_v1(team_id, user_id)

Get Membership

Return a membership by its ID.\\ \\ **Required permissions:** _memberships.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.team_user_response_v1 import TeamUserResponseV1
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
    api_instance = sysdig_client.TeamsApi(api_client)
    team_id = 56 # int | The team ID.
    user_id = 56 # int | The user ID.

    try:
        # Get Membership
        api_response = api_instance.get_team_user_by_id_v1(team_id, user_id)
        print("The response of TeamsApi->get_team_user_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_user_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **user_id** | **int**| The user ID. | 

### Return type

[**TeamUserResponseV1**](TeamUserResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Membership found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_users_v1**
> GetTeamUsersPaginatedResponseV1 get_team_users_v1(team_id, offset=offset, limit=limit)

List Memberships

Retrieve a paginated list of memberships in a given team ID.\\ \\ **Required permissions:** _memberships.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_team_users_paginated_response_v1 import GetTeamUsersPaginatedResponseV1
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
    api_instance = sysdig_client.TeamsApi(api_client)
    team_id = 56 # int | The team ID.
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)

    try:
        # List Memberships
        api_response = api_instance.get_team_users_v1(team_id, offset=offset, limit=limit)
        print("The response of TeamsApi->get_team_users_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_users_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]

### Return type

[**GetTeamUsersPaginatedResponseV1**](GetTeamUsersPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The memberships page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_v1**
> GetTeamsPaginatedResponseV1 get_teams_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)

List Teams

Retrieve a paginated list of teams.\\ \\ **Required permissions:** _customer-teams.read_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.get_teams_paginated_response_v1 import GetTeamsPaginatedResponseV1
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
    api_instance = sysdig_client.TeamsApi(api_client)
    offset = 0 # int | The offset number of items to start with (optional) (default to 0)
    limit = 25 # int | The number of items to return (optional) (default to 25)
    orderby = '' # str | The order by field separated by a colon for the direction (optional) (default to '')
    filter = '' # str | The filter by field separated by a colon for the filter value (optional) (default to '')

    try:
        # List Teams
        api_response = api_instance.get_teams_v1(offset=offset, limit=limit, orderby=orderby, filter=filter)
        print("The response of TeamsApi->get_teams_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_teams_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset number of items to start with | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 25]
 **orderby** | **str**| The order by field separated by a colon for the direction | [optional] [default to &#39;&#39;]
 **filter** | **str**| The filter by field separated by a colon for the filter value | [optional] [default to &#39;&#39;]

### Return type

[**GetTeamsPaginatedResponseV1**](GetTeamsPaginatedResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The teams page. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_team_user_v1**
> TeamUserResponseV1 save_team_user_v1(team_id, user_id, save_team_user_request_v1=save_team_user_request_v1)

Save Membership

Add or update a membership.  | Permission             | Description                                                                                             | | -----------------------| --------------------------------------------------------------------------------------------------------| | memberships.edit       | Required to create a new membership.                                                                    | | memberships-roles.edit | Required to change roles of an existing membership or to create a new membership with a specific role.  | 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.save_team_user_request_v1 import SaveTeamUserRequestV1
from sysdig_client.models.team_user_response_v1 import TeamUserResponseV1
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
    api_instance = sysdig_client.TeamsApi(api_client)
    team_id = 56 # int | The team ID.
    user_id = 56 # int | The user ID.
    save_team_user_request_v1 = sysdig_client.SaveTeamUserRequestV1() # SaveTeamUserRequestV1 |  (optional)

    try:
        # Save Membership
        api_response = api_instance.save_team_user_v1(team_id, user_id, save_team_user_request_v1=save_team_user_request_v1)
        print("The response of TeamsApi->save_team_user_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->save_team_user_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **user_id** | **int**| The user ID. | 
 **save_team_user_request_v1** | [**SaveTeamUserRequestV1**](SaveTeamUserRequestV1.md)|  | [optional] 

### Return type

[**TeamUserResponseV1**](TeamUserResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Membership updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**201** | Membership created. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_by_id_v1**
> TeamResponseV1 update_team_by_id_v1(team_id, update_team_request_v1=update_team_request_v1)

Update Team

Update a team by its ID.\\ \\ **Required permissions:** _teams.edit_ 

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.team_response_v1 import TeamResponseV1
from sysdig_client.models.update_team_request_v1 import UpdateTeamRequestV1
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
    api_instance = sysdig_client.TeamsApi(api_client)
    team_id = 56 # int | The team ID.
    update_team_request_v1 = sysdig_client.UpdateTeamRequestV1() # UpdateTeamRequestV1 |  (optional)

    try:
        # Update Team
        api_response = api_instance.update_team_by_id_v1(team_id, update_team_request_v1=update_team_request_v1)
        print("The response of TeamsApi->update_team_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->update_team_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The team ID. | 
 **update_team_request_v1** | [**UpdateTeamRequestV1**](UpdateTeamRequestV1.md)|  | [optional] 

### Return type

[**TeamResponseV1**](TeamResponseV1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team updated. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**404** | Not found. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**409** | Conflict. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**415** | Server cannot accept content of type specified in Content-Type header. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**422** | Server was unable to process the request. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

