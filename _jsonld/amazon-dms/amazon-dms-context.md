---
class_count: 25
classes:
- AccountQuota
- AvailabilityZone
- Certificate
- CollectorResponse
- Connection
- DatabaseResponse
- Endpoint
- EventSubscription
- Limitation
- OrderableReplicationInstance
- PendingMaintenanceAction
- RefreshSchemasStatus
- ReplicationInstance
- ReplicationSubnetGroup
- ReplicationInstanceTaskLog
- ReplicationTask
- ReplicationTaskStats
- ReplicationTaskAssessmentResult
- ReplicationTaskAssessmentRun
- SchemaResponse
- Subnet
- SupportedEndpointType
- TableStatistics
- Tag
- VpcSecurityGroupMembership
context_file: json-ld/amazon-dms-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/json-ld/amazon-dms-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Dms from Amazon DMS.
layout: jsonld
name: Amazon Dms Context
namespaces:
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
- prefix: dms
  uri: https://aws.amazon.com/dms/vocab#
properties:
- container: ''
  name: AccountQuotaName
  type: string
- container: ''
  name: Used
  type: string
- container: ''
  name: Max
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: CertificateIdentifier
  type: string
- container: ''
  name: CertificateCreationDate
  type: string
- container: ''
  name: CertificatePem
  type: string
- container: ''
  name: CertificateWallet
  type: string
- container: ''
  name: CertificateArn
  type: string
- container: ''
  name: CertificateOwner
  type: string
- container: ''
  name: ValidFromDate
  type: string
- container: ''
  name: ValidToDate
  type: string
- container: ''
  name: SigningAlgorithm
  type: string
- container: ''
  name: KeyLength
  type: string
- container: ''
  name: CollectorReferencedId
  type: string
- container: ''
  name: CollectorName
  type: string
- container: ''
  name: CollectorVersion
  type: string
- container: ''
  name: VersionStatus
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: S3BucketName
  type: string
- container: ''
  name: ServiceAccessRoleArn
  type: string
- container: ''
  name: CollectorHealthCheck
  type: string
- container: ''
  name: LastDataReceived
  type: string
- container: ''
  name: RegisteredDate
  type: string
- container: ''
  name: CreatedDate
  type: string
- container: ''
  name: ModifiedDate
  type: string
- container: ''
  name: InventoryData
  type: string
- container: ''
  name: ReplicationInstanceArn
  type: string
- container: ''
  name: EndpointArn
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: LastFailureMessage
  type: string
- container: ''
  name: EndpointIdentifier
  type: string
- container: ''
  name: ReplicationInstanceIdentifier
  type: string
- container: ''
  name: DatabaseId
  type: string
- container: ''
  name: DatabaseName
  type: string
- container: ''
  name: IpAddress
  type: string
- container: ''
  name: NumberOfSchemas
  type: string
- container: ''
  name: Server
  type: string
- container: ''
  name: SoftwareDetails
  type: string
- container: ''
  name: Collectors
  type: string
- container: ''
  name: EndpointType
  type: string
- container: ''
  name: EngineName
  type: string
- container: ''
  name: EngineDisplayName
  type: string
- container: ''
  name: Username
  type: string
- container: ''
  name: ServerName
  type: string
- container: ''
  name: Port
  type: string
- container: ''
  name: ExtraConnectionAttributes
  type: string
- container: ''
  name: KmsKeyId
  type: string
- container: ''
  name: SslMode
  type: string
- container: ''
  name: ExternalTableDefinition
  type: string
- container: ''
  name: ExternalId
  type: string
- container: ''
  name: DynamoDbSettings
  type: string
- container: ''
  name: S3Settings
  type: string
- container: ''
  name: DmsTransferSettings
  type: string
- container: ''
  name: MongoDbSettings
  type: string
- container: ''
  name: KinesisSettings
  type: string
- container: ''
  name: KafkaSettings
  type: string
- container: ''
  name: ElasticsearchSettings
  type: string
- container: ''
  name: NeptuneSettings
  type: string
- container: ''
  name: RedshiftSettings
  type: string
- container: ''
  name: PostgreSQLSettings
  type: string
- container: ''
  name: MySQLSettings
  type: string
- container: ''
  name: OracleSettings
  type: string
- container: ''
  name: SybaseSettings
  type: string
- container: ''
  name: MicrosoftSQLServerSettings
  type: string
- container: ''
  name: IBMDb2Settings
  type: string
- container: ''
  name: DocDbSettings
  type: string
- container: ''
  name: RedisSettings
  type: string
- container: ''
  name: GcpMySQLSettings
  type: string
- container: ''
  name: CustomerAwsId
  type: string
- container: ''
  name: CustSubscriptionId
  type: string
- container: ''
  name: SnsTopicArn
  type: string
- container: ''
  name: SubscriptionCreationTime
  type: string
- container: ''
  name: SourceType
  type: string
- container: ''
  name: SourceIdsList
  type: string
- container: ''
  name: EventCategoriesList
  type: string
- container: ''
  name: Enabled
  type: string
- container: ''
  name: Impact
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: EngineVersion
  type: string
- container: ''
  name: ReplicationInstanceClass
  type: string
- container: ''
  name: StorageType
  type: string
- container: ''
  name: MinAllocatedStorage
  type: string
- container: ''
  name: MaxAllocatedStorage
  type: string
- container: ''
  name: DefaultAllocatedStorage
  type: string
- container: ''
  name: IncludedAllocatedStorage
  type: string
- container: ''
  name: AvailabilityZones
  type: string
- container: ''
  name: ReleaseStatus
  type: string
- container: ''
  name: Action
  type: string
- container: ''
  name: AutoAppliedAfterDate
  type: string
- container: ''
  name: ForcedApplyDate
  type: string
- container: ''
  name: OptInStatus
  type: string
- container: ''
  name: CurrentApplyDate
  type: string
- container: ''
  name: LastRefreshDate
  type: string
- container: ''
  name: ReplicationInstanceStatus
  type: string
- container: ''
  name: AllocatedStorage
  type: string
- container: ''
  name: InstanceCreateTime
  type: string
- container: ''
  name: VpcSecurityGroups
  type: string
- container: ''
  name: PreferredMaintenanceWindow
  type: string
- container: ''
  name: PendingModifiedValues
  type: string
- container: ''
  name: MultiAZ
  type: string
- container: ''
  name: AutoMinorVersionUpgrade
  type: string
- container: ''
  name: ReplicationInstancePublicIpAddress
  type: string
- container: ''
  name: ReplicationInstancePrivateIpAddress
  type: string
- container: ''
  name: ReplicationInstancePublicIpAddresses
  type: string
- container: ''
  name: ReplicationInstancePrivateIpAddresses
  type: string
- container: ''
  name: ReplicationInstanceIpv6Addresses
  type: string
- container: ''
  name: PubliclyAccessible
  type: string
- container: ''
  name: SecondaryAvailabilityZone
  type: string
- container: ''
  name: FreeUntil
  type: string
- container: ''
  name: DnsNameServers
  type: string
- container: ''
  name: NetworkType
  type: string
- container: ''
  name: ReplicationTaskName
  type: string
- container: ''
  name: ReplicationTaskArn
  type: string
- container: ''
  name: ReplicationInstanceTaskLogSize
  type: string
- container: ''
  name: ReplicationSubnetGroupIdentifier
  type: string
- container: ''
  name: ReplicationSubnetGroupDescription
  type: string
- container: ''
  name: VpcId
  type: string
- container: ''
  name: SubnetGroupStatus
  type: string
- container: ''
  name: Subnets
  type: string
- container: ''
  name: SupportedNetworkTypes
  type: string
- container: ''
  name: ReplicationTaskIdentifier
  type: string
- container: ''
  name: SourceEndpointArn
  type: string
- container: ''
  name: TargetEndpointArn
  type: string
- container: ''
  name: MigrationType
  type: string
- container: ''
  name: TableMappings
  type: string
- container: ''
  name: ReplicationTaskSettings
  type: string
- container: ''
  name: StopReason
  type: string
- container: ''
  name: ReplicationTaskCreationDate
  type: string
- container: ''
  name: ReplicationTaskStartDate
  type: string
- container: ''
  name: CdcStartPosition
  type: string
- container: ''
  name: CdcStopPosition
  type: string
- container: ''
  name: RecoveryCheckpoint
  type: string
- container: ''
  name: TaskData
  type: string
- container: ''
  name: TargetReplicationInstanceArn
  type: string
- container: ''
  name: ReplicationTaskLastAssessmentDate
  type: string
- container: ''
  name: AssessmentStatus
  type: string
- container: ''
  name: AssessmentResultsFile
  type: string
- container: ''
  name: AssessmentResults
  type: string
- container: ''
  name: S3ObjectUrl
  type: string
- container: ''
  name: ReplicationTaskAssessmentRunArn
  type: string
- container: ''
  name: ReplicationTaskAssessmentRunCreationDate
  type: string
- container: ''
  name: AssessmentProgress
  type: string
- container: ''
  name: ResultLocationBucket
  type: string
- container: ''
  name: ResultLocationFolder
  type: string
- container: ''
  name: ResultEncryptionMode
  type: string
- container: ''
  name: ResultKmsKeyArn
  type: string
- container: ''
  name: AssessmentRunName
  type: string
- container: ''
  name: FullLoadProgressPercent
  type: string
- container: ''
  name: ElapsedTimeMillis
  type: string
- container: ''
  name: TablesLoaded
  type: string
- container: ''
  name: TablesLoading
  type: string
- container: ''
  name: TablesQueued
  type: string
- container: ''
  name: TablesErrored
  type: string
- container: ''
  name: FreshStartDate
  type: string
- container: ''
  name: StartDate
  type: string
- container: ''
  name: StopDate
  type: string
- container: ''
  name: FullLoadStartDate
  type: string
- container: ''
  name: FullLoadFinishDate
  type: string
- container: ''
  name: CodeLineCount
  type: string
- container: ''
  name: CodeSize
  type: string
- container: ''
  name: Complexity
  type: string
- container: ''
  name: DatabaseInstance
  type: string
- container: ''
  name: SchemaId
  type: string
- container: ''
  name: SchemaName
  type: string
- container: ''
  name: OriginalSchema
  type: string
- container: ''
  name: Similarity
  type: string
- container: ''
  name: SubnetIdentifier
  type: string
- container: ''
  name: SubnetAvailabilityZone
  type: string
- container: ''
  name: SubnetStatus
  type: string
- container: ''
  name: SupportsCDC
  type: string
- container: ''
  name: ReplicationInstanceEngineMinimumVersion
  type: string
- container: ''
  name: TableName
  type: string
- container: ''
  name: Inserts
  type: string
- container: ''
  name: Deletes
  type: string
- container: ''
  name: Updates
  type: string
- container: ''
  name: Ddls
  type: string
- container: ''
  name: AppliedInserts
  type: string
- container: ''
  name: AppliedDeletes
  type: string
- container: ''
  name: AppliedUpdates
  type: string
- container: ''
  name: AppliedDdls
  type: string
- container: ''
  name: FullLoadRows
  type: string
- container: ''
  name: FullLoadCondtnlChkFailedRows
  type: string
- container: ''
  name: FullLoadErrorRows
  type: string
- container: ''
  name: FullLoadStartTime
  type: string
- container: ''
  name: FullLoadEndTime
  type: string
- container: ''
  name: FullLoadReloaded
  type: string
- container: ''
  name: LastUpdateTime
  type: string
- container: ''
  name: TableState
  type: string
- container: ''
  name: ValidationPendingRecords
  type: string
- container: ''
  name: ValidationFailedRecords
  type: string
- container: ''
  name: ValidationSuspendedRecords
  type: string
- container: ''
  name: ValidationState
  type: string
- container: ''
  name: ValidationStateDetails
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: ResourceArn
  type: string
- container: ''
  name: VpcSecurityGroupId
  type: string
property_count: 198
provider_name: Amazon DMS
provider_slug: amazon-dms
slug: amazon-dms-context
tags:
- AWS
- Data Replication
- Database
- Database Migration
- Migration
- JSON-LD
- Linked Data
- Semantic Web
---
