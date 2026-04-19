---
class_count: 175
classes:
- AssociateConnectionAliasResult
- AssociateConnectionAliasRequest
- AssociateIpGroupsResult
- AssociateIpGroupsRequest
- AuthorizeIpRulesResult
- AuthorizeIpRulesRequest
- CopyWorkspaceImageResult
- CopyWorkspaceImageRequest
- CreateConnectClientAddInResult
- CreateConnectClientAddInRequest
- CreateConnectionAliasResult
- CreateConnectionAliasRequest
- CreateIpGroupResult
- CreateIpGroupRequest
- CreateStandbyWorkspacesResult
- CreateStandbyWorkspacesRequest
- CreateTagsResult
- CreateTagsRequest
- CreateUpdatedWorkspaceImageResult
- CreateUpdatedWorkspaceImageRequest
- CreateWorkspaceBundleResult
- WorkspaceBundle
- CreateWorkspaceBundleRequest
- ComputeType
- UserStorage
- RootStorage
- CreateWorkspaceImageResult
- OperatingSystem
- CreateWorkspaceImageRequest
- CreateWorkspacesResult
- CreateWorkspacesRequest
- DeleteClientBrandingResult
- DeleteClientBrandingRequest
- DeleteConnectClientAddInResult
- DeleteConnectClientAddInRequest
- DeleteConnectionAliasResult
- DeleteConnectionAliasRequest
- DeleteIpGroupResult
- DeleteIpGroupRequest
- DeleteTagsResult
- DeleteTagsRequest
- DeleteWorkspaceBundleResult
- DeleteWorkspaceBundleRequest
- DeleteWorkspaceImageResult
- DeleteWorkspaceImageRequest
- DeregisterWorkspaceDirectoryResult
- DeregisterWorkspaceDirectoryRequest
- DescribeAccountResult
- DescribeAccountRequest
- DescribeAccountModificationsResult
- DescribeAccountModificationsRequest
- DescribeClientBrandingResult
- DescribeClientBrandingRequest
- DescribeClientPropertiesResult
- DescribeClientPropertiesRequest
- DescribeConnectClientAddInsResult
- DescribeConnectClientAddInsRequest
- DescribeConnectionAliasPermissionsResult
- DescribeConnectionAliasPermissionsRequest
- DescribeConnectionAliasesResult
- DescribeConnectionAliasesRequest
- DescribeIpGroupsResult
- DescribeIpGroupsRequest
- DescribeTagsResult
- DescribeTagsRequest
- DescribeWorkspaceBundlesResult
- DescribeWorkspaceBundlesRequest
- DescribeWorkspaceDirectoriesResult
- DescribeWorkspaceDirectoriesRequest
- DescribeWorkspaceImagePermissionsResult
- DescribeWorkspaceImagePermissionsRequest
- DescribeWorkspaceImagesResult
- DescribeWorkspaceImagesRequest
- DescribeWorkspaceSnapshotsResult
- DescribeWorkspaceSnapshotsRequest
- DescribeWorkspacesResult
- DescribeWorkspacesRequest
- DescribeWorkspacesConnectionStatusResult
- DescribeWorkspacesConnectionStatusRequest
- DisassociateConnectionAliasResult
- DisassociateConnectionAliasRequest
- DisassociateIpGroupsResult
- DisassociateIpGroupsRequest
- ImportClientBrandingResult
- ImportClientBrandingRequest
- ImportWorkspaceImageResult
- ImportWorkspaceImageRequest
- ListAvailableManagementCidrRangesResult
- ListAvailableManagementCidrRangesRequest
- MigrateWorkspaceResult
- MigrateWorkspaceRequest
- ModifyAccountResult
- ModifyAccountRequest
- ModifyCertificateBasedAuthPropertiesResult
- ModifyCertificateBasedAuthPropertiesRequest
- CertificateBasedAuthProperties
- ModifyClientPropertiesResult
- ModifyClientPropertiesRequest
- ClientProperties
- ModifySamlPropertiesResult
- ModifySamlPropertiesRequest
- SamlProperties
- ModifySelfservicePermissionsResult
- ModifySelfservicePermissionsRequest
- SelfservicePermissions
- ModifyWorkspaceAccessPropertiesResult
- ModifyWorkspaceAccessPropertiesRequest
- WorkspaceAccessProperties
- ModifyWorkspaceCreationPropertiesResult
- ModifyWorkspaceCreationPropertiesRequest
- WorkspaceCreationProperties
- ModifyWorkspacePropertiesResult
- ModifyWorkspacePropertiesRequest
- WorkspaceProperties
- ModifyWorkspaceStateResult
- ModifyWorkspaceStateRequest
- RebootWorkspacesResult
- RebootWorkspacesRequest
- RebuildWorkspacesResult
- RebuildWorkspacesRequest
- RegisterWorkspaceDirectoryResult
- RegisterWorkspaceDirectoryRequest
- RestoreWorkspaceResult
- RestoreWorkspaceRequest
- RevokeIpRulesResult
- RevokeIpRulesRequest
- StartWorkspacesResult
- StartWorkspacesRequest
- StopWorkspacesResult
- StopWorkspacesRequest
- TerminateWorkspacesResult
- TerminateWorkspacesRequest
- UpdateConnectClientAddInResult
- UpdateConnectClientAddInRequest
- UpdateConnectionAliasPermissionResult
- UpdateConnectionAliasPermissionRequest
- ConnectionAliasPermission
- UpdateRulesOfIpGroupResult
- UpdateRulesOfIpGroupRequest
- UpdateWorkspaceBundleResult
- UpdateWorkspaceBundleRequest
- UpdateWorkspaceImagePermissionResult
- UpdateWorkspaceImagePermissionRequest
- AccountModification
- ModificationState
- ClientPropertiesResult
- ConnectClientAddIn
- ConnectionAlias
- ConnectionAliasAssociation
- DefaultClientBrandingAttributes
- DefaultImportClientBrandingAttributes
- DefaultWorkspaceCreationProperties
- IosClientBrandingAttributes
- WorkspaceDirectory
- StandbyWorkspace
- FailedCreateStandbyWorkspacesRequest
- FailedCreateWorkspaceRequest
- FailedWorkspaceChangeRequest
- ImagePermission
- IosImportClientBrandingAttributes
- IpRuleItem
- PendingCreateStandbyWorkspacesRequest
- RebootRequest
- RebuildRequest
- RelatedWorkspaceProperties
- Snapshot
- StartRequest
- StopRequest
- Tag
- TerminateRequest
- UpdateResult
- Workspace
- WorkspaceConnectionStatus
- WorkspaceImage
- WorkspacesIpGroup
context_file: json-ld/amazon-workspaces-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-workspaces/refs/heads/main/json-ld/amazon-workspaces-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Workspaces from Amazon WorkSpaces.
layout: jsonld
name: Amazon Workspaces Context
namespaces:
- prefix: amz
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ConnectionIdentifier
  type: string
- container: ''
  name: AliasId
  type: string
- container: ''
  name: ResourceId
  type: string
- container: ''
  name: DirectoryId
  type: string
- container: ''
  name: GroupIds
  type: string
- container: ''
  name: GroupId
  type: string
- container: ''
  name: UserRules
  type: string
- container: ''
  name: ImageId
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: SourceImageId
  type: string
- container: ''
  name: SourceRegion
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: AddInId
  type: string
- container: ''
  name: URL
  type: string
- container: ''
  name: ConnectionString
  type: string
- container: ''
  name: GroupName
  type: string
- container: ''
  name: GroupDesc
  type: string
- container: ''
  name: FailedStandbyRequests
  type: string
- container: ''
  name: PendingStandbyRequests
  type: string
- container: ''
  name: PrimaryRegion
  type: string
- container: ''
  name: StandbyWorkspaces
  type: string
- container: ''
  name: BundleName
  type: string
- container: ''
  name: BundleDescription
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: RequiredTenancy
  type: string
- container: ''
  name: Created
  type: string
- container: ''
  name: OwnerAccountId
  type: string
- container: ''
  name: WorkspaceId
  type: string
- container: ''
  name: FailedRequests
  type: string
- container: ''
  name: PendingRequests
  type: string
- container: ''
  name: Workspaces
  type: string
- container: ''
  name: Platforms
  type: string
- container: ''
  name: TagKeys
  type: string
- container: ''
  name: BundleId
  type: string
- container: ''
  name: DedicatedTenancySupport
  type: string
- container: ''
  name: DedicatedTenancyManagementCidrRange
  type: string
- container: ''
  name: AccountModifications
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: DeviceTypeWindows
  type: string
- container: ''
  name: DeviceTypeOsx
  type: string
- container: ''
  name: DeviceTypeAndroid
  type: string
- container: ''
  name: DeviceTypeIos
  type: string
- container: ''
  name: DeviceTypeLinux
  type: string
- container: ''
  name: DeviceTypeWeb
  type: string
- container: ''
  name: ClientPropertiesList
  type: string
- container: ''
  name: ResourceIds
  type: string
- container: ''
  name: AddIns
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: ConnectionAliasPermissions
  type: string
- container: ''
  name: ConnectionAliases
  type: string
- container: ''
  name: AliasIds
  type: string
- container: ''
  name: Limit
  type: string
- container: ''
  name: Result
  type: string
- container: ''
  name: TagList
  type: string
- container: ''
  name: Bundles
  type: string
- container: ''
  name: BundleIds
  type: string
- container: ''
  name: Owner
  type: string
- container: ''
  name: Directories
  type: string
- container: ''
  name: DirectoryIds
  type: string
- container: ''
  name: ImagePermissions
  type: string
- container: ''
  name: Images
  type: string
- container: ''
  name: ImageIds
  type: string
- container: ''
  name: ImageType
  type: string
- container: ''
  name: RebuildSnapshots
  type: string
- container: ''
  name: RestoreSnapshots
  type: string
- container: ''
  name: WorkspaceIds
  type: string
- container: ''
  name: UserName
  type: string
- container: ''
  name: WorkspacesConnectionStatus
  type: string
- container: ''
  name: Ec2ImageId
  type: string
- container: ''
  name: IngestionProcess
  type: string
- container: ''
  name: ImageName
  type: string
- container: ''
  name: ImageDescription
  type: string
- container: ''
  name: Applications
  type: string
- container: ''
  name: ManagementCidrRanges
  type: string
- container: ''
  name: ManagementCidrRangeConstraint
  type: string
- container: ''
  name: SourceWorkspaceId
  type: string
- container: ''
  name: TargetWorkspaceId
  type: string
- container: ''
  name: PropertiesToDelete
  type: string
- container: ''
  name: WorkspaceState
  type: string
- container: ''
  name: RebootWorkspaceRequests
  type: string
- container: ''
  name: RebuildWorkspaceRequests
  type: string
- container: ''
  name: SubnetIds
  type: string
- container: ''
  name: EnableWorkDocs
  type: string
- container: ''
  name: EnableSelfService
  type: string
- container: ''
  name: Tenancy
  type: string
- container: ''
  name: StartWorkspaceRequests
  type: string
- container: ''
  name: StopWorkspaceRequests
  type: string
- container: ''
  name: TerminateWorkspaceRequests
  type: string
- container: ''
  name: AllowCopyImage
  type: string
- container: ''
  name: SharedAccountId
  type: string
- container: ''
  name: StartTime
  type: string
- container: ''
  name: ErrorCode
  type: string
- container: ''
  name: ErrorMessage
  type: string
- container: ''
  name: LastUpdatedTime
  type: string
- container: ''
  name: CreationTime
  type: string
- container: ''
  name: BundleType
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: CertificateAuthorityArn
  type: string
- container: ''
  name: ReconnectEnabled
  type: string
- container: ''
  name: LogUploadEnabled
  type: string
- container: ''
  name: Associations
  type: string
- container: ''
  name: AssociationStatus
  type: string
- container: ''
  name: AssociatedAccountId
  type: string
- container: ''
  name: AllowAssociation
  type: string
- container: ''
  name: Capacity
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: LoginMessage
  type: string
- container: ''
  name: LogoUrl
  type: string
- container: ''
  name: SupportEmail
  type: string
- container: ''
  name: SupportLink
  type: string
- container: ''
  name: ForgotPasswordLink
  type: string
- container: ''
  name: Logo
  type: string
- container: ''
  name: EnableInternetAccess
  type: string
- container: ''
  name: DefaultOu
  type: string
- container: ''
  name: CustomSecurityGroupId
  type: string
- container: ''
  name: UserEnabledAsLocalAdministrator
  type: string
- container: ''
  name: EnableMaintenanceMode
  type: string
- container: ''
  name: Logo2xUrl
  type: string
- container: ''
  name: Logo3xUrl
  type: string
- container: ''
  name: Alias
  type: string
- container: ''
  name: DirectoryName
  type: string
- container: ''
  name: RegistrationCode
  type: string
- container: ''
  name: DnsIpAddresses
  type: string
- container: ''
  name: CustomerUserName
  type: string
- container: ''
  name: IamRoleId
  type: string
- container: ''
  name: DirectoryType
  type: string
- container: ''
  name: WorkspaceSecurityGroupId
  type: string
- container: ''
  name: ipGroupIds
  type: string
- container: ''
  name: PrimaryWorkspaceId
  type: string
- container: ''
  name: VolumeEncryptionKey
  type: string
- container: ''
  name: StandbyWorkspaceRequest
  type: string
- container: ''
  name: WorkspaceRequest
  type: string
- container: ''
  name: UserVolumeEncryptionEnabled
  type: string
- container: ''
  name: RootVolumeEncryptionEnabled
  type: string
- container: ''
  name: Logo2x
  type: string
- container: ''
  name: Logo3x
  type: string
- container: ''
  name: ipRule
  type: string
- container: ''
  name: ruleDesc
  type: string
- container: ''
  name: Resource
  type: string
- container: ''
  name: UserAccessUrl
  type: string
- container: ''
  name: RelayStateParameterName
  type: string
- container: ''
  name: RestartWorkspace
  type: string
- container: ''
  name: IncreaseVolumeSize
  type: string
- container: ''
  name: ChangeComputeType
  type: string
- container: ''
  name: SwitchRunningMode
  type: string
- container: ''
  name: RebuildWorkspace
  type: string
- container: ''
  name: DeviceTypeChromeOs
  type: string
- container: ''
  name: DeviceTypeZeroClient
  type: string
- container: ''
  name: RunningMode
  type: string
- container: ''
  name: RunningModeAutoStopTimeoutInMinutes
  type: string
- container: ''
  name: RootVolumeSizeGib
  type: string
- container: ''
  name: UserVolumeSizeGib
  type: string
- container: ''
  name: ComputeTypeName
  type: string
- container: ''
  name: Protocols
  type: string
- container: ''
  name: Region
  type: string
- container: ''
  name: SnapshotTime
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: UpdateAvailable
  type: string
- container: ''
  name: IpAddress
  type: string
- container: ''
  name: SubnetId
  type: string
- container: ''
  name: ComputerName
  type: string
- container: ''
  name: ModificationStates
  type: string
- container: ''
  name: RelatedWorkspaces
  type: string
- container: ''
  name: ConnectionState
  type: string
- container: ''
  name: ConnectionStateCheckTimestamp
  type: string
- container: ''
  name: LastKnownUserConnectionTimestamp
  type: string
- container: ''
  name: Updates
  type: string
- container: ''
  name: groupId
  type: string
- container: ''
  name: groupName
  type: string
- container: ''
  name: groupDesc
  type: string
- container: ''
  name: userRules
  type: string
property_count: 173
provider_name: Amazon WorkSpaces
provider_slug: amazon-workspaces
slug: amazon-workspaces-context
tags:
- AWS
- Desktop
- End User Computing
- Virtual Desktop
- Desktop as a Service
- JSON-LD
- Linked Data
- Semantic Web
---
