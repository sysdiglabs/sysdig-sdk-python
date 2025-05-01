# SbomComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specifies the type of component. For software components, classify as application if no more specific appropriate classification is available or cannot be determined for the component. Types include:  * __application__ &#x3D; A software application. Refer to [https://en.wikipedia.org/wiki/Application_software](https://en.wikipedia.org/wiki/Application_software) for information about applications. * __framework__ &#x3D; A software framework. Refer to [https://en.wikipedia.org/wiki/Software_framework](https://en.wikipedia.org/wiki/Software_framework) for information on how frameworks vary slightly from libraries. * __library__ &#x3D; A software library. Refer to [https://en.wikipedia.org/wiki/Library_(computing)](https://en.wikipedia.org/wiki/Library_(computing))  for information about libraries. All third-party and open source reusable components will likely be a library. If the library also has key features of a framework, then it should be classified as a framework. If not, or is unknown, then specifying library is RECOMMENDED. * __container__ &#x3D; A packaging and/or runtime format, not specific to any particular technology, which isolates software inside the container from software outside of a container through virtualization technology. Refer to [https://en.wikipedia.org/wiki/OS-level_virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization) * __platform__ &#x3D; A runtime environment which interprets or executes software. This may include runtimes such as those that execute bytecode or low-code/no-code application platforms. * __operating-system__ &#x3D; A software operating system without regard to deployment model (i.e. installed on physical hardware, virtual machine, image, etc) Refer to [https://en.wikipedia.org/wiki/Operating_system](https://en.wikipedia.org/wiki/Operating_system) * __device__ &#x3D; A hardware device such as a processor, or chip-set. A hardware device containing firmware SHOULD include a component for the physical hardware itself, and another component of type &#39;firmware&#39; or &#39;operating-system&#39; (whichever is relevant), describing information about the software running on the device.   See also the list of [known device properties](https://github.com/CycloneDX/cyclonedx-property-taxonomy/blob/main/cdx/device.md). * __device-driver__ &#x3D; A special type of software that operates or controls a particular type of device. Refer to [https://en.wikipedia.org/wiki/Device_driver](https://en.wikipedia.org/wiki/Device_driver) * __firmware__ &#x3D; A special type of software that provides low-level control over a devices hardware. Refer to [https://en.wikipedia.org/wiki/Firmware](https://en.wikipedia.org/wiki/Firmware) * __file__ &#x3D; A computer file. Refer to [https://en.wikipedia.org/wiki/Computer_file](https://en.wikipedia.org/wiki/Computer_file) for information about files. * __machine-learning-model__ &#x3D; A model based on training data that can make predictions or decisions without being explicitly programmed to do so. * __data__ &#x3D; A collection of discrete values that convey information. | 
**name** | **str** | The name of the component. This will often be a shortened, single name of the component. Examples: commons-lang3 and jquery | 
**bom_ref** | **str** | An optional identifier which can be used to reference the component elsewhere in the BOM. Every bom-ref MUST be unique within the BOM. | [optional] 
**version** | **str** | The component version. The version should ideally comply with semantic versioning but is not enforced. | [optional] 
**group** | **str** | The grouping name or identifier. This will often be a shortened, single name of the company or project that produced the component, or the source package or domain name. Whitespace and special characters should be avoided. Examples include: apache, org.apache.commons, and apache.org. | [optional] 
**purl** | **str** | Specifies the package-url (purl). The purl, if specified, MUST be valid and conform to the specification defined at: [https://github.com/package-url/purl-spec](https://github.com/package-url/purl-spec) | [optional] 

## Example

```python
from sysdig_client.models.sbom_component import SbomComponent

# TODO update the JSON string below
json = "{}"
# create an instance of SbomComponent from a JSON string
sbom_component_instance = SbomComponent.from_json(json)
# print the JSON string representation of the object
print(SbomComponent.to_json())

# convert the object into a dict
sbom_component_dict = sbom_component_instance.to_dict()
# create an instance of SbomComponent from a dict
sbom_component_from_dict = SbomComponent.from_dict(sbom_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


