# ListRiskAcceptedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**OffsetPaginatedResponsePage**](OffsetPaginatedResponsePage.md) |  | [optional] 
**data** | [**List[ListRiskAcceptedResponseAllOfData]**](ListRiskAcceptedResponseAllOfData.md) | List of Accepted Risks | 

## Example

```python
from sysdig_client.models.list_risk_accepted_response import ListRiskAcceptedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRiskAcceptedResponse from a JSON string
list_risk_accepted_response_instance = ListRiskAcceptedResponse.from_json(json)
# print the JSON string representation of the object
print(ListRiskAcceptedResponse.to_json())

# convert the object into a dict
list_risk_accepted_response_dict = list_risk_accepted_response_instance.to_dict()
# create an instance of ListRiskAcceptedResponse from a dict
list_risk_accepted_response_from_dict = ListRiskAcceptedResponse.from_dict(list_risk_accepted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


