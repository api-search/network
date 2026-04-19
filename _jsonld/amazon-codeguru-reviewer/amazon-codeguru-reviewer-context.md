---
class_count: 40
classes:
- AssociateRepositoryResponse
- CodeCommitRepository
- ThirdPartySourceRepository
- S3Repository
- CreateCodeReviewResponse
- DescribeCodeReviewResponse
- DescribeRecommendationFeedbackResponse
- DescribeRepositoryAssociationResponse
- DisassociateRepositoryResponse
- ListCodeReviewsResponse
- ListRecommendationFeedbackResponse
- ListRecommendationsResponse
- ListRepositoryAssociationsResponse
- ListTagsForResourceResponse
- PutRecommendationFeedbackResponse
- TagResourceResponse
- UntagResourceResponse
- TagMap
- AssociateRepositoryRequest
- BranchDiffSourceCodeType
- CodeReviewSummary
- CodeReviewType
- CommitDiffSourceCodeType
- CreateCodeReviewRequest
- DescribeCodeReviewRequest
- DescribeRecommendationFeedbackRequest
- DescribeRepositoryAssociationRequest
- DisassociateRepositoryRequest
- ListCodeReviewsRequest
- ListRecommendationFeedbackRequest
- ListRecommendationsRequest
- ListRepositoryAssociationsRequest
- ListTagsForResourceRequest
- PutRecommendationFeedbackRequest
- RecommendationFeedbackSummary
- RecommendationSummary
- RepositoryHeadSourceCodeType
- RepositoryAssociationSummary
- TagResourceRequest
- UntagResourceRequest
context_file: json-ld/amazon-codeguru-reviewer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-reviewer/refs/heads/main/json-ld/amazon-codeguru-reviewer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codeguru Reviewer from Amazon CodeGuru Reviewer.
layout: jsonld
name: Amazon Codeguru Reviewer Context
namespaces:
- prefix: amazon-code-guru-reviewer
  uri: https://amazon-code-guru-reviewer.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: RepositoryAnalysis
  type: string
- container: ''
  name: Repository
  type: string
- container: ''
  name: KMSKeyDetails
  type: string
- container: ''
  name: RepositoryAssociation
  type: string
- container: ''
  name: CodeArtifacts
  type: string
- container: ''
  name: SourceCodeType
  type: string
- container: ''
  name: Metrics
  type: string
- container: ''
  name: CodeReview
  type: string
- container: ''
  name: MetricsSummary
  type: string
- container: ''
  name: RecommendationFeedback
  type: string
- container: ''
  name: EventInfo
  type: string
- container: ''
  name: RuleMetadata
  type: string
- container: ''
  name: S3RepositoryDetails
  type: string
- container: ''
  name: RequestMetadata
  type: string
- container: ''
  name: S3BucketRepository
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: ConnectionArn
  type: string
- container: ''
  name: Owner
  type: string
- container: ''
  name: BucketName
  type: string
- container: ''
  name: RepositoryHead
  type: string
- container: ''
  name: CodeReviewSummaries
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: RecommendationFeedbackSummaries
  type: string
- container: ''
  name: RecommendationSummaries
  type: string
- container: ''
  name: RepositoryAssociationSummaries
  type: string
- container: ''
  name: CodeCommit
  type: string
- container: ''
  name: Bitbucket
  type: string
- container: ''
  name: GitHubEnterpriseServer
  type: string
- container: ''
  name: S3Bucket
  type: string
- container: ''
  name: KMSKeyId
  type: string
- container: ''
  name: EncryptionOption
  type: string
- container: ''
  name: ClientRequestToken
  type: string
- container: ''
  name: AssociationId
  type: string
- container: ''
  name: AssociationArn
  type: string
- container: ''
  name: ProviderType
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: StateReason
  type: string
- container: ''
  name: LastUpdatedTimeStamp
  type: string
- container: ''
  name: CreatedTimeStamp
  type: string
- container: ''
  name: SourceBranchName
  type: string
- container: ''
  name: DestinationBranchName
  type: string
- container: ''
  name: SourceCodeArtifactsObjectKey
  type: string
- container: ''
  name: BuildArtifactsObjectKey
  type: string
- container: ''
  name: CommitDiff
  type: string
- container: ''
  name: BranchDiff
  type: string
- container: ''
  name: MeteredLinesOfCodeCount
  type: string
- container: ''
  name: SuppressedLinesOfCodeCount
  type: string
- container: ''
  name: FindingsCount
  type: string
- container: ''
  name: CodeReviewArn
  type: string
- container: ''
  name: RepositoryName
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: PullRequestId
  type: string
- container: ''
  name: AnalysisTypes
  type: string
- container: ''
  name: ConfigFileState
  type: string
- container: ''
  name: SourceCommit
  type: string
- container: ''
  name: DestinationCommit
  type: string
- container: ''
  name: MergeBaseCommit
  type: string
- container: ''
  name: RepositoryAssociationArn
  type: string
- container: ''
  name: RecommendationId
  type: string
- container: ''
  name: Reactions
  type: string
- container: ''
  name: UserId
  type: string
- container: ''
  name: FilePath
  type: string
- container: ''
  name: StartLine
  type: string
- container: ''
  name: EndLine
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: RecommendationCategory
  type: string
- container: ''
  name: Severity
  type: string
- container: ''
  name: RuleId
  type: string
- container: ''
  name: RuleName
  type: string
- container: ''
  name: ShortDescription
  type: string
- container: ''
  name: LongDescription
  type: string
- container: ''
  name: RuleTags
  type: string
- container: ''
  name: BranchName
  type: string
- container: ''
  name: RequestId
  type: string
- container: ''
  name: Requester
  type: string
- container: ''
  name: VendorName
  type: string
- container: ''
  name: Details
  type: string
property_count: 78
provider_name: Amazon CodeGuru Reviewer
provider_slug: amazon-codeguru-reviewer
slug: amazon-codeguru-reviewer-context
tags:
- Amazon
- AWS
- Code Review
- Security
- DevOps
- Machine Learning
- Developer Tools
- JSON-LD
- Linked Data
- Semantic Web
---
