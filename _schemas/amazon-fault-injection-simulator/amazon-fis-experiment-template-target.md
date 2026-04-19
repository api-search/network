---
description: Target definition in an experiment template
layout: schema
name: ExperimentTemplateTarget
properties_list:
- description: AWS resource type
  name: resourceType
  type: string
- description: Specific resource ARNs
  name: resourceArns
  type: array
- description: Tags to filter resources
  name: resourceTags
  type: object
- description: Resource filters
  name: filters
  type: array
- description: Selection mode
  name: selectionMode
  type: string
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
schema_file: json-schema/amazon-fis-experiment-template-target-schema.json
slug: amazon-fis-experiment-template-target
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
title: ExperimentTemplateTarget
---
