# InventoryResource

An Inventory Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | Resource unique identifier | 
**name** | **str** | Resource name | 
**platform** | **str** | The resource platform (such as AWS, GCP, Kubernetes, or Azure) | 
**type** | **str** | The resource type | 
**category** | **str** | The resource category | 
**last_seen** | **int** | Last scan date as unix timestamp | 
**is_exposed** | **bool** | Indicates if a resource is exposed to the internet | [optional] 
**validated_exposure** | **bool** | Indicates if a resource which is exposed to the internet could be reach by our network exposure validator | [optional] 
**labels** | **List[str]** | The resource labels | 
**metadata** | **object** | The resource metadata | 
**resource_origin** | **str** | Where a resource was collected (Code, Deployed) | 
**posture_policy_summary** | [**PosturePolicySummary**](PosturePolicySummary.md) |  | [optional] 
**vulnerability_summary** | [**VulnerabilitySummary**](VulnerabilitySummary.md) |  | [optional] 
**in_use_vulnerability_summary** | [**VulnerabilitySummary**](VulnerabilitySummary.md) |  | [optional] 
**zones** | [**List[InventoryZone]**](InventoryZone.md) | Resource zones | 
**config_api_endpoint** | **str** | A link that provides the resource configuration. | [optional] 
**posture_control_summary_api_endpoint** | **str** | A link that provides the posture control summary. | [optional] 
**vm_api_endpoint** | **str** | A link that provides vulnerability management information about an image (Images only). | [optional] 
**container_info** | [**List[ContainerInfo]**](ContainerInfo.md) | List of containers (with some of kubernetes metadata) belonging to this kubernetes workload. If resource is not kubernetes workload this fild will be empty. | [optional] 

## Example

```python
from sysdig_client.models.inventory_resource import InventoryResource

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryResource from a JSON string
inventory_resource_instance = InventoryResource.from_json(json)
# print the JSON string representation of the object
print(InventoryResource.to_json())

# convert the object into a dict
inventory_resource_dict = inventory_resource_instance.to_dict()
# create an instance of InventoryResource from a dict
inventory_resource_from_dict = InventoryResource.from_dict(inventory_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


