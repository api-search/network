---
class_count: 0
classes: []
context_file: json-ld/amazon-data-pipeline-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/json-ld/amazon-data-pipeline-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Data Pipeline from Amazon Data Pipeline.
layout: jsonld
name: Amazon Data Pipeline Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/datapipeline/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Pipeline
  type: ''
- container: ''
  name: PipelineObject
  type: ''
- container: ''
  name: PipelineDescription
  type: ''
- container: ''
  name: Field
  type: ''
- container: ''
  name: Tag
  type: ''
- container: ''
  name: ValidationError
  type: ''
- container: ''
  name: pipelineId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: uniqueId
  type: string
- container: ''
  name: pipelineState
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: stringValue
  type: string
- container: ''
  name: refValue
  type: string
- container: set
  name: fields
  type: ''
- container: set
  name: tags
  type: ''
- container: set
  name: pipelineObjects
  type: ''
- container: set
  name: pipelineIdList
  type: ''
- container: set
  name: pipelineDescriptionList
  type: ''
- container: ''
  name: hasMoreResults
  type: boolean
- container: ''
  name: marker
  type: string
- container: ''
  name: errored
  type: boolean
- container: set
  name: validationErrors
  type: ''
- container: set
  name: validationWarnings
  type: ''
- container: ''
  name: startTimestamp
  type: dateTime
- container: ''
  name: cancelActive
  type: boolean
- container: ''
  name: sphere
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: code
  type: string
property_count: 30
provider_name: Amazon Data Pipeline
provider_slug: amazon-data-pipeline
slug: amazon-data-pipeline-context
tags:
- AWS
- Data Processing
- ETL
- Workflows
- Data Pipeline
- Automation
- JSON-LD
- Linked Data
- Semantic Web
---
