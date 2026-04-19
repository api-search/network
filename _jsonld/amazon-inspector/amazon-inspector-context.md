---
class_count: 102
classes:
- Account
- AccountAggregation
- AccountAggregationResponse
- AccountState
- AggregationRequest
- AggregationResponse
- Amazon Inspector Finding Definition
- AmiAggregation
- AmiAggregationResponse
- AssociateMemberRequest
- AssociateMemberResponse
- AtigData
- AutoEnable
- AwsEc2InstanceDetails
- AwsEcrContainerAggregation
- AwsEcrContainerAggregationResponse
- AwsEcrContainerImageDetails
- AwsLambdaFunctionDetails
- BatchGetAccountStatusRequest
- BatchGetAccountStatusResponse
- BatchGetCodeSnippetRequest
- BatchGetCodeSnippetResponse
- BatchGetFindingDetailsRequest
- BatchGetFindingDetailsResponse
- BatchGetFreeTrialInfoRequest
- BatchGetFreeTrialInfoResponse
- BatchGetMemberEc2DeepInspectionStatusRequest
- BatchGetMemberEc2DeepInspectionStatusResponse
- BatchUpdateMemberEc2DeepInspectionStatusRequest
- BatchUpdateMemberEc2DeepInspectionStatusResponse
- CancelFindingsReportRequest
- CancelFindingsReportResponse
- CancelSbomExportRequest
- CancelSbomExportResponse
- CisaData
- CodeFilePath
- CodeLine
- CodeSnippetError
- CodeSnippetResult
- CodeVulnerabilityDetails
- Counts
- CoverageDateFilter
- CoverageFilterCriteria
- CoverageMapFilter
- CoverageStringFilter
- CoveredResource
- CreateFilterRequest
- CreateFilterResponse
- CreateFindingsReportRequest
- CreateFindingsReportResponse
- CreateSbomExportRequest
- CreateSbomExportResponse
- Cvss2
- Cvss3
- CvssScore
- CvssScoreAdjustment
- CvssScoreDetails
- DateFilter
- DelegatedAdmin
- DelegatedAdminAccount
- DeleteFilterRequest
- DeleteFilterResponse
- DescribeOrganizationConfigurationRequest
- DescribeOrganizationConfigurationResponse
- Destination
- DisableDelegatedAdminAccountRequest
- DisableDelegatedAdminAccountResponse
- DisableResponse
- DisassociateMemberResponse
- Ec2InstanceAggregation
- Ec2InstanceAggregationResponse
- EnableDelegatedAdminAccountResponse
- EnableResponse
- FilterCriteria
- FindingTypeAggregation
- FindingTypeAggregationResponse
- GetConfigurationResponse
- GetDelegatedAdminAccountResponse
- GetEc2DeepInspectionConfigurationResponse
- GetEncryptionKeyResponse
- GetFindingsReportStatusResponse
- GetMemberResponse
- GetSbomExportResponse
- ImageLayerAggregation
- ImageLayerAggregationResponse
- LambdaFunctionAggregation
- LambdaFunctionAggregationResponse
- LambdaLayerAggregation
- LambdaLayerAggregationResponse
- LambdaVpcConfig
- ListAccountPermissionsResponse
- ListCoverageResponse
- ListCoverageStatisticsResponse
- ListDelegatedAdminAccountsResponse
- ListFiltersResponse
- ListFindingAggregationsResponse
- ListFindingsResponse
- ListMembersResponse
- ListTagsForResourceResponse
- ListUsageTotalsResponse
- description
- name
context_file: json-ld/amazon-inspector-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-inspector/refs/heads/main/json-ld/amazon-inspector-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Inspector from Amazon Inspector.
layout: jsonld
name: Amazon Inspector Context
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
  name: accountAggregation
  type: string
- container: ''
  name: accountId
  type: string
- container: ''
  name: accountIds
  type: string
- container: ''
  name: accounts
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: activateDeepInspection
  type: string
- container: ''
  name: adjustments
  type: string
- container: ''
  name: affectedImages
  type: string
- container: ''
  name: affectedInstances
  type: string
- container: ''
  name: aggregationType
  type: string
- container: ''
  name: all
  type: string
- container: ''
  name: ami
  type: string
- container: ''
  name: amiAggregation
  type: string
- container: ''
  name: amis
  type: string
- container: ''
  name: architecture
  type: string
- container: ''
  name: architectures
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: author
  type: string
- container: ''
  name: autoEnable
  type: string
- container: ''
  name: awsAccountId
  type: string
- container: ''
  name: awsEcrContainerAggregation
  type: string
- container: ''
  name: baseScore
  type: string
- container: ''
  name: bucketName
  type: string
- container: ''
  name: codeSha256
  type: string
- container: ''
  name: codeSnippet
  type: string
- container: ''
  name: codeSnippetResults
  type: string
- container: ''
  name: codeVulnerabilityDetectorName
  type: string
- container: ''
  name: codeVulnerabilityDetectorTags
  type: string
- container: ''
  name: codeVulnerabilityFilePath
  type: string
- container: ''
  name: comparison
  type: string
- container: ''
  name: componentId
  type: string
- container: ''
  name: componentType
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: count
  type: string
- container: ''
  name: countsByGroup
  type: string
- container: ''
  name: coveredResources
  type: string
- container: ''
  name: critical
  type: string
- container: ''
  name: cvssSource
  type: string
- container: ''
  name: cwes
  type: string
- container: ''
  name: dateAdded
  type: string
- container: ''
  name: dateDue
  type: string
- container: ''
  name: delegatedAdmin
  type: string
- container: ''
  name: delegatedAdminAccountId
  type: string
- container: ''
  name: delegatedAdminAccounts
  type: string
- container: ''
  name: destination
  type: string
- container: ''
  name: detectorId
  type: string
- container: ''
  name: detectorName
  type: string
- container: ''
  name: detectorTags
  type: string
- container: ''
  name: ec2
  type: string
- container: ''
  name: ec2InstanceAggregation
  type: string
- container: ''
  name: ec2InstanceImageId
  type: string
- container: ''
  name: ec2InstanceSubnetId
  type: string
- container: ''
  name: ec2InstanceTags
  type: string
- container: ''
  name: ec2InstanceVpcId
  type: string
- container: ''
  name: ecr
  type: string
- container: ''
  name: ecrConfiguration
  type: string
- container: ''
  name: ecrImage
  type: string
- container: ''
  name: ecrImageArchitecture
  type: string
- container: ''
  name: ecrImageHash
  type: string
- container: ''
  name: ecrImagePushedAt
  type: string
- container: ''
  name: ecrImageRegistry
  type: string
- container: ''
  name: ecrImageRepositoryName
  type: string
- container: ''
  name: ecrImageTags
  type: string
- container: ''
  name: ecrRepository
  type: string
- container: ''
  name: ecrRepositoryName
  type: string
- container: ''
  name: endInclusive
  type: string
- container: ''
  name: endLine
  type: string
- container: ''
  name: epssScore
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: errors
  type: string
- container: ''
  name: executionRoleArn
  type: string
- container: ''
  name: exploitAvailable
  type: string
- container: ''
  name: failedAccountIds
  type: string
- container: ''
  name: failedAccounts
  type: string
- container: ''
  name: fileName
  type: string
- container: ''
  name: filePath
  type: string
- container: ''
  name: filterCriteria
  type: string
- container: ''
  name: filters
  type: string
- container: ''
  name: findingArn
  type: string
- container: ''
  name: findingArns
  type: string
- container: ''
  name: findingDetails
  type: string
- container: ''
  name: findingStatus
  type: string
- container: ''
  name: findingType
  type: string
- container: ''
  name: findingTypeAggregation
  type: string
- container: ''
  name: findings
  type: string
- container: ''
  name: firstObservedAt
  type: dateTime
- container: ''
  name: firstSeen
  type: string
- container: ''
  name: fixAvailable
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: functionName
  type: string
- container: ''
  name: functionNames
  type: string
- container: ''
  name: functionTags
  type: string
- container: ''
  name: groupKey
  type: string
- container: ''
  name: high
  type: string
- container: ''
  name: iamInstanceProfileArn
  type: string
- container: ''
  name: imageHash
  type: string
- container: ''
  name: imageId
  type: string
- container: ''
  name: imageLayerAggregation
  type: string
- container: ''
  name: imageSha
  type: string
- container: ''
  name: imageShas
  type: string
- container: ''
  name: imageTags
  type: string
- container: ''
  name: inspectorScore
  type: string
- container: ''
  name: instanceId
  type: string
- container: ''
  name: instanceIds
  type: string
- container: ''
  name: instanceTags
  type: string
- container: ''
  name: ipV4Addresses
  type: string
- container: ''
  name: ipV6Addresses
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: keyName
  type: string
- container: ''
  name: keyPrefix
  type: string
- container: ''
  name: kmsKeyArn
  type: string
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: lambda
  type: string
- container: ''
  name: lambdaCode
  type: string
- container: ''
  name: lambdaFunction
  type: string
- container: ''
  name: lambdaFunctionAggregation
  type: string
- container: ''
  name: lambdaFunctionExecutionRoleArn
  type: string
- container: ''
  name: lambdaFunctionLastModifiedAt
  type: string
- container: ''
  name: lambdaFunctionLayers
  type: string
- container: ''
  name: lambdaFunctionName
  type: string
- container: ''
  name: lambdaFunctionRuntime
  type: string
- container: ''
  name: lambdaFunctionTags
  type: string
- container: ''
  name: lambdaLayerAggregation
  type: string
- container: ''
  name: lambdaTags
  type: string
- container: ''
  name: lastModifiedAt
  type: string
- container: ''
  name: lastObservedAt
  type: dateTime
- container: ''
  name: lastScannedAt
  type: string
- container: ''
  name: lastSeen
  type: string
- container: ''
  name: launchedAt
  type: string
- container: ''
  name: layerArn
  type: string
- container: ''
  name: layerArns
  type: string
- container: ''
  name: layerHash
  type: string
- container: ''
  name: layerHashes
  type: string
- container: ''
  name: layers
  type: string
- container: ''
  name: lineNumber
  type: string
- container: ''
  name: maxAccountLimitReached
  type: string
- container: ''
  name: medium
  type: string
- container: ''
  name: member
  type: string
- container: ''
  name: members
  type: string
- container: ''
  name: metric
  type: string
- container: ''
  name: networkFindings
  type: string
- container: ''
  name: networkProtocol
  type: string
- container: ''
  name: networkReachabilityDetails
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: operatingSystem
  type: string
- container: ''
  name: operatingSystems
  type: string
- container: ''
  name: orgPackagePaths
  type: string
- container: ''
  name: packageAggregation
  type: string
- container: ''
  name: packageName
  type: string
- container: ''
  name: packageNames
  type: string
- container: ''
  name: packagePaths
  type: string
- container: ''
  name: packageType
  type: string
- container: ''
  name: packageVulnerabilityDetails
  type: string
- container: ''
  name: permissions
  type: string
- container: ''
  name: platform
  type: string
- container: ''
  name: portRange
  type: string
- container: ''
  name: pushedAt
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: referenceUrls
  type: string
- container: ''
  name: registry
  type: string
- container: ''
  name: relatedVulnerabilities
  type: string
- container: ''
  name: relationshipStatus
  type: string
- container: ''
  name: remediation
  type: string
- container: ''
  name: reportFormat
  type: string
- container: ''
  name: reportId
  type: string
- container: ''
  name: repositories
  type: string
- container: ''
  name: repository
  type: string
- container: ''
  name: repositoryAggregation
  type: string
- container: ''
  name: repositoryName
  type: string
- container: ''
  name: resourceFilterCriteria
  type: string
- container: ''
  name: resourceId
  type: string
- container: ''
  name: resourceIds
  type: string
- container: ''
  name: resourceMetadata
  type: string
- container: ''
  name: resourceState
  type: string
- container: ''
  name: resourceStatus
  type: string
- container: ''
  name: resourceTags
  type: string
- container: ''
  name: resourceType
  type: string
- container: set
  name: resources
  type: string
- container: ''
  name: responses
  type: string
- container: ''
  name: ruleId
  type: string
- container: ''
  name: runtime
  type: string
- container: ''
  name: runtimes
  type: string
- container: ''
  name: s3Destination
  type: string
- container: ''
  name: scanStatus
  type: string
- container: ''
  name: scanStatusCode
  type: string
- container: ''
  name: scanStatusReason
  type: string
- container: ''
  name: scanType
  type: string
- container: ''
  name: score
  type: string
- container: ''
  name: scoreSource
  type: string
- container: ''
  name: scoringVector
  type: string
- container: ''
  name: securityGroupIds
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: severityCounts
  type: string
- container: ''
  name: sortBy
  type: string
- container: ''
  name: sortOrder
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: sourceLambdaLayerArn
  type: string
- container: ''
  name: startInclusive
  type: string
- container: ''
  name: startLine
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusCode
  type: string
- container: ''
  name: subnetId
  type: string
- container: ''
  name: subnetIds
  type: string
- container: ''
  name: suggestedFixes
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: targets
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: titleAggregation
  type: string
- container: ''
  name: titles
  type: string
- container: ''
  name: totalCounts
  type: string
- container: ''
  name: totals
  type: string
- container: ''
  name: ttps
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: value
  type: string
- container: ''
  name: vendorSeverity
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: vpcConfig
  type: string
- container: ''
  name: vpcId
  type: string
- container: ''
  name: vulnerabilities
  type: string
- container: ''
  name: vulnerabilityId
  type: string
- container: ''
  name: vulnerabilityIds
  type: string
- container: ''
  name: vulnerabilitySource
  type: string
- container: ''
  name: vulnerablePackages
  type: string
property_count: 226
provider_name: Amazon Inspector
provider_slug: amazon-inspector
slug: amazon-inspector-context
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
- JSON-LD
- Linked Data
- Semantic Web
---
