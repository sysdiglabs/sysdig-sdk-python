# EventsFeedPage

Pagination information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The number of events matching the search criteria. This number is always major or equal to the number of events returned.  | 
**prev** | **str** | &#x60;prev&#x60; is a string pointing to the previous page of data. Use this as the &#x60;cursor&#x60; to get the previous page of data.  | [optional] 
**next** | **str** | &#x60;next&#x60; is a string pointing to the next page of data. Use this as the &#x60;cursor&#x60; to scroll paginated results and get the next page of data.  If not included, the current response is the last page.  | [optional] 

## Example

```python
from sysdig_client.models.events_feed_page import EventsFeedPage

# TODO update the JSON string below
json = "{}"
# create an instance of EventsFeedPage from a JSON string
events_feed_page_instance = EventsFeedPage.from_json(json)
# print the JSON string representation of the object
print(EventsFeedPage.to_json())

# convert the object into a dict
events_feed_page_dict = events_feed_page_instance.to_dict()
# create an instance of EventsFeedPage from a dict
events_feed_page_from_dict = EventsFeedPage.from_dict(events_feed_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


