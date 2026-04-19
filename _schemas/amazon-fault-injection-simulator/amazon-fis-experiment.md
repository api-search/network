---
description: A fault injection experiment instance
layout: schema
name: Experiment
properties_list:
- description: Experiment ID
  name: id
  type: string
- description: Experiment ARN
  name: arn
  type: string
- description: Source template ID
  name: experimentTemplateId
  type: string
- description: IAM role used
  name: roleArn
  type: string
- description: ''
  name: state
  type: object
- description: Resolved targets
  name: targets
  type: object
- description: Experiment actions
  name: actions
  type: object
- description: Stop conditions
  name: stopConditions
  type: array
- description: Experiment start time
  name: startTime
  type: string
- description: Experiment end time
  name: endTime
  type: string
- description: Resource tags
  name: tags
  type: object
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
schema_file: json-schema/amazon-fis-experiment-schema.json
slug: amazon-fis-experiment
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
title: Experiment
---
