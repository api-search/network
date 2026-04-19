---
class_count: 16
classes:
- Stack
- description
- ChangeSet
- StackResource
- Parameter
- Output
- Tag
- RollbackConfiguration
- StackDriftInformation
- StackResourceDriftInformation
- Change
- CreateStackOutput
- DescribeStacksOutput
- UpdateStackOutput
- ListStacksOutput
- CreateChangeSetOutput
context_file: json-ld/amazon-cloudformation-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudformation/refs/heads/main/json-ld/amazon-cloudformation-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloudformation from Amazon CloudFormation.
layout: jsonld
name: Amazon Cloudformation Context
namespaces:
- prefix: cloudformation
  uri: https://aws.amazon.com/cloudformation/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: stackId
  type: string
- container: ''
  name: stackName
  type: string
- container: ''
  name: changeSetId
  type: string
- container: set
  name: parameters
  type: string
- container: ''
  name: creationTime
  type: dateTime
- container: ''
  name: deletionTime
  type: dateTime
- container: ''
  name: lastUpdatedTime
  type: dateTime
- container: ''
  name: rollbackConfiguration
  type: string
- container: ''
  name: stackStatus
  type: string
- container: ''
  name: stackStatusReason
  type: string
- container: ''
  name: disableRollback
  type: boolean
- container: set
  name: notificationARNs
  type: string
- container: ''
  name: timeoutInMinutes
  type: integer
- container: set
  name: capabilities
  type: string
- container: set
  name: outputs
  type: string
- container: ''
  name: roleARN
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: enableTerminationProtection
  type: boolean
- container: ''
  name: driftInformation
  type: string
- container: ''
  name: changeSetName
  type: string
- container: ''
  name: executionStatus
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: string
- container: set
  name: changes
  type: string
- container: ''
  name: logicalResourceId
  type: string
- container: ''
  name: physicalResourceId
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: resourceStatus
  type: string
- container: ''
  name: resourceStatusReason
  type: string
- container: ''
  name: parameterKey
  type: string
- container: ''
  name: parameterValue
  type: string
- container: ''
  name: usePreviousValue
  type: boolean
- container: ''
  name: resolvedValue
  type: string
- container: ''
  name: outputKey
  type: string
- container: ''
  name: outputValue
  type: string
- container: ''
  name: exportName
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: rollbackTriggers
  type: string
- container: ''
  name: monitoringTimeInMinutes
  type: integer
- container: ''
  name: stackDriftStatus
  type: string
- container: ''
  name: lastCheckTimestamp
  type: dateTime
- container: ''
  name: stackResourceDriftStatus
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: resourceChange
  type: string
- container: set
  name: stacks
  type: string
- container: ''
  name: nextToken
  type: string
- container: set
  name: stackSummaries
  type: string
- container: ''
  name: id
  type: string
property_count: 50
provider_name: Amazon CloudFormation
provider_slug: amazon-cloudformation
slug: amazon-cloudformation-context
tags:
- AWS
- CloudFormation
- Infrastructure as Code
- DevOps
- IaC
- JSON-LD
- Linked Data
- Semantic Web
---
