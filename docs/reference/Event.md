# Event

Event feed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The event id. | 
**cursor** | **str** | The cursor that can be used to fetch a set of events surrounding this same event. By providing this value as &#x60;cursor&#x60; in a GET &#x60;secureEvents&#x60; request, you will get the set of events surrounding this current event.  | [optional] 
**timestamp** | **int** | The event timestamp in nanoseconds. | 
**originator** | [**Originator**](Originator.md) |  | 
**category** | [**Category**](Category.md) |  | 
**source** | [**Source**](Source.md) |  | 
**source_details** | [**SourceDetails**](SourceDetails.md) |  | [optional] 
**raw_event_originator** | **str** | The agent type, hosting the &#x60;engine&#x60;, that generated the event after the raw event - &#x60;admissionController&#x60; - Admission Controller, part of the Cluster Shield - &#x60;agentless&#x60; - Agentless - &#x60;cloudConnector&#x60; - Cloud Connector - &#x60;linuxAgent&#x60; - Linux Host Agent - &#x60;serverlessAgent&#x60; - Serverless workloads Agent (CaaS) generated events - &#x60;windowsAgent&#x60; - Windows Host Agent  | [optional] 
**raw_event_category** | **str** | The semantic category (area) of the event in the Sysdig product: - &#x60;kspm&#x60; -  Kubernetes Security Posture Management events - &#x60;runtime&#x60; - Threat detection events  | [optional] 
**engine** | **str** | The engine used to generate the event out of the raw signal: - &#x60;drift&#x60; - engine to detect container drifts  - &#x60;falco&#x60; - Falco open source engine - &#x60;list&#x60; - list matching engine for list matching rules - &#x60;machineLearning&#x60; - ML engine - &#x60;malware&#x60; - malware detection engine  | [optional] 
**name** | **str** | Name of the policy the event is generated after. | 
**description** | **str** | Description of the policy the event is generated after. | 
**severity** | **int** | The policy severity: - &#x60;0-3&#x60; - High - &#x60;4-5&#x60; - Medium - &#x60;6&#x60; - Low - &#x60;7&#x60; - Info  | 
**actions** | [**List[Action]**](Action.md) | actions that have been triggered by the event | [optional] 
**content** | [**EventContent**](EventContent.md) |  | [optional] 
**labels** | **Dict[str, str]** | Key value pairs of values. | [optional] 

## Example

```python
from sysdig_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


