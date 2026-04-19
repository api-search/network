---
class_count: 116
classes:
- AccessPreview
- AccessPreviewFinding
- AccessPreviewStatusReason
- AccessPreviewSummary
- AclGrantee
- AnalyzedResource
- AnalyzedResourceSummary
- AnalyzerSummary
- ApplyArchiveRuleRequest
- ArchiveRuleSummary
- CancelPolicyGenerationRequest
- CancelPolicyGenerationResponse
- CloudTrailDetails
- CloudTrailProperties
- ConditionKeyMap
- Configuration
- ConfigurationsMap
- CreateAccessPreviewRequest
- CreateAccessPreviewResponse
- CreateAnalyzerRequest
- CreateAnalyzerResponse
- CreateArchiveRuleRequest
- Criterion
- DeleteAnalyzerRequest
- DeleteArchiveRuleRequest
- EbsSnapshotConfiguration
- EcrRepositoryConfiguration
- EfsFileSystemConfiguration
- FilterCriteriaMap
- Finding
- FindingSource
- FindingSourceDetail
- FindingSummary
- GeneratedPolicy
- GeneratedPolicyProperties
- GeneratedPolicyResult
- GetAccessPreviewRequest
- GetAccessPreviewResponse
- GetAnalyzedResourceRequest
- GetAnalyzedResourceResponse
- GetAnalyzerRequest
- GetAnalyzerResponse
- GetArchiveRuleRequest
- GetArchiveRuleResponse
- GetFindingRequest
- GetFindingResponse
- GetGeneratedPolicyRequest
- GetGeneratedPolicyResponse
- IamRoleConfiguration
- InlineArchiveRule
- InternetConfiguration
- JobDetails
- JobError
- KmsConstraintsMap
- KmsGrantConfiguration
- KmsGrantConstraints
- KmsKeyConfiguration
- KmsKeyPoliciesMap
- ListAccessPreviewFindingsRequest
- ListAccessPreviewFindingsResponse
- ListAccessPreviewsRequest
- ListAccessPreviewsResponse
- ListAnalyzedResourcesRequest
- ListAnalyzedResourcesResponse
- ListAnalyzersRequest
- ListAnalyzersResponse
- ListArchiveRulesRequest
- ListArchiveRulesResponse
- ListFindingsRequest
- ListFindingsResponse
- ListPolicyGenerationsRequest
- ListPolicyGenerationsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- Location
- NetworkOriginConfiguration
- PathElement
- PolicyGeneration
- PolicyGenerationDetails
- Position
- PrincipalMap
- RdsDbClusterSnapshotAttributeValue
- RdsDbClusterSnapshotAttributesMap
- RdsDbClusterSnapshotConfiguration
- RdsDbSnapshotAttributeValue
- RdsDbSnapshotAttributesMap
- RdsDbSnapshotConfiguration
- S3AccessPointConfiguration
- S3AccessPointConfigurationsMap
- S3BucketAclGrantConfiguration
- S3BucketConfiguration
- S3PublicAccessBlockConfiguration
- SecretsManagerSecretConfiguration
- SnsTopicConfiguration
- SortCriteria
- Span
- SqsQueueConfiguration
- StartPolicyGenerationRequest
- StartPolicyGenerationResponse
- StartResourceScanRequest
- StatusReason
- Substring
- TagResourceRequest
- TagResourceResponse
- TagsMap
- Trail
- TrailProperties
- UntagResourceRequest
- UntagResourceResponse
- UpdateArchiveRuleRequest
- UpdateFindingsRequest
- ValidatePolicyFinding
- ValidatePolicyRequest
- ValidatePolicyResponse
- VpcConfiguration
- name
context_file: json-ld/amazon-iam-access-analyzer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/json-ld/amazon-iam-access-analyzer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Iam Access Analyzer from Amazon IAM Access Analyzer.
layout: jsonld
name: Amazon Iam Access Analyzer Context
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
  name: accessPointAccount
  type: string
- container: ''
  name: accessPointArn
  type: string
- container: ''
  name: accessPointPolicy
  type: string
- container: ''
  name: accessPoints
  type: string
- container: ''
  name: accessPreview
  type: string
- container: ''
  name: accessPreviews
  type: string
- container: ''
  name: accessRole
  type: string
- container: ''
  name: accountIds
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: actions
  type: string
- container: ''
  name: allRegions
  type: string
- container: ''
  name: analyzedAt
  type: string
- container: ''
  name: analyzedResources
  type: string
- container: ''
  name: analyzer
  type: string
- container: ''
  name: analyzerArn
  type: string
- container: ''
  name: analyzerName
  type: string
- container: ''
  name: analyzers
  type: string
- container: ''
  name: archiveRule
  type: reference
- container: ''
  name: archiveRules
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: attributeName
  type: string
- container: ''
  name: attributes
  type: string
- container: ''
  name: bucketAclGrants
  type: string
- container: ''
  name: bucketPolicy
  type: string
- container: ''
  name: bucketPublicAccessBlock
  type: string
- container: ''
  name: changeType
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: cloudTrailArn
  type: string
- container: ''
  name: cloudTrailDetails
  type: string
- container: ''
  name: cloudTrailProperties
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: column
  type: string
- container: ''
  name: completedOn
  type: string
- container: ''
  name: condition
  type: string
- container: ''
  name: configurations
  type: string
- container: ''
  name: constraints
  type: string
- container: ''
  name: contains
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: detail
  type: string
- container: ''
  name: ebsSnapshot
  type: string
- container: ''
  name: ecrRepository
  type: string
- container: ''
  name: efsFileSystem
  type: string
- container: ''
  name: encryptionContextEquals
  type: string
- container: ''
  name: encryptionContextSubset
  type: string
- container: ''
  name: end
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: eq
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: existingFindingId
  type: string
- container: ''
  name: existingFindingStatus
  type: string
- container: ''
  name: exists
  type: string
- container: ''
  name: fileSystemPolicy
  type: string
- container: ''
  name: filter
  type: string
- container: ''
  name: finding
  type: string
- container: ''
  name: findingDetails
  type: string
- container: ''
  name: findingType
  type: string
- container: ''
  name: findings
  type: string
- container: ''
  name: generatedPolicies
  type: string
- container: ''
  name: generatedPolicyResult
  type: string
- container: ''
  name: grantee
  type: string
- container: ''
  name: granteePrincipal
  type: string
- container: ''
  name: grants
  type: string
- container: ''
  name: groups
  type: string
- container: ''
  name: iamRole
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: ids
  type: string
- container: ''
  name: ignorePublicAcls
  type: string
- container: ''
  name: index
  type: string
- container: ''
  name: internetConfiguration
  type: string
- container: ''
  name: isComplete
  type: string
- container: ''
  name: isPublic
  type: string
- container: ''
  name: issueCode
  type: string
- container: ''
  name: issuingAccount
  type: string
- container: ''
  name: jobDetails
  type: string
- container: ''
  name: jobError
  type: string
- container: ''
  name: jobId
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: keyPolicies
  type: string
- container: ''
  name: kmsKey
  type: string
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: lastResourceAnalyzed
  type: string
- container: ''
  name: lastResourceAnalyzedAt
  type: string
- container: ''
  name: learnMoreLink
  type: string
- container: ''
  name: length
  type: string
- container: ''
  name: line
  type: string
- container: ''
  name: locale
  type: string
- container: ''
  name: locations
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: neq
  type: string
- container: ''
  name: networkOrigin
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: offset
  type: string
- container: ''
  name: operations
  type: string
- container: ''
  name: orderBy
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: permission
  type: string
- container: ''
  name: policy
  type: string
- container: ''
  name: policyDocument
  type: string
- container: ''
  name: policyGenerationDetails
  type: string
- container: ''
  name: policyGenerations
  type: string
- container: ''
  name: policyType
  type: string
- container: ''
  name: principal
  type: string
- container: ''
  name: principalArn
  type: string
- container: ''
  name: properties
  type: string
- container: ''
  name: publicAccessBlock
  type: string
- container: ''
  name: queuePolicy
  type: string
- container: ''
  name: rdsDbClusterSnapshot
  type: string
- container: ''
  name: rdsDbSnapshot
  type: string
- container: ''
  name: regions
  type: string
- container: ''
  name: repositoryPolicy
  type: string
- container: ''
  name: resource
  type: string
- container: ''
  name: resourceArn
  type: string
- container: ''
  name: resourceOwnerAccount
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: restrictPublicBuckets
  type: string
- container: ''
  name: retiringPrincipal
  type: string
- container: ''
  name: ruleName
  type: string
- container: ''
  name: s3Bucket
  type: string
- container: ''
  name: secretPolicy
  type: string
- container: ''
  name: secretsManagerSecret
  type: string
- container: ''
  name: sharedVia
  type: string
- container: ''
  name: snsTopic
  type: string
- container: ''
  name: sort
  type: string
- container: ''
  name: sources
  type: string
- container: ''
  name: span
  type: string
- container: ''
  name: sqsQueue
  type: string
- container: ''
  name: start
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: startedOn
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: reference
- container: ''
  name: substring
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: topicPolicy
  type: string
- container: ''
  name: trailProperties
  type: string
- container: ''
  name: trails
  type: string
- container: ''
  name: trustPolicy
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: updatedAt
  type: string
- container: ''
  name: uri
  type: string
- container: ''
  name: userIds
  type: string
- container: ''
  name: validatePolicyResourceType
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: vpcConfiguration
  type: reference
- container: ''
  name: vpcId
  type: string
property_count: 146
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
slug: amazon-iam-access-analyzer-context
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
