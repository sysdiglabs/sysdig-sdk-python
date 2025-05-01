# sysdig_client.InventoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource**](InventoryApi.md#get_resource) | **GET** /secure/inventory/v1/resources/{hash} | Get Resource
[**get_resources**](InventoryApi.md#get_resources) | **GET** /secure/inventory/v1/resources | List Resources


# **get_resource**
> InventoryResourceExtended get_resource(hash)

Get Resource

Retrieve an Inventory Resource by its unique hash value.

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.inventory_resource_extended import InventoryResourceExtended
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.InventoryApi(api_client)
    hash = 'hash_example' # str | resource hash

    try:
        # Get Resource
        api_response = api_instance.get_resource(hash)
        print("The response of InventoryApi->get_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| resource hash | 

### Return type

[**InventoryResourceExtended**](InventoryResourceExtended.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an Inventory v1 resource. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> InventoryResourceResponse get_resources(filter=filter, page_number=page_number, page_size=page_size, with_enriched_containers=with_enriched_containers)

List Resources

Search for Inventory Resources based on the given filter.

### Example

* Bearer Authentication (bearerAuth):

```python
import sysdig_client
from sysdig_client.models.inventory_resource_response import InventoryResourceResponse
from sysdig_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysdig_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = sysdig_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sysdig_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sysdig_client.InventoryApi(api_client)
    filter = 'platform = \"AWS\" and policy.failed in (\"CIS Amazon Web Services Foundations Benchmark\")' # str | Query language expression for filtering results. Operators: - `and` and `not` logical operators - `=`, `!=` - `in` - `contains` and `startsWith` to check partial values of attributes - `exists` to check if a field exists and not empty  List of supported fields: - `account`   - Type: string   - Example: `account in (\"285211435247\")`   - Description: DEPRECATED. The account that will be included in the results. - `accountName`   - Type: string   - Example: `accountName in (\"some-account-name\")`   - Description: The account name that will be included in the results. - `accountId`   - Type: string   - Example: `accountId in (\"345224567\")`   - Description: The account id that will be included in the results. - `cluster`   - Type: string   - Example: `cluster in (\"cluster1\")`   - Description: The kubernetes cluster that will be included in the results. - `externalDNS`   - Type: string   - Example: `externalDNS in (\"ec2-102-34-15-23.compute-1.amazonaws.com\")`   - Description: The external DNS that will be included in the results. - `distribution`   - Type: string   - Example: `distribution in (\"gke\", \"vanilla\")`   - Description: The kubernetes distribution that will be included in the results. - `integrationName`   - Type: string   - Example: `integrationName = \"github-integration\"`   - Description: The name of the integration an IaC resource belongs to. - `labels`   - Type: string   - Example: `not labels exists`   - Description: The resource labels that will be included in the results. - `location`   - Type: string   - Example: `location starts with \"https://bitbucket.org/organizations-workspace/teams-repository/src\"`   - Description: The web address of an IaC Manifest. - `name`   - Type: string   - Example: `name starts with \"acl\"`   - Description: The names that will be included in the results. - `namespace`   - Type: string   - Example: `namespace contains \"production\"`   - Description: The namespace that will be included in the results. - `nodeType`   - Type: string   - Example: `nodeType=\"Worker\"`   - Description: The nodeType that will be included in the results. - `osName`   - Type: string   - Example: `osName != \"linux\"`   - Description: The operating system that will be included in the results. - `osImage`   - Type: string   - Example: `osImage = \"Ubuntu 18.04.6 LTS\"`   - Description: The operating system image that will be included in the results. - `organization`   - Type: string   - Example: `organization = \"s-xqe92dwe61\"`   - Description: The organization that will be included in the results. - `platform`   - Type: string   - Example: `platform = \"AWS\"`   - Description: The platform that will be included in the results. - `control.accepted`   - Type: boolean   - Example: `control.accepted exists`   - Description: Include (or Exclude) only resources with accepted results. Supported operators: exists and not exists. - `policy`   - Type: string   - Example: `policy in (\"CIS Docker Benchmark\")`   - Description: Include resources that applied the selected policies. Supported operators: in, not in, exists, not exists. - `control.severity`   - Type: string   - Example: `control.severity in (\"High\")`   - Description: Include resources that have violated risks in the selected severities. Supported operators: in, not in. - `control.failed`   - Type: string   - Example: `control.failed in (\"/etc/default/docker owned by root:root\")`   - Description: Include resources that have violated the selected risks. Supported operators: in, not in, exists, not exists. - `policy.failed`   - Type: string   - Example: `policy.failed in (\"PCI DSS (Payment Card Industry Data Security Standard) v3.2.1\")`   - Description: Include resources that failed the selected policies. Supported operators: in, not in, exists, not exists. - `policy.passed` in (\"CIS Kubernetes V1.20 Benchmark\")   - Type: string   - Example: `policy.passed in (\"CIS Kubernetes V1.20 Benchmark\")`   - Description: Include resources that passed the selected policies. Supported operators: in, not in, exists, not exists. - `project`   - Type: string   - Example: `project = \"project1\"`   - Description: DEPRECATED. The project that will be included in the results. - `projectName`   - Type: string   - Example: `projectName = \"project123\"`   - Description: The project name that will be included in the results. - `projectId`   - Type: string   - Example: `projectId = \"1235495521\"`   - Description: The project id that will be included in the results. - `region`   - Type: string   - Example: `region in (\"europe-west1\")`   - Description: The regions that will be included in the results. - `repository`   - Type: string   - Example: `repository in (\"e2e-repo\")`   - Description: The Repository an IaC resource belongs to. - `resourceOrigin`   - Type: string   - Example: `resourceOrigin = \"Code\"`   - Description: Origin of the resource. Supported values: Code, Deployed. - `type`   - Type: string   - Example: `type = \"Account\"`   - Description: The resource types that will be included in the results. - `subscription`   - Type: string   - Example: `subscription = \"Azure subscription 1\"`   - Description: DEPRECATED. The Azure subscription that will be included in the results. - `subscriptionName`   - Type: string   - Example: `subscriptionName = \"subscription abc\"`   - Description: The Azure subscription name that will be included in the results. - `subscriptionId`   - Type: string   - Example: `subscriptionId = \"568634664353\"`   - Description: The Azure subscription id that will be included in the results. - `sourceType`   - Type: string   - Example: `sourceType = \"YAML\"`   - Description: The source type of an IaC resource. Supported values: YAML, Kustomize, Terraform, Helm. - `version`   - Type: string   - Example: `version = \"1.1\"`   - Description: OCP Cluster versions that will be included in the results. - `zone`   - Type: string   - Example: `zone in (\"zone1\")`   - Description: The zones that will be included in the results. - `category`   - Type: string   - Example: `category in (\"Compute\", \"IAM\")`   - Description: The category that will be included in the results. Supported operators: in, not in. - `isExposed`   - Type: boolean   - Example: `isExposed exists`   - Description - Specifies whether the resource to return is exposed to the internet. Supported operators: exists and not exists. - `validatedExposure`   - Type: boolean   - Example: `validatedExposure exists`   - Description - Specifies whether the resource to return is exposed to the internet and could be reach by our network exposure validator. Supported operators: exists and not exists. - `arn`   - Type: string   - Example: `arn in (\"arn:aws:ec2:eu-central-1:843232641625:instance/i-0c1dedd325e71138d\")`   - Description - The AWS ARN of the resource. - `resourceId`   - Type: string   - Example: `resourceId = \"//compute.googleapis.com/projects/project1/global/routes/default-route-192ae83214caddd\"`   - Description - The Azure or GCP Resource Identifier of the resource. - `container.name`   - Type: string   - Example: `container.name in (\"sysdig-container\")`   - Description - Filters the resource by a container. - `architecture`   - Type: string   - Example: `architecture = \"arm64\"`   - Description - Image architecture. - `baseOS`   - Type: string   - Example: `baseOS = \"debian 11.6\"`   - Description - Image Base OS. - `digest`   - Type: string   - Example: `digest = \"sha256:21829f4f033ac2805aa43a412bcdf60e98eee4124d565a06dee184c97efff6091\"`   - Description - Image Digest. - `imageId`   - Type: string   - Example: `imageId in (\"sha256:3768ff6176e29a35ce1354622977a1e5c013045cbc4f30754ef3459218be8ac\")`   - Description - Image Id. - `os`   - Type: string   - Example: `os = \"linux\"`   - Description - Image OS. - `container.imageName`   - Type: string   - Example: `container.imageName in (\"registry.k8s.io/kube-image:v1.2.4\")`   - Description - Image Pullstring. - `image.registry`   - Type: string   - Example: `image.registry = \"quay.io\"`   - Description - Image Registry. - `image.tag`   - Type: string   - Example: `image.tag in (\"tag1\")`   - Description - Image tag. - `package.inUse`   - Type: boolean   - Example: `package.inUse exists`   - Description - Package in use filter. Supported operators: exists and not exists. - `package.info`   - Type: string   - Example: `package.info in (\"github.com/golang/protobuf - v1.5.2\")`   - Description - Filters by a package using the format [packge name] - [version]. - `package.path`   - Type: string   - Example: `package.path in (\"/app\")`   - Description - Filters by package path. - `package.type`   - Type: string   - Example: `package.type in (\"Golang\")`   - Description - Package type. - `vuln.cvssScore`   - Type: string   - Example: `vuln.cvssScore >= \"3\"`   - Description - Filter by vulnerability CVSS. Supported operators: `=` and `>=`. - `vuln.hasExploit`   - Type: boolean   - Example: `vuln.hasExploit exists`   - Description - Filters resources by the existence of vulnerabilities with exploits. Supported operators: exists and not exists. - `vuln.hasFix`   - Type: boolean   - Example: `vuln.hasFix exists`   - Description - Filters resources by the existence of vulnerabilities with fixes. Supported operators: exists and not exists. - `vuln.name`   - Type: string   - Example: `vuln.name in (\"CVE-2023-0049\")`   - Description - Filter by vulnerability name. - `vuln.severity`   - Type: string   - Example: `vuln.severity in (\"Critical\")`   - Description - Filter by vulnerability severity. Supported operators: in, not in, exists and not exists. - `machineImage`   - Type: string   - Example: `machineImage = \"ami-0b22b359fdfabe1b5\"`   - Description - Filter by host machine image.  **Note**: Whenever you filter for values with special characters, ensure that you encode the values. If the special characters are \" or \\, use the escape character \\ and then encode the values.  (optional)
    page_number = 1 # int | Page number. Defaults to 1. (optional)
    page_size = 20 # int | Page size. Defaults to 20. (optional)
    with_enriched_containers = True # bool | If true then for kubernetes workload resources additional container information will be included. (optional)

    try:
        # List Resources
        api_response = api_instance.get_resources(filter=filter, page_number=page_number, page_size=page_size, with_enriched_containers=with_enriched_containers)
        print("The response of InventoryApi->get_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query language expression for filtering results. Operators: - &#x60;and&#x60; and &#x60;not&#x60; logical operators - &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60; - &#x60;in&#x60; - &#x60;contains&#x60; and &#x60;startsWith&#x60; to check partial values of attributes - &#x60;exists&#x60; to check if a field exists and not empty  List of supported fields: - &#x60;account&#x60;   - Type: string   - Example: &#x60;account in (\&quot;285211435247\&quot;)&#x60;   - Description: DEPRECATED. The account that will be included in the results. - &#x60;accountName&#x60;   - Type: string   - Example: &#x60;accountName in (\&quot;some-account-name\&quot;)&#x60;   - Description: The account name that will be included in the results. - &#x60;accountId&#x60;   - Type: string   - Example: &#x60;accountId in (\&quot;345224567\&quot;)&#x60;   - Description: The account id that will be included in the results. - &#x60;cluster&#x60;   - Type: string   - Example: &#x60;cluster in (\&quot;cluster1\&quot;)&#x60;   - Description: The kubernetes cluster that will be included in the results. - &#x60;externalDNS&#x60;   - Type: string   - Example: &#x60;externalDNS in (\&quot;ec2-102-34-15-23.compute-1.amazonaws.com\&quot;)&#x60;   - Description: The external DNS that will be included in the results. - &#x60;distribution&#x60;   - Type: string   - Example: &#x60;distribution in (\&quot;gke\&quot;, \&quot;vanilla\&quot;)&#x60;   - Description: The kubernetes distribution that will be included in the results. - &#x60;integrationName&#x60;   - Type: string   - Example: &#x60;integrationName &#x3D; \&quot;github-integration\&quot;&#x60;   - Description: The name of the integration an IaC resource belongs to. - &#x60;labels&#x60;   - Type: string   - Example: &#x60;not labels exists&#x60;   - Description: The resource labels that will be included in the results. - &#x60;location&#x60;   - Type: string   - Example: &#x60;location starts with \&quot;https://bitbucket.org/organizations-workspace/teams-repository/src\&quot;&#x60;   - Description: The web address of an IaC Manifest. - &#x60;name&#x60;   - Type: string   - Example: &#x60;name starts with \&quot;acl\&quot;&#x60;   - Description: The names that will be included in the results. - &#x60;namespace&#x60;   - Type: string   - Example: &#x60;namespace contains \&quot;production\&quot;&#x60;   - Description: The namespace that will be included in the results. - &#x60;nodeType&#x60;   - Type: string   - Example: &#x60;nodeType&#x3D;\&quot;Worker\&quot;&#x60;   - Description: The nodeType that will be included in the results. - &#x60;osName&#x60;   - Type: string   - Example: &#x60;osName !&#x3D; \&quot;linux\&quot;&#x60;   - Description: The operating system that will be included in the results. - &#x60;osImage&#x60;   - Type: string   - Example: &#x60;osImage &#x3D; \&quot;Ubuntu 18.04.6 LTS\&quot;&#x60;   - Description: The operating system image that will be included in the results. - &#x60;organization&#x60;   - Type: string   - Example: &#x60;organization &#x3D; \&quot;s-xqe92dwe61\&quot;&#x60;   - Description: The organization that will be included in the results. - &#x60;platform&#x60;   - Type: string   - Example: &#x60;platform &#x3D; \&quot;AWS\&quot;&#x60;   - Description: The platform that will be included in the results. - &#x60;control.accepted&#x60;   - Type: boolean   - Example: &#x60;control.accepted exists&#x60;   - Description: Include (or Exclude) only resources with accepted results. Supported operators: exists and not exists. - &#x60;policy&#x60;   - Type: string   - Example: &#x60;policy in (\&quot;CIS Docker Benchmark\&quot;)&#x60;   - Description: Include resources that applied the selected policies. Supported operators: in, not in, exists, not exists. - &#x60;control.severity&#x60;   - Type: string   - Example: &#x60;control.severity in (\&quot;High\&quot;)&#x60;   - Description: Include resources that have violated risks in the selected severities. Supported operators: in, not in. - &#x60;control.failed&#x60;   - Type: string   - Example: &#x60;control.failed in (\&quot;/etc/default/docker owned by root:root\&quot;)&#x60;   - Description: Include resources that have violated the selected risks. Supported operators: in, not in, exists, not exists. - &#x60;policy.failed&#x60;   - Type: string   - Example: &#x60;policy.failed in (\&quot;PCI DSS (Payment Card Industry Data Security Standard) v3.2.1\&quot;)&#x60;   - Description: Include resources that failed the selected policies. Supported operators: in, not in, exists, not exists. - &#x60;policy.passed&#x60; in (\&quot;CIS Kubernetes V1.20 Benchmark\&quot;)   - Type: string   - Example: &#x60;policy.passed in (\&quot;CIS Kubernetes V1.20 Benchmark\&quot;)&#x60;   - Description: Include resources that passed the selected policies. Supported operators: in, not in, exists, not exists. - &#x60;project&#x60;   - Type: string   - Example: &#x60;project &#x3D; \&quot;project1\&quot;&#x60;   - Description: DEPRECATED. The project that will be included in the results. - &#x60;projectName&#x60;   - Type: string   - Example: &#x60;projectName &#x3D; \&quot;project123\&quot;&#x60;   - Description: The project name that will be included in the results. - &#x60;projectId&#x60;   - Type: string   - Example: &#x60;projectId &#x3D; \&quot;1235495521\&quot;&#x60;   - Description: The project id that will be included in the results. - &#x60;region&#x60;   - Type: string   - Example: &#x60;region in (\&quot;europe-west1\&quot;)&#x60;   - Description: The regions that will be included in the results. - &#x60;repository&#x60;   - Type: string   - Example: &#x60;repository in (\&quot;e2e-repo\&quot;)&#x60;   - Description: The Repository an IaC resource belongs to. - &#x60;resourceOrigin&#x60;   - Type: string   - Example: &#x60;resourceOrigin &#x3D; \&quot;Code\&quot;&#x60;   - Description: Origin of the resource. Supported values: Code, Deployed. - &#x60;type&#x60;   - Type: string   - Example: &#x60;type &#x3D; \&quot;Account\&quot;&#x60;   - Description: The resource types that will be included in the results. - &#x60;subscription&#x60;   - Type: string   - Example: &#x60;subscription &#x3D; \&quot;Azure subscription 1\&quot;&#x60;   - Description: DEPRECATED. The Azure subscription that will be included in the results. - &#x60;subscriptionName&#x60;   - Type: string   - Example: &#x60;subscriptionName &#x3D; \&quot;subscription abc\&quot;&#x60;   - Description: The Azure subscription name that will be included in the results. - &#x60;subscriptionId&#x60;   - Type: string   - Example: &#x60;subscriptionId &#x3D; \&quot;568634664353\&quot;&#x60;   - Description: The Azure subscription id that will be included in the results. - &#x60;sourceType&#x60;   - Type: string   - Example: &#x60;sourceType &#x3D; \&quot;YAML\&quot;&#x60;   - Description: The source type of an IaC resource. Supported values: YAML, Kustomize, Terraform, Helm. - &#x60;version&#x60;   - Type: string   - Example: &#x60;version &#x3D; \&quot;1.1\&quot;&#x60;   - Description: OCP Cluster versions that will be included in the results. - &#x60;zone&#x60;   - Type: string   - Example: &#x60;zone in (\&quot;zone1\&quot;)&#x60;   - Description: The zones that will be included in the results. - &#x60;category&#x60;   - Type: string   - Example: &#x60;category in (\&quot;Compute\&quot;, \&quot;IAM\&quot;)&#x60;   - Description: The category that will be included in the results. Supported operators: in, not in. - &#x60;isExposed&#x60;   - Type: boolean   - Example: &#x60;isExposed exists&#x60;   - Description - Specifies whether the resource to return is exposed to the internet. Supported operators: exists and not exists. - &#x60;validatedExposure&#x60;   - Type: boolean   - Example: &#x60;validatedExposure exists&#x60;   - Description - Specifies whether the resource to return is exposed to the internet and could be reach by our network exposure validator. Supported operators: exists and not exists. - &#x60;arn&#x60;   - Type: string   - Example: &#x60;arn in (\&quot;arn:aws:ec2:eu-central-1:843232641625:instance/i-0c1dedd325e71138d\&quot;)&#x60;   - Description - The AWS ARN of the resource. - &#x60;resourceId&#x60;   - Type: string   - Example: &#x60;resourceId &#x3D; \&quot;//compute.googleapis.com/projects/project1/global/routes/default-route-192ae83214caddd\&quot;&#x60;   - Description - The Azure or GCP Resource Identifier of the resource. - &#x60;container.name&#x60;   - Type: string   - Example: &#x60;container.name in (\&quot;sysdig-container\&quot;)&#x60;   - Description - Filters the resource by a container. - &#x60;architecture&#x60;   - Type: string   - Example: &#x60;architecture &#x3D; \&quot;arm64\&quot;&#x60;   - Description - Image architecture. - &#x60;baseOS&#x60;   - Type: string   - Example: &#x60;baseOS &#x3D; \&quot;debian 11.6\&quot;&#x60;   - Description - Image Base OS. - &#x60;digest&#x60;   - Type: string   - Example: &#x60;digest &#x3D; \&quot;sha256:21829f4f033ac2805aa43a412bcdf60e98eee4124d565a06dee184c97efff6091\&quot;&#x60;   - Description - Image Digest. - &#x60;imageId&#x60;   - Type: string   - Example: &#x60;imageId in (\&quot;sha256:3768ff6176e29a35ce1354622977a1e5c013045cbc4f30754ef3459218be8ac\&quot;)&#x60;   - Description - Image Id. - &#x60;os&#x60;   - Type: string   - Example: &#x60;os &#x3D; \&quot;linux\&quot;&#x60;   - Description - Image OS. - &#x60;container.imageName&#x60;   - Type: string   - Example: &#x60;container.imageName in (\&quot;registry.k8s.io/kube-image:v1.2.4\&quot;)&#x60;   - Description - Image Pullstring. - &#x60;image.registry&#x60;   - Type: string   - Example: &#x60;image.registry &#x3D; \&quot;quay.io\&quot;&#x60;   - Description - Image Registry. - &#x60;image.tag&#x60;   - Type: string   - Example: &#x60;image.tag in (\&quot;tag1\&quot;)&#x60;   - Description - Image tag. - &#x60;package.inUse&#x60;   - Type: boolean   - Example: &#x60;package.inUse exists&#x60;   - Description - Package in use filter. Supported operators: exists and not exists. - &#x60;package.info&#x60;   - Type: string   - Example: &#x60;package.info in (\&quot;github.com/golang/protobuf - v1.5.2\&quot;)&#x60;   - Description - Filters by a package using the format [packge name] - [version]. - &#x60;package.path&#x60;   - Type: string   - Example: &#x60;package.path in (\&quot;/app\&quot;)&#x60;   - Description - Filters by package path. - &#x60;package.type&#x60;   - Type: string   - Example: &#x60;package.type in (\&quot;Golang\&quot;)&#x60;   - Description - Package type. - &#x60;vuln.cvssScore&#x60;   - Type: string   - Example: &#x60;vuln.cvssScore &gt;&#x3D; \&quot;3\&quot;&#x60;   - Description - Filter by vulnerability CVSS. Supported operators: &#x60;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;. - &#x60;vuln.hasExploit&#x60;   - Type: boolean   - Example: &#x60;vuln.hasExploit exists&#x60;   - Description - Filters resources by the existence of vulnerabilities with exploits. Supported operators: exists and not exists. - &#x60;vuln.hasFix&#x60;   - Type: boolean   - Example: &#x60;vuln.hasFix exists&#x60;   - Description - Filters resources by the existence of vulnerabilities with fixes. Supported operators: exists and not exists. - &#x60;vuln.name&#x60;   - Type: string   - Example: &#x60;vuln.name in (\&quot;CVE-2023-0049\&quot;)&#x60;   - Description - Filter by vulnerability name. - &#x60;vuln.severity&#x60;   - Type: string   - Example: &#x60;vuln.severity in (\&quot;Critical\&quot;)&#x60;   - Description - Filter by vulnerability severity. Supported operators: in, not in, exists and not exists. - &#x60;machineImage&#x60;   - Type: string   - Example: &#x60;machineImage &#x3D; \&quot;ami-0b22b359fdfabe1b5\&quot;&#x60;   - Description - Filter by host machine image.  **Note**: Whenever you filter for values with special characters, ensure that you encode the values. If the special characters are \&quot; or \\, use the escape character \\ and then encode the values.  | [optional] 
 **page_number** | **int**| Page number. Defaults to 1. | [optional] 
 **page_size** | **int**| Page size. Defaults to 20. | [optional] 
 **with_enriched_containers** | **bool**| If true then for kubernetes workload resources additional container information will be included. | [optional] 

### Return type

[**InventoryResourceResponse**](InventoryResourceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned Inventory v1 resources. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**400** | Operation failed due to invalid payload. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**401** | Access denied. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**403** | Not enough privileges to complete the action. |  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**429** | Too many requests. |  * Retry-After - Retry after X seconds. <br>  * X-RateLimit-Limit - Maximum number of allowed requests per minute. <br>  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

