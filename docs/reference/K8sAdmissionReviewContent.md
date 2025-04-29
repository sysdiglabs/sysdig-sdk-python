# K8sAdmissionReviewContent

Kubernetes admission requests-posture checks event content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EventContentType**](EventContentType.md) |  | 
**namespace** | **str** | Kubernetes namespace | [optional] 
**cluster_name** | **str** | Kubernetes cluster name | [optional] 
**resource_name** | **str** | Kubernetes resource name | [optional] 
**resource_kind** | **str** | Kubernetes resource kind | [optional] 
**zones** | [**List[Zone]**](Zone.md) | List of zones that match the scope of the resource. | [optional] 
**scan_result** | [**K8sAdmissionReviewContentAllOfScanResult**](K8sAdmissionReviewContentAllOfScanResult.md) |  | 

## Example

```python
from sysdig_client.models.k8s_admission_review_content import K8sAdmissionReviewContent

# TODO update the JSON string below
json = "{}"
# create an instance of K8sAdmissionReviewContent from a JSON string
k8s_admission_review_content_instance = K8sAdmissionReviewContent.from_json(json)
# print the JSON string representation of the object
print(K8sAdmissionReviewContent.to_json())

# convert the object into a dict
k8s_admission_review_content_dict = k8s_admission_review_content_instance.to_dict()
# create an instance of K8sAdmissionReviewContent from a dict
k8s_admission_review_content_from_dict = K8sAdmissionReviewContent.from_dict(k8s_admission_review_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


