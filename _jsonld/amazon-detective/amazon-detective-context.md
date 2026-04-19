---
class_count: 53
classes:
- AcceptInvitationRequest
- Account
- Administrator
- BatchGetGraphMemberDatasourcesRequest
- BatchGetGraphMemberDatasourcesResponse
- BatchGetMembershipDatasourcesRequest
- BatchGetMembershipDatasourcesResponse
- CreateGraphRequest
- CreateGraphResponse
- CreateMembersRequest
- CreateMembersResponse
- DatasourcePackageIngestDetail
- DeleteGraphRequest
- DeleteMembersRequest
- DeleteMembersResponse
- DescribeOrganizationConfigurationRequest
- DescribeOrganizationConfigurationResponse
- DisassociateMembershipRequest
- EnableOrganizationAdminAccountRequest
- GetInvestigationRequest
- GetInvestigationResponse
- GetMembersRequest
- GetMembersResponse
- Graph
- Indicator
- InvestigationDetail
- ListDatasourcePackagesRequest
- ListDatasourcePackagesResponse
- ListGraphsRequest
- ListGraphsResponse
- ListIndicatorsRequest
- ListIndicatorsResponse
- ListInvestigationsRequest
- ListInvestigationsResponse
- ListInvitationsRequest
- ListInvitationsResponse
- ListMembersRequest
- ListMembersResponse
- ListOrganizationAdminAccountsRequest
- ListOrganizationAdminAccountsResponse
- ListTagsForResourceResponse
- MemberDetail
- RejectInvitationRequest
- StartInvestigationRequest
- StartInvestigationResponse
- StartMonitoringMemberRequest
- TagResourceRequest
- TimestampForCollection
- UnprocessedAccount
- UnprocessedGraph
- UpdateDatasourcePackagesRequest
- UpdateInvestigationStateRequest
- UpdateOrganizationConfigurationRequest
context_file: json-ld/amazon-detective-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-detective/refs/heads/main/json-ld/amazon-detective-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Detective from Amazon Detective.
layout: jsonld
name: Amazon Detective Context
namespaces:
- prefix: amz
  uri: https://amazonaws.com/detective/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: MembershipDatasources
  type: string
- container: ''
  name: AccountId
  type: string
- container: set
  name: AccountIds
  type: string
- container: set
  name: Accounts
  type: string
- container: ''
  name: AdministratorId
  type: string
- container: set
  name: Administrators
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: AutoEnable
  type: boolean
- container: ''
  name: CreatedTime
  type: dateTime
- container: ''
  name: DatasourcePackageIngestHistory
  type: reference
- container: ''
  name: DatasourcePackageIngestState
  type: string
- container: ''
  name: DatasourcePackages
  type: reference
- container: ''
  name: DelegationTime
  type: dateTime
- container: ''
  name: DisableEmailNotification
  type: boolean
- container: ''
  name: DisabledReason
  type: string
- container: ''
  name: EmailAddress
  type: string
- container: ''
  name: EntityArn
  type: string
- container: ''
  name: EntityType
  type: string
- container: ''
  name: Field
  type: string
- container: ''
  name: FilterCriteria
  type: reference
- container: ''
  name: GraphArn
  type: string
- container: set
  name: GraphArns
  type: string
- container: set
  name: GraphList
  type: string
- container: ''
  name: IndicatorDetail
  type: reference
- container: ''
  name: IndicatorType
  type: string
- container: set
  name: Indicators
  type: string
- container: set
  name: InvestigationDetails
  type: string
- container: ''
  name: InvestigationId
  type: string
- container: ''
  name: InvitationType
  type: string
- container: set
  name: Invitations
  type: string
- container: ''
  name: InvitedTime
  type: dateTime
- container: ''
  name: LastIngestStateChange
  type: reference
- container: ''
  name: MaxResults
  type: integer
- container: set
  name: MemberDatasources
  type: string
- container: set
  name: MemberDetails
  type: string
- container: set
  name: Members
  type: string
- container: ''
  name: Message
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: PercentOfGraphUtilization
  type: decimal
- container: ''
  name: Reason
  type: string
- container: ''
  name: ScopeEndTime
  type: dateTime
- container: ''
  name: ScopeStartTime
  type: dateTime
- container: ''
  name: Severity
  type: string
- container: ''
  name: SortCriteria
  type: reference
- container: ''
  name: SortOrder
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: Tags
  type: reference
- container: ''
  name: Timestamp
  type: dateTime
- container: set
  name: UnprocessedAccounts
  type: string
- container: set
  name: UnprocessedGraphs
  type: string
- container: ''
  name: UpdatedTime
  type: dateTime
- container: ''
  name: Value
  type: string
- container: ''
  name: VolumeUsageInBytes
  type: integer
- container: ''
  name: VolumeUsageUpdatedTime
  type: dateTime
property_count: 55
provider_name: Amazon Detective
provider_slug: amazon-detective
slug: amazon-detective-context
tags:
- AWS
- Forensics
- Investigation
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
