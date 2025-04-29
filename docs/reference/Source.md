# Source

Source of the event: - `syscall` - a syscall within a workload - `windows` - Windows event log - `profiling` - ML workload threat detections - `K8SAdmissionController` - Admission control request coming from the Kubernetes admission controller - `k8s_audit` - Kubernetes audit logs, if the category is `runtime`, otherwise Admission control request - `aws_cloudtrail` - AWS CloudTrail log, from CloudConnector - `awscloudtrail` - AWS CloudTrail log, agentless only - `agentless-aws-ml` - ML threat detections for AWS - `gcp_auditlog` - GCP Audit log - `azure_platformlogs` - Azure platform logs - `okta` - Okta System Logs - `agentless-okta-ml` - ML threat detections for Okta - `github` - Github organization logs 

## Enum

* `SYSCALL` (value: `'syscall'`)

* `WINDOWS` (value: `'windows'`)

* `PROFILING` (value: `'profiling'`)

* `K8SADMISSIONCONTROLLER` (value: `'K8SAdmissionController'`)

* `K8S_AUDIT` (value: `'k8s_audit'`)

* `AWS_CLOUDTRAIL` (value: `'aws_cloudtrail'`)

* `AWSCLOUDTRAIL` (value: `'awscloudtrail'`)

* `AGENTLESS_MINUS_AWS_MINUS_ML` (value: `'agentless-aws-ml'`)

* `GCP_AUDITLOG` (value: `'gcp_auditlog'`)

* `AZURE_PLATFORMLOGS` (value: `'azure_platformlogs'`)

* `OKTA` (value: `'okta'`)

* `AGENTLESS_MINUS_OKTA_MINUS_ML` (value: `'agentless-okta-ml'`)

* `GITHUB` (value: `'github'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


