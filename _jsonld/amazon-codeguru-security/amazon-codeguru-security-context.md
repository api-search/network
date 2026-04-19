---
class_count: 49
classes:
- BatchGetFindingsResponse
- FindingIdentifier
- CreateScanResponse
- CreateUploadUrlResponse
- GetAccountConfigurationResponse
- GetFindingsResponse
- GetMetricsSummaryResponse
- GetScanResponse
- ListFindingsMetricsResponse
- ListScansResponse
- ListTagsForResourceResponse
- TagResourceResponse
- UntagResourceResponse
- UpdateAccountConfigurationResponse
- FindingMetricsValuePerSeverity
- AccountFindingsMetric
- BatchGetFindingsError
- BatchGetFindingsRequest
- CategoryWithFindingNum
- CodeLine
- ResourceId
- TagMap
- CreateScanRequest
- CreateUploadUrlRequest
- RequestHeaderMap
- EncryptionConfig
- FilePath
- Remediation
- Resource
- Vulnerability
- Finding
- GetAccountConfigurationRequest
- GetFindingsRequest
- GetMetricsSummaryRequest
- MetricsSummary
- GetScanRequest
- ListFindingsMetricsRequest
- ListScansRequest
- ListTagsForResourceRequest
- Recommendation
- ScanNameWithFindingNum
- ScanSummary
- SuggestedFix
- TagResourceRequest
- UntagResourceRequest
- UpdateAccountConfigurationRequest
- name
- description
- url
context_file: json-ld/amazon-codeguru-security-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-security/refs/heads/main/json-ld/amazon-codeguru-security-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codeguru Security from Amazon CodeGuru Security.
layout: jsonld
name: Amazon Codeguru Security Context
namespaces:
- prefix: amazon-code-guru-security
  uri: https://amazon-code-guru-security.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: failedFindings
  type: string
- container: ''
  name: findings
  type: string
- container: ''
  name: findingId
  type: string
- container: ''
  name: scanName
  type: string
- container: ''
  name: resourceId
  type: string
- container: ''
  name: runId
  type: string
- container: ''
  name: scanNameArn
  type: string
- container: ''
  name: scanState
  type: string
- container: ''
  name: codeArtifactId
  type: string
- container: ''
  name: requestHeaders
  type: string
- container: ''
  name: s3Url
  type: string
- container: ''
  name: encryptionConfig
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: metricsSummary
  type: string
- container: ''
  name: analysisType
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: numberOfRevisions
  type: string
- container: ''
  name: updatedAt
  type: string
- container: ''
  name: findingsMetrics
  type: string
- container: ''
  name: summaries
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: critical
  type: string
- container: ''
  name: high
  type: string
- container: ''
  name: info
  type: string
- container: ''
  name: low
  type: string
- container: ''
  name: medium
  type: string
- container: ''
  name: closedFindings
  type: string
- container: ''
  name: date
  type: string
- container: ''
  name: meanTimeToClose
  type: string
- container: ''
  name: newFindings
  type: string
- container: ''
  name: openFindings
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: findingIdentifiers
  type: string
- container: ''
  name: categoryName
  type: string
- container: ''
  name: findingNumber
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: scanType
  type: string
- container: ''
  name: kmsKeyArn
  type: string
- container: ''
  name: codeSnippet
  type: string
- container: ''
  name: endLine
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: startLine
  type: string
- container: ''
  name: recommendation
  type: string
- container: ''
  name: suggestedFixes
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: subResourceId
  type: string
- container: ''
  name: filePath
  type: string
- container: ''
  name: itemCount
  type: string
- container: ''
  name: referenceUrls
  type: string
- container: ''
  name: relatedVulnerabilities
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
  name: generatorId
  type: string
- container: ''
  name: remediation
  type: string
- container: ''
  name: resource
  type: string
- container: ''
  name: ruleId
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: vulnerability
  type: string
- container: ''
  name: categoriesWithMostFindings
  type: string
- container: ''
  name: scansWithMostOpenCriticalFindings
  type: string
- container: ''
  name: scansWithMostOpenFindings
  type: string
- container: ''
  name: text
  type: string
- container: ''
  name: code
  type: string
property_count: 70
provider_name: Amazon CodeGuru Security
provider_slug: amazon-codeguru-security
slug: amazon-codeguru-security-context
tags:
- Amazon
- AWS
- Security
- SAST
- Code Analysis
- DevSecOps
- Developer Tools
- JSON-LD
- Linked Data
- Semantic Web
---
