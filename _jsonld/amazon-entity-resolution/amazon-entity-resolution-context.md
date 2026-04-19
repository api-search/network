---
class_count: 49
classes:
- CreateMatchingWorkflowInput
- description
- CreateMatchingWorkflowOutput
- CreateSchemaMappingInput
- CreateSchemaMappingOutput
- DeleteMatchingWorkflowInput
- DeleteMatchingWorkflowOutput
- DeleteSchemaMappingInput
- DeleteSchemaMappingOutput
- ErrorDetails
- GetMatchIdInput
- GetMatchIdOutput
- GetMatchingJobInput
- GetMatchingJobOutput
- GetMatchingWorkflowInput
- GetMatchingWorkflowOutput
- GetSchemaMappingInput
- GetSchemaMappingOutput
- IncrementalRunConfig
- InputSource
- JobMetrics
- JobSummary
- ListMatchingJobsInput
- ListMatchingJobsOutput
- ListMatchingWorkflowsInput
- ListMatchingWorkflowsOutput
- ListSchemaMappingsInput
- ListSchemaMappingsOutput
- ListTagsForResourceInput
- ListTagsForResourceOutput
- MatchingWorkflowSummary
- OutputAttribute
- name
- OutputSource
- RecordAttributeMap
- ResolutionTechniques
- RuleBasedProperties
- Rule
- SchemaInputAttribute
- SchemaMappingSummary
- StartMatchingJobInput
- StartMatchingJobOutput
- TagMap
- TagResourceInput
- TagResourceOutput
- UntagResourceInput
- UntagResourceOutput
- UpdateMatchingWorkflowInput
- UpdateMatchingWorkflowOutput
context_file: json-ld/amazon-entity-resolution-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-entity-resolution/refs/heads/main/json-ld/amazon-entity-resolution-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Entity Resolution from Amazon Entity Resolution.
layout: jsonld
name: Amazon Entity Resolution Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: incrementalRunConfig
  type: string
- container: ''
  name: inputSourceConfig
  type: string
- container: ''
  name: outputSourceConfig
  type: string
- container: ''
  name: resolutionTechniques
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: workflowName
  type: string
- container: ''
  name: workflowArn
  type: string
- container: ''
  name: mappedInputFields
  type: string
- container: ''
  name: schemaName
  type: string
- container: ''
  name: schemaArn
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: record
  type: string
- container: ''
  name: matchId
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: errorDetails
  type: string
- container: ''
  name: jobId
  type: string
- container: ''
  name: metrics
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: updatedAt
  type: string
- container: ''
  name: incrementalRunType
  type: string
- container: ''
  name: applyNormalization
  type: string
- container: ''
  name: inputSourceARN
  type: string
- container: ''
  name: inputRecords
  type: string
- container: ''
  name: matchIDs
  type: string
- container: ''
  name: recordsNotProcessed
  type: string
- container: ''
  name: totalRecordsProcessed
  type: string
- container: ''
  name: jobs
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: workflowSummaries
  type: string
- container: ''
  name: schemaList
  type: string
- container: ''
  name: hashed
  type: string
- container: ''
  name: KMSArn
  type: string
- container: ''
  name: output
  type: string
- container: ''
  name: outputS3Path
  type: string
- container: ''
  name: resolutionType
  type: string
- container: ''
  name: ruleBasedProperties
  type: string
- container: ''
  name: attributeMatchingModel
  type: string
- container: ''
  name: rules
  type: string
- container: ''
  name: matchingKeys
  type: string
- container: ''
  name: ruleName
  type: string
- container: ''
  name: fieldName
  type: string
- container: ''
  name: groupName
  type: string
- container: ''
  name: matchKey
  type: string
- container: ''
  name: type
  type: string
property_count: 48
provider_name: Amazon Entity Resolution
provider_slug: amazon-entity-resolution
slug: amazon-entity-resolution-context
tags:
- Amazon Web Services
- AWS
- Data Integration
- Data Matching
- Entity Resolution
- Machine Learning
- JSON-LD
- Linked Data
- Semantic Web
---
