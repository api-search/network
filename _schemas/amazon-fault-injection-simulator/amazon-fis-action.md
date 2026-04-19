---
description: An available FIS fault injection action
layout: schema
name: Action
properties_list:
- description: Action ID
  name: id
  type: string
- description: Action ARN
  name: arn
  type: string
- description: Action description
  name: description
  type: string
- description: Action parameters
  name: parameters
  type: object
- description: Target definitions
  name: targets
  type: object
- description: Resource tags
  name: tags
  type: object
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
schema_file: json-schema/amazon-fis-action-schema.json
slug: amazon-fis-action
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
title: Action
---
