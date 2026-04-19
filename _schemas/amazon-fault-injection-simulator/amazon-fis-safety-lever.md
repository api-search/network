---
description: A safety mechanism that can stop or prevent FIS experiments
layout: schema
name: SafetyLever
properties_list:
- description: Safety lever ID
  name: id
  type: string
- description: Safety lever ARN
  name: arn
  type: string
- description: ''
  name: state
  type: object
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
schema_file: json-schema/amazon-fis-safety-lever-schema.json
slug: amazon-fis-safety-lever
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
title: SafetyLever
---
