---
class_count: 13
classes:
- ExperimentTemplateTarget
- TargetResourceType
- description
- ExperimentTemplateStopCondition
- ExperimentState
- SafetyLeverState
- SafetyLever
- ExperimentTemplate
- creationTime
- lastUpdateTime
- Action
- ExperimentTemplateAction
- Experiment
context_file: json-ld/amazon-fis-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/json-ld/amazon-fis-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Fis from Amazon Fault Injection Simulator.
layout: jsonld
name: Amazon Fis Context
namespaces:
- prefix: fis
  uri: https://aws.amazon.com/fis/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: resourceType
  type: string
- container: set
  name: resourceArns
  type: string
- container: ''
  name: resourceTags
  type: reference
- container: set
  name: filters
  type: reference
- container: ''
  name: selectionMode
  type: string
- container: ''
  name: parameters
  type: reference
- container: ''
  name: source
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: targets
  type: reference
- container: ''
  name: actions
  type: reference
- container: set
  name: stopConditions
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: tags
  type: reference
- container: ''
  name: actionId
  type: string
- container: set
  name: startAfter
  type: string
- container: ''
  name: experimentTemplateId
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: endTime
  type: dateTime
property_count: 23
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
slug: amazon-fis-context
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
- JSON-LD
- Linked Data
- Semantic Web
---
