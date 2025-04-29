# SourceDetails

Additional details related to the Event source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of component that generated the raw event: - &#x60;cloud&#x60; - Cloud platform - &#x60;git&#x60; - Git platform - &#x60;iam&#x60; - Identity and Access Management platform - &#x60;kubernetes&#x60; - Kubernetes control plane - &#x60;workload&#x60; - Workload (from bare metal to *aaS compute)  | 
**sub_type** | **str** | A deeper particularization for the type of component that generated the raw event: - &#x60;auditlogs&#x60; - Audit logs of platforms/apps - &#x60;auditWebhooks&#x60; - Kubernetes Audit - &#x60;caas&#x60; - Container As A Service workload - &#x60;dynamicAdmissionControl&#x60; - Dynamic admission control - &#x60;host&#x60; - Non-containerized host - &#x60;container&#x60; - Container - &#x60;workforce&#x60; - Workforce type IAM  | [optional] 

## Example

```python
from sysdig_client.models.source_details import SourceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDetails from a JSON string
source_details_instance = SourceDetails.from_json(json)
# print the JSON string representation of the object
print(SourceDetails.to_json())

# convert the object into a dict
source_details_dict = source_details_instance.to_dict()
# create an instance of SourceDetails from a dict
source_details_from_dict = SourceDetails.from_dict(source_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


