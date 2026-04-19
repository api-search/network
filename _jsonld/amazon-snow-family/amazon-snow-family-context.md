---
class_count: 77
classes:
- UpdateJobShipmentStateRequest
- ListCompatibleImagesResult
- GetSnowballUsageRequest
- TGWOnDeviceServiceConfiguration
- ClusterListEntry
- UpdateLongTermPricingResult
- CancelJobRequest
- Ec2AmiResource
- NFSOnDeviceServiceConfiguration
- CreateReturnShippingLabelRequest
- UpdateClusterRequest
- DescribeAddressRequest
- CreateLongTermPricingResult
- ListJobsRequest
- DependentService
- ListCompatibleImagesRequest
- ListServiceVersionsResult
- LambdaResource
- GetSoftwareUpdatesResult
- CancelClusterRequest
- GetJobManifestRequest
- CancelJobResult
- CancelClusterResult
- DescribeReturnShippingLabelRequest
- ListLongTermPricingRequest
- DescribeJobRequest
- DescribeReturnShippingLabelResult
- ListPickupLocationsResult
- DataTransfer
- ListClustersResult
- ListClusterJobsRequest
- DescribeAddressesResult
- GetJobUnlockCodeResult
- CreateClusterRequest
- GetSnowballUsageResult
- GetJobUnlockCodeRequest
- UpdateClusterResult
- DescribeAddressesRequest
- ListClusterJobsResult
- S3Resource
- CreateClusterResult
- CreateAddressResult
- CreateJobResult
- TargetOnDeviceService
- DescribeClusterRequest
- CreateJobRequest
- Shipment
- DescribeAddressResult
- S3OnDeviceServiceConfiguration
- DescribeClusterResult
- CreateLongTermPricingRequest
- UpdateJobShipmentStateResult
- CreateReturnShippingLabelResult
- LongTermPricingListEntry
- ListServiceVersionsRequest
- JobLogs
- INDTaxDocuments
- JobListEntry
- UpdateLongTermPricingRequest
- CreateAddressRequest
- GetJobManifestResult
- EventTriggerDefinition
- EKSOnDeviceServiceConfiguration
- GetSoftwareUpdatesRequest
- ListLongTermPricingResult
- UpdateJobRequest
- DescribeJobResult
- ListClustersRequest
- ListJobsResult
- UpdateJobResult
- CompatibleImage
- JobResource
- ListPickupLocationsRequest
- Description
- Name
- Email
- Version
context_file: json-ld/amazon-snow-family-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-snow-family/refs/heads/main/json-ld/amazon-snow-family-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Snow Family from Amazon Snow Family.
layout: jsonld
name: Amazon Snow Family Context
namespaces:
- prefix: aws
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: PickupDetails
  type: string
- container: ''
  name: ClusterMetadata
  type: string
- container: ''
  name: DeviceConfiguration
  type: string
- container: ''
  name: TaxDocuments
  type: string
- container: ''
  name: JobMetadata
  type: string
- container: ''
  name: WirelessConnection
  type: string
- container: ''
  name: SnowconeDeviceConfiguration
  type: string
- container: ''
  name: Address
  type: string
- container: ''
  name: KeyRange
  type: string
- container: ''
  name: ShippingDetails
  type: string
- container: ''
  name: OnDeviceServiceConfiguration
  type: string
- container: ''
  name: ServiceVersion
  type: string
- container: ''
  name: Notification
  type: string
- container: ''
  name: JobId
  type: string
- container: ''
  name: ShipmentState
  type: string
- container: ''
  name: CompatibleImages
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: StorageLimit
  type: string
- container: ''
  name: StorageUnit
  type: string
- container: ''
  name: ClusterId
  type: string
- container: ''
  name: ClusterState
  type: string
- container: ''
  name: CreationDate
  type: string
- container: ''
  name: AmiId
  type: string
- container: ''
  name: SnowballAmiId
  type: string
- container: ''
  name: ShippingOption
  type: string
- container: ''
  name: RoleARN
  type: string
- container: ''
  name: Resources
  type: string
- container: ''
  name: AddressId
  type: string
- container: ''
  name: ForwardingAddressId
  type: string
- container: ''
  name: LongTermPricingId
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: ServiceName
  type: string
- container: ''
  name: ServiceVersions
  type: string
- container: ''
  name: DependentServices
  type: string
- container: ''
  name: LambdaArn
  type: string
- container: ''
  name: EventTriggers
  type: string
- container: ''
  name: UpdatesURI
  type: string
- container: ''
  name: PhoneNumber
  type: string
- container: ''
  name: IdentificationNumber
  type: string
- container: ''
  name: IdentificationExpirationDate
  type: string
- container: ''
  name: IdentificationIssuingOrg
  type: string
- container: ''
  name: DevicePickupId
  type: string
- container: ''
  name: KmsKeyARN
  type: string
- container: ''
  name: JobType
  type: string
- container: ''
  name: SnowballType
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: ExpirationDate
  type: string
- container: ''
  name: ReturnShippingLabelURI
  type: string
- container: ''
  name: Addresses
  type: string
- container: ''
  name: BytesTransferred
  type: string
- container: ''
  name: ObjectsTransferred
  type: string
- container: ''
  name: TotalBytes
  type: string
- container: ''
  name: TotalObjects
  type: string
- container: ''
  name: ClusterListEntries
  type: string
- container: ''
  name: UnlockCode
  type: string
- container: ''
  name: RemoteManagement
  type: string
- container: ''
  name: InitialClusterSize
  type: string
- container: ''
  name: ForceCreateJobs
  type: string
- container: ''
  name: LongTermPricingIds
  type: string
- container: ''
  name: SnowballCapacityPreference
  type: string
- container: ''
  name: SnowballLimit
  type: string
- container: ''
  name: SnowballsInUse
  type: string
- container: ''
  name: IND
  type: string
- container: ''
  name: JobState
  type: string
- container: ''
  name: DataTransferProgress
  type: string
- container: ''
  name: JobLogInfo
  type: string
- container: ''
  name: ImpactLevel
  type: string
- container: ''
  name: SnowballId
  type: string
- container: ''
  name: JobListEntries
  type: string
- container: ''
  name: BucketArn
  type: string
- container: ''
  name: TargetOnDeviceServices
  type: string
- container: ''
  name: TransferOption
  type: string
- container: ''
  name: TrackingNumber
  type: string
- container: ''
  name: IsWifiEnabled
  type: string
- container: ''
  name: ServiceSize
  type: string
- container: ''
  name: FaultTolerance
  type: string
- container: ''
  name: LongTermPricingType
  type: string
- container: ''
  name: IsLongTermPricingAutoRenew
  type: string
- container: ''
  name: Company
  type: string
- container: ''
  name: Street1
  type: string
- container: ''
  name: Street2
  type: string
- container: ''
  name: Street3
  type: string
- container: ''
  name: City
  type: string
- container: ''
  name: StateOrProvince
  type: string
- container: ''
  name: PrefectureOrDistrict
  type: string
- container: ''
  name: Landmark
  type: string
- container: ''
  name: Country
  type: string
- container: ''
  name: PostalCode
  type: string
- container: ''
  name: IsRestricted
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: LongTermPricingEndDate
  type: string
- container: ''
  name: LongTermPricingStartDate
  type: string
- container: ''
  name: CurrentActiveJob
  type: string
- container: ''
  name: ReplacementJob
  type: string
- container: ''
  name: LongTermPricingStatus
  type: string
- container: ''
  name: JobIds
  type: string
- container: ''
  name: BeginMarker
  type: string
- container: ''
  name: EndMarker
  type: string
- container: ''
  name: JobCompletionReportURI
  type: string
- container: ''
  name: JobSuccessLogURI
  type: string
- container: ''
  name: JobFailureLogURI
  type: string
- container: ''
  name: GSTIN
  type: string
- container: ''
  name: IsMaster
  type: string
- container: ''
  name: InboundShipment
  type: string
- container: ''
  name: OutboundShipment
  type: string
- container: ''
  name: NFSOnDeviceService
  type: string
- container: ''
  name: TGWOnDeviceService
  type: string
- container: ''
  name: EKSOnDeviceService
  type: string
- container: ''
  name: S3OnDeviceService
  type: string
- container: ''
  name: ManifestURI
  type: string
- container: ''
  name: EventResourceARN
  type: string
- container: ''
  name: KubernetesVersion
  type: string
- container: ''
  name: EKSAnywhereVersion
  type: string
- container: ''
  name: LongTermPricingEntries
  type: string
- container: ''
  name: SubJobMetadata
  type: string
- container: ''
  name: SnsTopicARN
  type: string
- container: ''
  name: JobStatesToNotify
  type: string
- container: ''
  name: NotifyAll
  type: string
- container: ''
  name: DevicePickupSnsTopicARN
  type: string
- container: ''
  name: S3Resources
  type: string
- container: ''
  name: LambdaResources
  type: string
- container: ''
  name: Ec2AmiResources
  type: string
property_count: 122
provider_name: Amazon Snow Family
provider_slug: amazon-snow-family
slug: amazon-snow-family-context
tags:
- AWS
- Data Migration
- Edge Computing
- Offline Transfer
- Physical Appliance
- JSON-LD
- Linked Data
- Semantic Web
---
