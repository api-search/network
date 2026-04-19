---
class_count: 130
classes:
- AccessControlAttribute
- AccessControlAttributeValue
- AccountAssignment
- AccountAssignmentOperationStatus
- AccountAssignmentOperationStatusMetadata
- Address
- AttachCustomerManagedPolicyReferenceToPermissionSetRequest
- AttachCustomerManagedPolicyReferenceToPermissionSetResponse
- AttachManagedPolicyToPermissionSetRequest
- AttachManagedPolicyToPermissionSetResponse
- AttachedManagedPolicy
- AttributeOperation
- CreateAccountAssignmentRequest
- CreateAccountAssignmentResponse
- CreateGroupMembershipRequest
- CreateGroupMembershipResponse
- CreateGroupRequest
- CreateGroupResponse
- CreateInstanceAccessControlAttributeConfigurationRequest
- CreateInstanceAccessControlAttributeConfigurationResponse
- CreatePermissionSetRequest
- CreatePermissionSetResponse
- CreateUserRequest
- CreateUserResponse
- DeleteAccountAssignmentRequest
- DeleteAccountAssignmentResponse
- DeleteGroupMembershipRequest
- DeleteGroupMembershipResponse
- DeleteGroupRequest
- DeleteGroupResponse
- DeleteInlinePolicyFromPermissionSetRequest
- DeleteInlinePolicyFromPermissionSetResponse
- DeleteInstanceAccessControlAttributeConfigurationRequest
- DeleteInstanceAccessControlAttributeConfigurationResponse
- DeletePermissionSetRequest
- DeletePermissionSetResponse
- DeletePermissionsBoundaryFromPermissionSetRequest
- DeletePermissionsBoundaryFromPermissionSetResponse
- DeleteUserRequest
- DeleteUserResponse
- DescribeAccountAssignmentCreationStatusRequest
- DescribeAccountAssignmentCreationStatusResponse
- DescribeAccountAssignmentDeletionStatusRequest
- DescribeAccountAssignmentDeletionStatusResponse
- DescribeGroupMembershipRequest
- DescribeGroupMembershipResponse
- DescribeGroupRequest
- DescribeGroupResponse
- DescribeInstanceAccessControlAttributeConfigurationRequest
- DescribeInstanceAccessControlAttributeConfigurationResponse
- DescribePermissionSetProvisioningStatusRequest
- DescribePermissionSetProvisioningStatusResponse
- DescribePermissionSetRequest
- DescribePermissionSetResponse
- DescribeUserRequest
- DescribeUserResponse
- DetachCustomerManagedPolicyReferenceFromPermissionSetRequest
- DetachCustomerManagedPolicyReferenceFromPermissionSetResponse
- DetachManagedPolicyFromPermissionSetRequest
- DetachManagedPolicyFromPermissionSetResponse
- Email
- GetGroupIdRequest
- GetGroupIdResponse
- GetGroupMembershipIdRequest
- GetGroupMembershipIdResponse
- GetInlinePolicyForPermissionSetRequest
- GetInlinePolicyForPermissionSetResponse
- GetPermissionsBoundaryForPermissionSetRequest
- GetPermissionsBoundaryForPermissionSetResponse
- GetUserIdRequest
- GetUserIdResponse
- Group
- GroupMembership
- GroupMembershipExistenceResult
- InstanceMetadata
- IsMemberInGroupsRequest
- IsMemberInGroupsResponse
- ListAccountAssignmentCreationStatusRequest
- ListAccountAssignmentCreationStatusResponse
- ListAccountAssignmentDeletionStatusRequest
- ListAccountAssignmentDeletionStatusResponse
- ListAccountAssignmentsRequest
- ListAccountAssignmentsResponse
- ListAccountsForProvisionedPermissionSetRequest
- ListAccountsForProvisionedPermissionSetResponse
- ListCustomerManagedPolicyReferencesInPermissionSetRequest
- ListCustomerManagedPolicyReferencesInPermissionSetResponse
- ListGroupMembershipsForMemberRequest
- ListGroupMembershipsForMemberResponse
- ListGroupMembershipsRequest
- ListGroupMembershipsResponse
- ListGroupsRequest
- ListGroupsResponse
- ListInstancesRequest
- ListInstancesResponse
- ListManagedPoliciesInPermissionSetRequest
- ListManagedPoliciesInPermissionSetResponse
- ListPermissionSetProvisioningStatusRequest
- ListPermissionSetProvisioningStatusResponse
- ListPermissionSetsProvisionedToAccountRequest
- ListPermissionSetsProvisionedToAccountResponse
- ListPermissionSetsRequest
- ListPermissionSetsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- ListUsersRequest
- ListUsersResponse
- OperationStatusFilter
- PermissionSetProvisioningStatusMetadata
- PhoneNumber
- ProvisionPermissionSetRequest
- ProvisionPermissionSetResponse
- PutInlinePolicyToPermissionSetRequest
- PutInlinePolicyToPermissionSetResponse
- PutPermissionsBoundaryToPermissionSetRequest
- PutPermissionsBoundaryToPermissionSetResponse
- Tag
- TagResourceRequest
- TagResourceResponse
- UntagResourceRequest
- UntagResourceResponse
- UpdateGroupRequest
- UpdateGroupResponse
- UpdateInstanceAccessControlAttributeConfigurationRequest
- UpdateInstanceAccessControlAttributeConfigurationResponse
- UpdatePermissionSetRequest
- UpdatePermissionSetResponse
- UpdateUserRequest
- UpdateUserResponse
- User
context_file: json-ld/amazon-iam-identity-center-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-identity-center/refs/heads/main/json-ld/amazon-iam-identity-center-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Iam Identity Center from Amazon IAM Identity Center.
layout: jsonld
name: Amazon Iam Identity Center Context
namespaces:
- prefix: amzn
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AlternateIdentifier
  type: string
- container: ''
  name: AttributeValue
  type: string
- container: ''
  name: CustomerManagedPolicyReference
  type: string
- container: ''
  name: ExternalId
  type: string
- container: ''
  name: Filter
  type: string
- container: ''
  name: InstanceAccessControlAttributeConfiguration
  type: string
- container: ''
  name: MemberId
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: PermissionSet
  type: string
- container: ''
  name: PermissionSetProvisioningStatus
  type: string
- container: ''
  name: PermissionsBoundary
  type: string
- container: ''
  name: UniqueAttribute
  type: string
- container: ''
  name: AccessControlAttributes
  type: string
- container: ''
  name: AccountAssignmentCreationRequestId
  type: string
- container: ''
  name: AccountAssignmentCreationStatus
  type: string
- container: ''
  name: AccountAssignmentDeletionRequestId
  type: string
- container: ''
  name: AccountAssignmentDeletionStatus
  type: string
- container: ''
  name: AccountAssignments
  type: string
- container: ''
  name: AccountAssignmentsCreationStatus
  type: string
- container: ''
  name: AccountAssignmentsDeletionStatus
  type: string
- container: ''
  name: AccountId
  type: string
- container: ''
  name: AccountIds
  type: string
- container: ''
  name: Addresses
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: AttachedManagedPolicies
  type: string
- container: ''
  name: AttributePath
  type: string
- container: ''
  name: Country
  type: string
- container: ''
  name: CreatedDate
  type: string
- container: ''
  name: CustomerManagedPolicyReferences
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: DisplayName
  type: string
- container: ''
  name: Emails
  type: string
- container: ''
  name: ExternalIds
  type: string
- container: ''
  name: FailureReason
  type: string
- container: ''
  name: FamilyName
  type: string
- container: ''
  name: Filters
  type: string
- container: ''
  name: Formatted
  type: string
- container: ''
  name: GivenName
  type: string
- container: ''
  name: GroupId
  type: string
- container: ''
  name: GroupIds
  type: string
- container: ''
  name: GroupMemberships
  type: string
- container: ''
  name: Groups
  type: string
- container: ''
  name: HonorificPrefix
  type: string
- container: ''
  name: HonorificSuffix
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: IdentityStoreId
  type: string
- container: ''
  name: InlinePolicy
  type: string
- container: ''
  name: InstanceArn
  type: string
- container: ''
  name: Instances
  type: string
- container: ''
  name: Issuer
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Locale
  type: string
- container: ''
  name: Locality
  type: string
- container: ''
  name: ManagedPolicyArn
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: MembershipExists
  type: string
- container: ''
  name: MembershipId
  type: string
- container: ''
  name: MiddleName
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: NickName
  type: string
- container: ''
  name: Operations
  type: string
- container: ''
  name: Path
  type: string
- container: ''
  name: PermissionSetArn
  type: string
- container: ''
  name: PermissionSets
  type: string
- container: ''
  name: PermissionSetsProvisioningStatus
  type: string
- container: ''
  name: PhoneNumbers
  type: string
- container: ''
  name: PostalCode
  type: string
- container: ''
  name: PreferredLanguage
  type: string
- container: ''
  name: Primary
  type: string
- container: ''
  name: PrincipalId
  type: string
- container: ''
  name: PrincipalType
  type: string
- container: ''
  name: ProfileUrl
  type: string
- container: ''
  name: ProvisionPermissionSetRequestId
  type: string
- container: ''
  name: ProvisioningStatus
  type: string
- container: ''
  name: Region
  type: string
- container: ''
  name: RelayState
  type: string
- container: ''
  name: RequestId
  type: string
- container: ''
  name: ResourceArn
  type: string
- container: ''
  name: Results
  type: string
- container: ''
  name: SessionDuration
  type: string
- container: ''
  name: Source
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: StatusReason
  type: string
- container: ''
  name: StreetAddress
  type: string
- container: ''
  name: TagKeys
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: TargetId
  type: string
- container: ''
  name: TargetType
  type: string
- container: ''
  name: Timezone
  type: string
- container: ''
  name: Title
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: UserId
  type: string
- container: ''
  name: UserName
  type: string
- container: ''
  name: UserType
  type: string
- container: ''
  name: Users
  type: string
- container: ''
  name: Value
  type: string
property_count: 96
provider_name: Amazon IAM Identity Center
provider_slug: amazon-iam-identity-center
slug: amazon-iam-identity-center-context
tags:
- Access Control
- Authentication
- AWS
- Identity Management
- Single Sign-On
- JSON-LD
- Linked Data
- Semantic Web
---
