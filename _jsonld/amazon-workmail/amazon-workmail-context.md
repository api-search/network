---
class_count: 184
classes:
- AccessControlRule
- AssociateDelegateToResourceRequest
- AssociateDelegateToResourceResponse
- AssociateMemberToGroupRequest
- AssociateMemberToGroupResponse
- AssumeImpersonationRoleRequest
- AssumeImpersonationRoleResponse
- AvailabilityConfiguration
- CancelMailboxExportJobRequest
- CancelMailboxExportJobResponse
- CreateAliasRequest
- CreateAliasResponse
- CreateAvailabilityConfigurationRequest
- CreateAvailabilityConfigurationResponse
- CreateGroupRequest
- CreateGroupResponse
- CreateImpersonationRoleRequest
- CreateImpersonationRoleResponse
- CreateMobileDeviceAccessRuleRequest
- CreateMobileDeviceAccessRuleResponse
- CreateOrganizationRequest
- CreateOrganizationResponse
- CreateResourceRequest
- CreateResourceResponse
- CreateUserRequest
- CreateUserResponse
- Delegate
- DeleteAccessControlRuleRequest
- DeleteAccessControlRuleResponse
- DeleteAliasRequest
- DeleteAliasResponse
- DeleteAvailabilityConfigurationRequest
- DeleteAvailabilityConfigurationResponse
- DeleteEmailMonitoringConfigurationRequest
- DeleteEmailMonitoringConfigurationResponse
- DeleteGroupRequest
- DeleteGroupResponse
- DeleteImpersonationRoleRequest
- DeleteImpersonationRoleResponse
- DeleteMailboxPermissionsRequest
- DeleteMailboxPermissionsResponse
- DeleteMobileDeviceAccessOverrideRequest
- DeleteMobileDeviceAccessOverrideResponse
- DeleteMobileDeviceAccessRuleRequest
- DeleteMobileDeviceAccessRuleResponse
- DeleteOrganizationRequest
- DeleteOrganizationResponse
- DeleteResourceRequest
- DeleteResourceResponse
- DeleteRetentionPolicyRequest
- DeleteRetentionPolicyResponse
- DeleteUserRequest
- DeleteUserResponse
- DeregisterFromWorkMailRequest
- DeregisterFromWorkMailResponse
- DeregisterMailDomainRequest
- DeregisterMailDomainResponse
- DescribeEmailMonitoringConfigurationRequest
- DescribeEmailMonitoringConfigurationResponse
- DescribeGroupRequest
- DescribeGroupResponse
- DescribeInboundDmarcSettingsRequest
- DescribeInboundDmarcSettingsResponse
- DescribeMailboxExportJobRequest
- DescribeMailboxExportJobResponse
- DescribeOrganizationRequest
- DescribeOrganizationResponse
- DescribeResourceRequest
- DescribeResourceResponse
- DescribeUserRequest
- DescribeUserResponse
- DisassociateDelegateFromResourceRequest
- DisassociateDelegateFromResourceResponse
- DisassociateMemberFromGroupRequest
- DisassociateMemberFromGroupResponse
- DnsRecord
- Domain
- EwsAvailabilityProvider
- FolderConfiguration
- GetAccessControlEffectRequest
- GetAccessControlEffectResponse
- GetDefaultRetentionPolicyRequest
- GetDefaultRetentionPolicyResponse
- GetImpersonationRoleEffectRequest
- GetImpersonationRoleEffectResponse
- GetImpersonationRoleRequest
- GetImpersonationRoleResponse
- GetMailDomainRequest
- GetMailDomainResponse
- GetMailboxDetailsRequest
- GetMailboxDetailsResponse
- GetMobileDeviceAccessEffectRequest
- GetMobileDeviceAccessEffectResponse
- GetMobileDeviceAccessOverrideRequest
- GetMobileDeviceAccessOverrideResponse
- Group
- ImpersonationMatchedRule
- ImpersonationRole
- ImpersonationRule
- LambdaAvailabilityProvider
- ListAccessControlRulesRequest
- ListAccessControlRulesResponse
- ListAliasesRequest
- ListAliasesResponse
- ListAvailabilityConfigurationsRequest
- ListAvailabilityConfigurationsResponse
- ListGroupMembersRequest
- ListGroupMembersResponse
- ListGroupsRequest
- ListGroupsResponse
- ListImpersonationRolesRequest
- ListImpersonationRolesResponse
- ListMailDomainsRequest
- ListMailDomainsResponse
- ListMailboxExportJobsRequest
- ListMailboxExportJobsResponse
- ListMailboxPermissionsRequest
- ListMailboxPermissionsResponse
- ListMobileDeviceAccessOverridesRequest
- ListMobileDeviceAccessOverridesResponse
- ListMobileDeviceAccessRulesRequest
- ListMobileDeviceAccessRulesResponse
- ListOrganizationsRequest
- ListOrganizationsResponse
- ListResourceDelegatesRequest
- ListResourceDelegatesResponse
- ListResourcesRequest
- ListResourcesResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- ListUsersRequest
- ListUsersResponse
- MailDomainSummary
- MailboxExportJob
- Member
- MobileDeviceAccessMatchedRule
- MobileDeviceAccessOverride
- MobileDeviceAccessRule
- OrganizationSummary
- Permission
- PutAccessControlRuleRequest
- PutAccessControlRuleResponse
- PutEmailMonitoringConfigurationRequest
- PutEmailMonitoringConfigurationResponse
- PutInboundDmarcSettingsRequest
- PutInboundDmarcSettingsResponse
- PutMailboxPermissionsRequest
- PutMailboxPermissionsResponse
- PutMobileDeviceAccessOverrideRequest
- PutMobileDeviceAccessOverrideResponse
- PutRetentionPolicyRequest
- PutRetentionPolicyResponse
- RedactedEwsAvailabilityProvider
- RegisterMailDomainRequest
- RegisterMailDomainResponse
- RegisterToWorkMailRequest
- RegisterToWorkMailResponse
- ResetPasswordRequest
- ResetPasswordResponse
- Resource
- StartMailboxExportJobRequest
- StartMailboxExportJobResponse
- TagResourceRequest
- TagResourceResponse
- Tag
- TestAvailabilityConfigurationRequest
- TestAvailabilityConfigurationResponse
- UntagResourceRequest
- UntagResourceResponse
- UpdateAvailabilityConfigurationRequest
- UpdateAvailabilityConfigurationResponse
- UpdateDefaultMailDomainRequest
- UpdateDefaultMailDomainResponse
- UpdateImpersonationRoleRequest
- UpdateImpersonationRoleResponse
- UpdateMailboxQuotaRequest
- UpdateMailboxQuotaResponse
- UpdateMobileDeviceAccessRuleRequest
- UpdateMobileDeviceAccessRuleResponse
- UpdatePrimaryEmailAddressRequest
- UpdatePrimaryEmailAddressResponse
- UpdateResourceRequest
- UpdateResourceResponse
- User
context_file: json-ld/amazon-workmail-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-workmail/refs/heads/main/json-ld/amazon-workmail-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Workmail from Amazon WorkMail.
layout: jsonld
name: Amazon Workmail Context
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
  name: Name
  type: string
- container: ''
  name: Effect
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: IpRanges
  type: string
- container: ''
  name: NotIpRanges
  type: string
- container: ''
  name: Actions
  type: string
- container: ''
  name: NotActions
  type: string
- container: ''
  name: UserIds
  type: string
- container: ''
  name: NotUserIds
  type: string
- container: ''
  name: DateCreated
  type: string
- container: ''
  name: DateModified
  type: string
- container: ''
  name: ImpersonationRoleIds
  type: string
- container: ''
  name: NotImpersonationRoleIds
  type: string
- container: ''
  name: OrganizationId
  type: string
- container: ''
  name: ResourceId
  type: string
- container: ''
  name: EntityId
  type: string
- container: ''
  name: GroupId
  type: string
- container: ''
  name: MemberId
  type: string
- container: ''
  name: ImpersonationRoleId
  type: string
- container: ''
  name: Token
  type: string
- container: ''
  name: ExpiresIn
  type: string
- container: ''
  name: DomainName
  type: string
- container: ''
  name: ProviderType
  type: string
- container: ''
  name: EwsProvider
  type: string
- container: ''
  name: LambdaProvider
  type: string
- container: ''
  name: BookingOptions
  type: string
- container: ''
  name: AutoAcceptRequests
  type: string
- container: ''
  name: AutoDeclineRecurringRequests
  type: string
- container: ''
  name: AutoDeclineConflictingRequests
  type: string
- container: ''
  name: ClientToken
  type: string
- container: ''
  name: JobId
  type: string
- container: ''
  name: Alias
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: Rules
  type: string
- container: ''
  name: DeviceTypes
  type: string
- container: ''
  name: NotDeviceTypes
  type: string
- container: ''
  name: DeviceModels
  type: string
- container: ''
  name: NotDeviceModels
  type: string
- container: ''
  name: DeviceOperatingSystems
  type: string
- container: ''
  name: NotDeviceOperatingSystems
  type: string
- container: ''
  name: DeviceUserAgents
  type: string
- container: ''
  name: NotDeviceUserAgents
  type: string
- container: ''
  name: MobileDeviceAccessRuleId
  type: string
- container: ''
  name: DirectoryId
  type: string
- container: ''
  name: Domains
  type: string
- container: ''
  name: KmsKeyArn
  type: string
- container: ''
  name: EnableInteroperability
  type: string
- container: ''
  name: DisplayName
  type: string
- container: ''
  name: Password
  type: string
- container: ''
  name: UserId
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: GranteeId
  type: string
- container: ''
  name: DeviceId
  type: string
- container: ''
  name: DeleteDirectory
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: RoleArn
  type: string
- container: ''
  name: LogGroupArn
  type: string
- container: ''
  name: Email
  type: string
- container: ''
  name: EnabledDate
  type: string
- container: ''
  name: DisabledDate
  type: string
- container: ''
  name: Enforced
  type: string
- container: ''
  name: S3BucketName
  type: string
- container: ''
  name: S3Prefix
  type: string
- container: ''
  name: S3Path
  type: string
- container: ''
  name: EstimatedProgress
  type: string
- container: ''
  name: ErrorInfo
  type: string
- container: ''
  name: StartTime
  type: string
- container: ''
  name: EndTime
  type: string
- container: ''
  name: DirectoryType
  type: string
- container: ''
  name: DefaultMailDomain
  type: string
- container: ''
  name: CompletedDate
  type: string
- container: ''
  name: ErrorMessage
  type: string
- container: ''
  name: ARN
  type: string
- container: ''
  name: UserRole
  type: string
- container: ''
  name: Hostname
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: HostedZoneId
  type: string
- container: ''
  name: EwsEndpoint
  type: string
- container: ''
  name: EwsUsername
  type: string
- container: ''
  name: EwsPassword
  type: string
- container: ''
  name: Action
  type: string
- container: ''
  name: Period
  type: string
- container: ''
  name: IpAddress
  type: string
- container: ''
  name: MatchedRules
  type: string
- container: ''
  name: FolderConfigurations
  type: string
- container: ''
  name: TargetUser
  type: string
- container: ''
  name: Records
  type: string
- container: ''
  name: IsTestDomain
  type: string
- container: ''
  name: IsDefault
  type: string
- container: ''
  name: OwnershipVerificationStatus
  type: string
- container: ''
  name: DkimVerificationStatus
  type: string
- container: ''
  name: MailboxQuota
  type: string
- container: ''
  name: MailboxSize
  type: string
- container: ''
  name: DeviceType
  type: string
- container: ''
  name: DeviceModel
  type: string
- container: ''
  name: DeviceOperatingSystem
  type: string
- container: ''
  name: DeviceUserAgent
  type: string
- container: ''
  name: ImpersonationRuleId
  type: string
- container: ''
  name: TargetUsers
  type: string
- container: ''
  name: NotTargetUsers
  type: string
- container: ''
  name: LambdaArn
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: Aliases
  type: string
- container: ''
  name: AvailabilityConfigurations
  type: string
- container: ''
  name: Members
  type: string
- container: ''
  name: Groups
  type: string
- container: ''
  name: Roles
  type: string
- container: ''
  name: MailDomains
  type: string
- container: ''
  name: Jobs
  type: string
- container: ''
  name: Permissions
  type: string
- container: ''
  name: Overrides
  type: string
- container: ''
  name: OrganizationSummaries
  type: string
- container: ''
  name: Delegates
  type: string
- container: ''
  name: Resources
  type: string
- container: ''
  name: ResourceARN
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: Users
  type: string
- container: ''
  name: DefaultDomain
  type: string
- container: ''
  name: GranteeType
  type: string
- container: ''
  name: PermissionValues
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: TestPassed
  type: string
- container: ''
  name: FailureReason
  type: string
- container: ''
  name: TagKeys
  type: string
property_count: 125
provider_name: Amazon WorkMail
provider_slug: amazon-workmail
slug: amazon-workmail-context
tags:
- AWS
- Business Communication
- Calendar
- Email
- Exchange
- Enterprise
- JSON-LD
- Linked Data
- Semantic Web
---
