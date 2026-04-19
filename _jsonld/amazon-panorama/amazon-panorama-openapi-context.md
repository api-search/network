---
class_count: 169
classes:
- AccessDeniedException
- AlternateSoftwareMetadata
- ApplicationInstance
- ApplicationInstanceArn
- ApplicationInstanceHealthStatus
- ApplicationInstanceName
- ApplicationInstanceStatus
- ApplicationInstanceStatusDescription
- Boolean
- ConflictException
- CreateApplicationInstanceRequest
- CreateApplicationInstanceResponse
- CreateJobForDevicesRequest
- CreateJobForDevicesResponse
- CreateNodeFromTemplateJobRequest
- CreateNodeFromTemplateJobResponse
- CreatePackageImportJobRequest
- CreatePackageImportJobResponse
- CreatePackageRequest
- CreatePackageResponse
- DeleteDeviceRequest
- DeleteDeviceResponse
- DeletePackageRequest
- DeletePackageResponse
- DeregisterPackageVersionRequest
- DeregisterPackageVersionResponse
- DescribeApplicationInstanceDetailsRequest
- DescribeApplicationInstanceDetailsResponse
- DescribeApplicationInstanceRequest
- DescribeApplicationInstanceResponse
- DescribeDeviceJobRequest
- DescribeDeviceJobResponse
- DescribeDeviceRequest
- DescribeDeviceResponse
- DescribeNodeFromTemplateJobRequest
- DescribeNodeFromTemplateJobResponse
- DescribeNodeRequest
- DescribeNodeResponse
- DescribePackageImportJobRequest
- DescribePackageImportJobResponse
- DescribePackageRequest
- DescribePackageResponse
- DescribePackageVersionRequest
- DescribePackageVersionResponse
- Device
- DeviceBrand
- DeviceIdList
- DeviceJob
- DeviceJobList
- DeviceList
- DeviceSerialNumber
- DeviceStatus
- DnsList
- EthernetPayload
- EthernetStatus
- InputPortList
- InternalServerException
- IpAddressOrServerName
- Job
- JobList
- JobResourceTags
- JobResourceType
- JobTagsList
- ListApplicationInstanceDependenciesRequest
- ListApplicationInstanceDependenciesResponse
- ListApplicationInstanceNodeInstancesRequest
- ListApplicationInstanceNodeInstancesResponse
- ListApplicationInstancesRequest
- ListApplicationInstancesResponse
- ListDevicesJobsRequest
- ListDevicesJobsResponse
- ListDevicesRequest
- ListDevicesResponse
- ListDevicesSortBy
- ListNodeFromTemplateJobsRequest
- ListNodeFromTemplateJobsResponse
- ListNodesRequest
- ListNodesResponse
- ListPackageImportJobsRequest
- ListPackageImportJobsResponse
- ListPackagesRequest
- ListPackagesResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- ManifestOverridesPayloadData
- ManifestPayloadData
- MarkLatestPatch
- MaxSize25
- NameFilter
- NetworkConnectionStatus
- NetworkPayload
- NetworkStatus
- Node
- NodeAssetName
- NodeCategory
- NodeFromTemplateJob
- NodeFromTemplateJobList
- NodeFromTemplateJobStatus
- NodeFromTemplateJobStatusMessage
- NodeInputPort
- NodeInstance
- NodeInstanceStatus
- NodeOutputPort
- NodePackageArn
- NodePackageId
- NodePackageName
- NodePackagePatchVersion
- NodePackageVersion
- NodeSignal
- NodeSignalList
- NodeSignalValue
- NodesList
- NtpPayload
- NtpServerList
- Object
- OutPutS3Location
- OutputPortList
- PackageImportJob
- PackageImportJobInputConfig
- PackageImportJobList
- PackageImportJobOutput
- PackageImportJobOutputConfig
- PackageImportJobStatus
- PackageImportJobStatusMessage
- PackageImportJobType
- PackageList
- PackageListItem
- PackageObject
- PackageOwnerAccount
- PackageVersionStatus
- PackageVersionStatusDescription
- PortDefaultValue
- PortName
- PortType
- PrincipalArn
- PrincipalArnsList
- ProvisionDeviceRequest
- ProvisionDeviceResponse
- RegisterPackageVersionRequest
- RegisterPackageVersionResponse
- RemoveApplicationInstanceRequest
- RemoveApplicationInstanceResponse
- ReportedRuntimeContextState
- ReportedRuntimeContextStates
- ResourceArn
- ResourceNotFoundException
- ServiceQuotaExceededException
- SignalApplicationInstanceNodeInstancesRequest
- SignalApplicationInstanceNodeInstancesResponse
- SortOrder
- StatusFilter
- TagKey
- TagKeyList
- TagMap
- TagResourceRequest
- TagResourceResponse
- TagValue
- TemplateKey
- TemplateParametersMap
- TemplateValue
- TimeStamp
- Token
- UntagResourceRequest
- UntagResourceResponse
- UpdateCreatedTime
- UpdateDeviceMetadataRequest
- UpdateDeviceMetadataResponse
- UpdateProgress
- ValidationException
context_file: json-ld/amazon-panorama-openapi-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-panorama/refs/heads/main/json-ld/amazon-panorama-openapi-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Panorama Openapi from Amazon Panorama.
layout: jsonld
name: Amazon Panorama Openapi Context
namespaces:
- prefix: panorama
  uri: https://panorama.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AlternateSoftwares
  type: string
- container: ''
  name: ApplicationInstanceId
  type: string
- container: ''
  name: ApplicationInstances
  type: string
- container: ''
  name: Bucket
  type: string
- container: ''
  name: BucketName
  type: string
- container: ''
  name: Certificates
  type: string
- container: ''
  name: ClientToken
  type: string
- container: ''
  name: ConnectionType
  type: string
- container: ''
  name: CreatedTime
  type: string
- container: ''
  name: CurrentSoftware
  type: string
- container: ''
  name: DefaultGateway
  type: string
- container: ''
  name: DefaultRuntimeContextDevice
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: DesiredState
  type: string
- container: ''
  name: DeviceAggregatedStatus
  type: string
- container: ''
  name: DeviceArn
  type: string
- container: ''
  name: DeviceConnectionStatus
  type: string
- container: ''
  name: DeviceId
  type: string
- container: ''
  name: DeviceJobConfig
  type: string
- container: ''
  name: DeviceName
  type: string
- container: ''
  name: DeviceReportedStatus
  type: string
- container: ''
  name: DeviceType
  type: string
- container: ''
  name: Dns
  type: string
- container: ''
  name: HwAddress
  type: string
- container: ''
  name: ImageVersion
  type: string
- container: ''
  name: IotThingName
  type: string
- container: ''
  name: IpAddress
  type: string
- container: ''
  name: JobId
  type: string
- container: ''
  name: JobType
  type: string
- container: ''
  name: LastUpdatedTime
  type: string
- container: ''
  name: LatestAlternateSoftware
  type: string
- container: ''
  name: LatestDeviceJob
  type: string
- container: ''
  name: LatestSoftware
  type: string
- container: ''
  name: LeaseExpirationTime
  type: string
- container: ''
  name: ManifestOverridesPayload
  type: string
- container: ''
  name: ManifestPayload
  type: string
- container: ''
  name: Mask
  type: string
- container: ''
  name: MaxConnections
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: NodeId
  type: string
- container: ''
  name: NodeInstanceId
  type: string
- container: ''
  name: NodeInstances
  type: string
- container: ''
  name: NodeInterface
  type: string
- container: ''
  name: NodeName
  type: string
- container: ''
  name: NtpServerName
  type: string
- container: ''
  name: NtpStatus
  type: string
- container: ''
  name: OTAJobConfig
  type: string
- container: ''
  name: ObjectKey
  type: string
- container: ''
  name: PackageObjects
  type: string
- container: ''
  name: PackageVersionInputConfig
  type: string
- container: ''
  name: PackageVersionOutputConfig
  type: string
- container: ''
  name: Region
  type: string
- container: ''
  name: RuntimeContextName
  type: string
- container: ''
  name: RuntimeRoleArn
  type: string
- container: ''
  name: S3Location
  type: string
- container: ''
  name: StaticIpConnectionInfo
  type: string
- container: ''
  name: StorageLocation
  type: string
- container: ''
  name: TemplateType
  type: string
- container: ''
  name: Version
  type: string
- container: ''
  name: AllowMajorVersionUpdate
  type: string
- container: ''
  name: ApplicationInstanceIdToReplace
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: AssetName
  type: string
- container: ''
  name: BinaryPrefixLocation
  type: string
- container: ''
  name: Brand
  type: string
- container: ''
  name: Category
  type: string
- container: ''
  name: ConnectionStatus
  type: string
- container: ''
  name: CurrentNetworkingStatus
  type: string
- container: ''
  name: CurrentStatus
  type: string
- container: ''
  name: DefaultRuntimeContextDeviceName
  type: string
- container: ''
  name: DefaultValue
  type: string
- container: ''
  name: DeviceIds
  type: string
- container: ''
  name: DeviceJobs
  type: string
- container: ''
  name: DeviceReportedTime
  type: string
- container: ''
  name: Devices
  type: string
- container: ''
  name: Ethernet0
  type: string
- container: ''
  name: Ethernet0Status
  type: string
- container: ''
  name: Ethernet1
  type: string
- container: ''
  name: Ethernet1Status
  type: string
- container: ''
  name: GeneratedPrefixLocation
  type: string
- container: ''
  name: HealthStatus
  type: string
- container: ''
  name: InputConfig
  type: string
- container: ''
  name: Inputs
  type: string
- container: ''
  name: IsLatestPatch
  type: string
- container: ''
  name: JobTags
  type: string
- container: ''
  name: Jobs
  type: string
- container: ''
  name: ManifestPrefixLocation
  type: string
- container: ''
  name: MarkLatest
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: NetworkingConfiguration
  type: string
- container: ''
  name: NodeDescription
  type: string
- container: ''
  name: NodeFromTemplateJobs
  type: string
- container: ''
  name: NodeSignals
  type: string
- container: ''
  name: Nodes
  type: string
- container: ''
  name: Ntp
  type: string
- container: ''
  name: NtpServers
  type: string
- container: ''
  name: Output
  type: string
- container: ''
  name: OutputConfig
  type: string
- container: ''
  name: OutputPackageName
  type: string
- container: ''
  name: OutputPackageVersion
  type: string
- container: ''
  name: OutputS3Location
  type: string
- container: ''
  name: Outputs
  type: string
- container: ''
  name: OwnerAccount
  type: string
- container: ''
  name: PackageArn
  type: string
- container: ''
  name: PackageId
  type: string
- container: ''
  name: PackageImportJobs
  type: string
- container: ''
  name: PackageName
  type: string
- container: ''
  name: PackagePatchVersion
  type: string
- container: ''
  name: PackageVersion
  type: string
- container: ''
  name: Packages
  type: string
- container: ''
  name: PatchVersion
  type: string
- container: ''
  name: PayloadData
  type: string
- container: ''
  name: ProvisioningStatus
  type: string
- container: ''
  name: ReadAccessPrincipalArns
  type: string
- container: ''
  name: RegisteredTime
  type: string
- container: ''
  name: RepoPrefixLocation
  type: string
- container: ''
  name: ResourceType
  type: string
- container: ''
  name: RuntimeContextStates
  type: string
- container: ''
  name: SerialNumber
  type: string
- container: ''
  name: Signal
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: StatusDescription
  type: string
- container: ''
  name: StatusMessage
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: TemplateParameters
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: WriteAccessPrincipalArns
  type: string
property_count: 127
provider_name: Amazon Panorama
provider_slug: amazon-panorama
slug: amazon-panorama-openapi-context
tags:
- AWS
- Cameras
- Computer Vision
- Edge ML
- Industrial IoT
- JSON-LD
- Linked Data
- Semantic Web
---
