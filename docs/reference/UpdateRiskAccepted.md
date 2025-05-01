# UpdateRiskAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date** | **str** | Date when the accepted risk expires. Setting this to null will make the accepted risk never expire.  | [optional] 
**reason** | **str** | Reason for acceptance | [optional] 
**description** | **str** | Description of why the accepted risk was created | [optional] 

## Example

```python
from sysdig_client.models.update_risk_accepted import UpdateRiskAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRiskAccepted from a JSON string
update_risk_accepted_instance = UpdateRiskAccepted.from_json(json)
# print the JSON string representation of the object
print(UpdateRiskAccepted.to_json())

# convert the object into a dict
update_risk_accepted_dict = update_risk_accepted_instance.to_dict()
# create an instance of UpdateRiskAccepted from a dict
update_risk_accepted_from_dict = UpdateRiskAccepted.from_dict(update_risk_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


