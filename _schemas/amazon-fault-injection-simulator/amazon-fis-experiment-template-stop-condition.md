---
description: Stop condition for an experiment
layout: schema
name: ExperimentTemplateStopCondition
properties_list:
- description: Stop condition source
  name: source
  type: string
- description: CloudWatch alarm ARN or none
  name: value
  type: string
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
schema_file: json-schema/amazon-fis-experiment-template-stop-condition-schema.json
slug: amazon-fis-experiment-template-stop-condition
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
title: ExperimentTemplateStopCondition
---
