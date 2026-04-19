---
description: An experiment template defining fault injection targets, actions, and stop conditions
layout: schema
name: ExperimentTemplate
properties_list:
- description: Template ID
  name: id
  type: string
- description: Template ARN
  name: arn
  type: string
- description: Template description
  name: description
  type: string
- description: Target definitions
  name: targets
  type: object
- description: Action definitions
  name: actions
  type: object
- description: Stop conditions
  name: stopConditions
  type: array
- description: Template creation time
  name: creationTime
  type: string
- description: Last update time
  name: lastUpdateTime
  type: string
- description: IAM role ARN for experiment execution
  name: roleArn
  type: string
- description: Resource tags
  name: tags
  type: object
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
schema_file: json-schema/amazon-fis-experiment-template-schema.json
slug: amazon-fis-experiment-template
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
title: ExperimentTemplate
---
