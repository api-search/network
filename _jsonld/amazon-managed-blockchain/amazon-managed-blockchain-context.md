---
class_count: 93
classes:
- Accessor
- AccessorSummary
- ApprovalThresholdPolicy
- CreateAccessorInput
- CreateAccessorOutput
- CreateMemberInput
- CreateMemberOutput
- CreateNetworkInput
- CreateNetworkOutput
- CreateNodeInput
- CreateNodeOutput
- CreateProposalInput
- CreateProposalOutput
- DeleteAccessorInput
- DeleteAccessorOutput
- DeleteMemberInput
- DeleteMemberOutput
- DeleteNodeInput
- DeleteNodeOutput
- GetAccessorInput
- GetAccessorOutput
- GetMemberInput
- GetMemberOutput
- GetNetworkInput
- GetNetworkOutput
- GetNodeInput
- GetNodeOutput
- GetProposalInput
- GetProposalOutput
- InputTagMap
- Invitation
- InviteAction
- ListAccessorsInput
- ListAccessorsOutput
- ListInvitationsInput
- ListInvitationsOutput
- ListMembersInput
- ListMembersOutput
- ListNetworksInput
- ListNetworksOutput
- ListNodesInput
- ListNodesOutput
- ListProposalVotesInput
- ListProposalVotesOutput
- ListProposalsInput
- ListProposalsOutput
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- LogConfiguration
- LogConfigurations
- Member
- MemberConfiguration
- MemberFabricAttributes
- MemberFabricConfiguration
- MemberFabricLogPublishingConfiguration
- MemberFrameworkAttributes
- MemberFrameworkConfiguration
- MemberLogPublishingConfiguration
- MemberSummary
- Network
- NetworkEthereumAttributes
- NetworkFabricAttributes
- NetworkFabricConfiguration
- NetworkFrameworkAttributes
- NetworkFrameworkConfiguration
- NetworkSummary
- Node
- NodeConfiguration
- NodeEthereumAttributes
- NodeFabricAttributes
- NodeFabricLogPublishingConfiguration
- NodeFrameworkAttributes
- NodeLogPublishingConfiguration
- NodeSummary
- OutputTagMap
- Proposal
- ProposalActions
- ProposalSummary
- RejectInvitationInput
- RejectInvitationOutput
- RemoveAction
- TagResourceRequest
- TagResourceResponse
- UntagResourceRequest
- UntagResourceResponse
- UpdateMemberInput
- UpdateMemberOutput
- UpdateNodeInput
- UpdateNodeOutput
- VoteOnProposalInput
- VoteOnProposalOutput
- VoteSummary
- VotingPolicy
context_file: json-ld/amazon-managed-blockchain-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-blockchain/refs/heads/main/json-ld/amazon-managed-blockchain-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Managed Blockchain from Amazon Managed Blockchain.
layout: jsonld
name: Amazon Managed Blockchain Context
namespaces:
- prefix: ambc
  uri: https://ambc.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AccessorId
  type: ''
- container: ''
  name: AccessorType
  type: ''
- container: ''
  name: Accessors
  type: ''
- container: ''
  name: Actions
  type: ''
- container: ''
  name: AdminPassword
  type: ''
- container: ''
  name: AdminUsername
  type: ''
- container: ''
  name: Arn
  type: ''
- container: ''
  name: AvailabilityZone
  type: ''
- container: ''
  name: BillingToken
  type: ''
- container: ''
  name: CaEndpoint
  type: ''
- container: ''
  name: CaLogs
  type: ''
- container: ''
  name: ChainId
  type: ''
- container: ''
  name: ChaincodeLogs
  type: ''
- container: ''
  name: ClientRequestToken
  type: ''
- container: ''
  name: Cloudwatch
  type: ''
- container: ''
  name: CreationDate
  type: ''
- container: ''
  name: Description
  type: ''
- container: ''
  name: Edition
  type: ''
- container: ''
  name: Enabled
  type: ''
- container: ''
  name: Ethereum
  type: ''
- container: ''
  name: ExpirationDate
  type: ''
- container: ''
  name: Fabric
  type: ''
- container: ''
  name: Framework
  type: ''
- container: ''
  name: FrameworkAttributes
  type: ''
- container: ''
  name: FrameworkConfiguration
  type: ''
- container: ''
  name: FrameworkVersion
  type: ''
- container: ''
  name: HttpEndpoint
  type: ''
- container: ''
  name: Id
  type: ''
- container: ''
  name: InstanceType
  type: ''
- container: ''
  name: InvitationId
  type: ''
- container: ''
  name: Invitations
  type: ''
- container: ''
  name: IsOwned
  type: ''
- container: ''
  name: KmsKeyArn
  type: ''
- container: ''
  name: LogPublishingConfiguration
  type: ''
- container: ''
  name: MemberId
  type: ''
- container: ''
  name: MemberName
  type: ''
- container: ''
  name: Members
  type: ''
- container: ''
  name: Name
  type: ''
- container: ''
  name: NetworkId
  type: ''
- container: ''
  name: Networks
  type: ''
- container: ''
  name: NextToken
  type: ''
- container: ''
  name: NoVoteCount
  type: ''
- container: ''
  name: NodeId
  type: ''
- container: ''
  name: Nodes
  type: ''
- container: ''
  name: OrderingServiceEndpoint
  type: ''
- container: ''
  name: OutstandingVoteCount
  type: ''
- container: ''
  name: PeerEndpoint
  type: ''
- container: ''
  name: PeerEventEndpoint
  type: ''
- container: ''
  name: PeerLogs
  type: ''
- container: ''
  name: Principal
  type: ''
- container: ''
  name: ProposalDurationInHours
  type: ''
- container: ''
  name: ProposalId
  type: ''
- container: ''
  name: ProposalVotes
  type: ''
- container: ''
  name: Proposals
  type: ''
- container: ''
  name: ProposedByMemberId
  type: ''
- container: ''
  name: ProposedByMemberName
  type: ''
- container: ''
  name: Removals
  type: ''
- container: ''
  name: StateDB
  type: ''
- container: ''
  name: Status
  type: ''
- container: ''
  name: Tags
  type: ''
- container: ''
  name: ThresholdComparator
  type: ''
- container: ''
  name: ThresholdPercentage
  type: ''
- container: ''
  name: Type
  type: ''
- container: ''
  name: Vote
  type: ''
- container: ''
  name: VoterMemberId
  type: ''
- container: ''
  name: VpcEndpointServiceName
  type: ''
- container: ''
  name: WebSocketEndpoint
  type: ''
- container: ''
  name: YesVoteCount
  type: ''
property_count: 68
provider_name: Amazon Managed Blockchain
provider_slug: amazon-managed-blockchain
slug: amazon-managed-blockchain-context
tags:
- AWS
- Blockchain
- Distributed Ledger
- Hyperledger Fabric
- Ethereum
- JSON-LD
- Linked Data
- Semantic Web
---
