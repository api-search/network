---
class_count: 9
classes:
- Pipeline
- CreatePipelineInput
- StageDeclaration
- ActionDeclaration
- PipelineExecution
- PipelineList
- Tag
- name
- version
context_file: json-ld/amazon-codepipeline-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codepipeline/refs/heads/main/json-ld/amazon-codepipeline-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codepipeline from Amazon CodePipeline.
layout: jsonld
name: Amazon Codepipeline Context
namespaces:
- prefix: amazon-code-pipeline
  uri: https://amazon-code-pipeline.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: roleArn
  type: string
- container: set
  name: stages
  type: string
- container: ''
  name: pipeline
  type: string
- container: set
  name: tags
  type: string
- container: set
  name: actions
  type: string
- container: ''
  name: actionTypeId
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: provider
  type: string
- container: ''
  name: configuration
  type: string
- container: set
  name: inputArtifacts
  type: string
- container: set
  name: outputArtifacts
  type: string
- container: ''
  name: pipelineName
  type: string
- container: ''
  name: pipelineExecutionId
  type: string
- container: ''
  name: pipelineVersion
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: statusSummary
  type: string
- container: set
  name: pipelines
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: updated
  type: dateTime
- container: ''
  name: nextToken
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
property_count: 23
provider_name: Amazon CodePipeline
provider_slug: amazon-codepipeline
slug: amazon-codepipeline-context
tags:
- Amazon
- AWS
- CI/CD
- Continuous Delivery
- DevOps
- Pipeline
- Release Automation
- JSON-LD
- Linked Data
- Semantic Web
---
