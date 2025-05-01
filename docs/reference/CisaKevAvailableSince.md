# CisaKevAvailableSince

Number of days since the vulnerability was added to CISA's Known Exploited Vulnerabilities (KEV) catalog. Calculated from initial inclusion date to current date. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**CisaKevPublishDateExtra**](CisaKevPublishDateExtra.md) |  | 

## Example

```python
from sysdig_client.models.cisa_kev_available_since import CisaKevAvailableSince

# TODO update the JSON string below
json = "{}"
# create an instance of CisaKevAvailableSince from a JSON string
cisa_kev_available_since_instance = CisaKevAvailableSince.from_json(json)
# print the JSON string representation of the object
print(CisaKevAvailableSince.to_json())

# convert the object into a dict
cisa_kev_available_since_dict = cisa_kev_available_since_instance.to_dict()
# create an instance of CisaKevAvailableSince from a dict
cisa_kev_available_since_from_dict = CisaKevAvailableSince.from_dict(cisa_kev_available_since_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


