---
class_count: 0
classes: []
context_file: json-ld/context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/cloudformation/refs/heads/main/json-ld/context.jsonld
description: JSON-LD context defining the semantic vocabulary for context from AWS CloudFormation.
layout: jsonld
name: context Context
namespaces:
- prefix: aws
  uri: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/
- prefix: awscc
  uri: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/
- prefix: cfn
  uri: https://schemas.api.aws/cloudformation/
properties:
- container: ''
  name: Stack
  type: schema:SoftwareApplication
- container: ''
  name: Template
  type: schema:SoftwareSourceCode
- container: ''
  name: Resource
  type: schema:Thing
- container: ''
  name: ChangeSet
  type: schema:UpdateAction
- container: ''
  name: CloudControlResource
  type: schema:Thing
- container: ''
  name: ProgressEvent
  type: schema:Action
- container: ''
  name: Tag
  type: schema:DefinedTerm
- container: ''
  name: Output
  type: schema:PropertyValue
property_count: 8
provider_name: AWS CloudFormation
provider_slug: cloudformation
slug: context
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
- JSON-LD
- Linked Data
- Semantic Web
---
