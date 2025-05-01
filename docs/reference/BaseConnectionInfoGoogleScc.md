# BaseConnectionInfoGoogleScc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **str** | ID of your GCP organization | 
**security_marks** | [**List[KeyValueObject]**](KeyValueObject.md) | additional annotations to add to assets or findings as they get forwarded to Security Command Center | [optional] 

## Example

```python
from sysdig_client.models.base_connection_info_google_scc import BaseConnectionInfoGoogleScc

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnectionInfoGoogleScc from a JSON string
base_connection_info_google_scc_instance = BaseConnectionInfoGoogleScc.from_json(json)
# print the JSON string representation of the object
print(BaseConnectionInfoGoogleScc.to_json())

# convert the object into a dict
base_connection_info_google_scc_dict = base_connection_info_google_scc_instance.to_dict()
# create an instance of BaseConnectionInfoGoogleScc from a dict
base_connection_info_google_scc_from_dict = BaseConnectionInfoGoogleScc.from_dict(base_connection_info_google_scc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


