# CvssScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**score** | **float** | CVSS score | 
**vector** | **str** | attack vector | [optional] 

## Example

```python
from sysdig_client.models.cvss_score import CvssScore

# TODO update the JSON string below
json = "{}"
# create an instance of CvssScore from a JSON string
cvss_score_instance = CvssScore.from_json(json)
# print the JSON string representation of the object
print(CvssScore.to_json())

# convert the object into a dict
cvss_score_dict = cvss_score_instance.to_dict()
# create an instance of CvssScore from a dict
cvss_score_from_dict = CvssScore.from_dict(cvss_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


