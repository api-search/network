---
description: Action definition in an experiment template
layout: schema
name: ExperimentTemplateAction
properties_list:
- description: FIS action ID
  name: actionId
  type: string
- description: Action description
  name: description
  type: string
- description: Action parameters
  name: parameters
  type: object
- description: Target mappings
  name: targets
  type: object
- description: Actions that must complete first
  name: startAfter
  type: array
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
schema_file: json-schema/amazon-fis-experiment-template-action-schema.json
slug: amazon-fis-experiment-template-action
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
title: ExperimentTemplateAction
---
