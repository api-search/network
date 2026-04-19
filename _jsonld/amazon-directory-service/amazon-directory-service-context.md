---
class_count: 26
classes:
- Certificate
- ClientCertAuthSettings
- Computer
- ConditionalForwarder
- DirectoryConfigurationStatus
- DirectoryConnectSettings
- DirectoryConnectSettingsDescription
- DirectoryDescription
- RadiusSettings
- OwnerDirectoryDescription
- DirectoryLimits
- DirectoryVpcSettings
- DirectoryVpcSettingsDescription
- EventTopic
- IpRoute
- IpRouteInfo
- LDAPSSettingInfo
- LogSubscription
- OSUpdateSettings
- RegionDescription
- SchemaExtensionInfo
- SharedDirectory
- Snapshot
- SnapshotLimits
- Tag
- Trust
context_file: json-ld/amazon-directory-service-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/json-ld/amazon-directory-service-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Directory Service from Amazon Directory Service.
layout: jsonld
name: Amazon Directory Service Context
namespaces:
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
- prefix: ds
  uri: https://aws.amazon.com/directoryservice/vocab#
properties:
- container: ''
  name: CertificateId
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: StateReason
  type: string
- container: ''
  name: CommonName
  type: string
- container: ''
  name: RegisteredDateTime
  type: string
- container: ''
  name: ExpiryDateTime
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: OCSPUrl
  type: string
- container: ''
  name: ComputerId
  type: string
- container: ''
  name: ComputerName
  type: string
- container: ''
  name: ComputerAttributes
  type: string
- container: ''
  name: RemoteDomainName
  type: string
- container: ''
  name: DnsIpAddrs
  type: string
- container: ''
  name: ReplicationScope
  type: string
- container: ''
  name: VpcId
  type: string
- container: ''
  name: SubnetIds
  type: string
- container: ''
  name: CustomerDnsIps
  type: string
- container: ''
  name: CustomerUserName
  type: string
- container: ''
  name: SecurityGroupId
  type: string
- container: ''
  name: AvailabilityZones
  type: string
- container: ''
  name: ConnectIps
  type: string
- container: ''
  name: DirectoryId
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: ShortName
  type: string
- container: ''
  name: Size
  type: string
- container: ''
  name: Edition
  type: string
- container: ''
  name: Alias
  type: string
- container: ''
  name: AccessUrl
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: Stage
  type: string
- container: ''
  name: ShareStatus
  type: string
- container: ''
  name: ShareMethod
  type: string
- container: ''
  name: ShareNotes
  type: string
- container: ''
  name: LaunchTime
  type: string
- container: ''
  name: StageLastUpdatedDateTime
  type: string
- container: ''
  name: VpcSettings
  type: string
- container: ''
  name: ConnectSettings
  type: string
- container: ''
  name: RadiusStatus
  type: string
- container: ''
  name: StageReason
  type: string
- container: ''
  name: SsoEnabled
  type: string
- container: ''
  name: DesiredNumberOfDomainControllers
  type: string
- container: ''
  name: RegionsInfo
  type: string
- container: ''
  name: OsVersion
  type: string
- container: ''
  name: CloudOnlyDirectoriesLimit
  type: string
- container: ''
  name: CloudOnlyDirectoriesCurrentCount
  type: string
- container: ''
  name: CloudOnlyDirectoriesLimitReached
  type: string
- container: ''
  name: CloudOnlyMicrosoftADLimit
  type: string
- container: ''
  name: CloudOnlyMicrosoftADCurrentCount
  type: string
- container: ''
  name: CloudOnlyMicrosoftADLimitReached
  type: string
- container: ''
  name: ConnectedDirectoriesLimit
  type: string
- container: ''
  name: ConnectedDirectoriesCurrentCount
  type: string
- container: ''
  name: ConnectedDirectoriesLimitReached
  type: string
- container: ''
  name: TopicName
  type: string
- container: ''
  name: TopicArn
  type: string
- container: ''
  name: CreatedDateTime
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: CidrIp
  type: string
- container: ''
  name: IpRouteStatusMsg
  type: string
- container: ''
  name: AddedDateTime
  type: string
- container: ''
  name: IpRouteStatusReason
  type: string
- container: ''
  name: LDAPSStatus
  type: string
- container: ''
  name: LDAPSStatusReason
  type: string
- container: ''
  name: LastUpdatedDateTime
  type: string
- container: ''
  name: LogGroupName
  type: string
- container: ''
  name: SubscriptionCreatedDateTime
  type: string
- container: ''
  name: OSVersion
  type: string
- container: ''
  name: AccountId
  type: string
- container: ''
  name: RadiusServers
  type: string
- container: ''
  name: RadiusPort
  type: string
- container: ''
  name: RadiusTimeout
  type: string
- container: ''
  name: RadiusRetries
  type: string
- container: ''
  name: SharedSecret
  type: string
- container: ''
  name: AuthenticationProtocol
  type: string
- container: ''
  name: DisplayLabel
  type: string
- container: ''
  name: UseSameUsername
  type: string
- container: ''
  name: RegionName
  type: string
- container: ''
  name: RegionType
  type: string
- container: ''
  name: StatusLastUpdatedDateTime
  type: string
- container: ''
  name: SchemaExtensionId
  type: string
- container: ''
  name: SchemaExtensionStatus
  type: string
- container: ''
  name: SchemaExtensionStatusReason
  type: string
- container: ''
  name: StartDateTime
  type: string
- container: ''
  name: EndDateTime
  type: string
- container: ''
  name: OwnerAccountId
  type: string
- container: ''
  name: OwnerDirectoryId
  type: string
- container: ''
  name: SharedAccountId
  type: string
- container: ''
  name: SharedDirectoryId
  type: string
- container: ''
  name: SnapshotId
  type: string
- container: ''
  name: StartTime
  type: string
- container: ''
  name: ManualSnapshotsLimit
  type: string
- container: ''
  name: ManualSnapshotsCurrentCount
  type: string
- container: ''
  name: ManualSnapshotsLimitReached
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: TrustId
  type: string
- container: ''
  name: TrustType
  type: string
- container: ''
  name: TrustDirection
  type: string
- container: ''
  name: TrustState
  type: string
- container: ''
  name: StateLastUpdatedDateTime
  type: string
- container: ''
  name: TrustStateReason
  type: string
- container: ''
  name: SelectiveAuth
  type: string
property_count: 101
provider_name: Amazon Directory Service
provider_slug: amazon-directory-service
slug: amazon-directory-service-context
tags:
- Active Directory
- Authentication
- AWS
- Directory Services
- Identity Management
- JSON-LD
- Linked Data
- Semantic Web
---
