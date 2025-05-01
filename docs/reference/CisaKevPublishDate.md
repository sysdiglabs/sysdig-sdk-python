# CisaKevPublishDate

Number of days remaining until the CISA KEV-listed vulnerability is fixed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**extra** | [**CisaKevPublishDateExtra**](CisaKevPublishDateExtra.md) |  | 

## Example

```python
from sysdig_client.models.cisa_kev_publish_date import CisaKevPublishDate

# TODO update the JSON string below
json = "{}"
# create an instance of CisaKevPublishDate from a JSON string
cisa_kev_publish_date_instance = CisaKevPublishDate.from_json(json)
# print the JSON string representation of the object
print(CisaKevPublishDate.to_json())

# convert the object into a dict
cisa_kev_publish_date_dict = cisa_kev_publish_date_instance.to_dict()
# create an instance of CisaKevPublishDate from a dict
cisa_kev_publish_date_from_dict = CisaKevPublishDate.from_dict(cisa_kev_publish_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


