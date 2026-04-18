---
description: ''
layout: schema
name: RollbackConfiguration
properties_list:
- description: The triggers to monitor during stack creation or update.
  name: RollbackTriggers
  type: array
- description: The amount of time to monitor after stack deployment.
  name: MonitoringTimeInMinutes
  type: integer
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-rollback-configuration-schema.json
slug: cloudformation-rollback-configuration
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: RollbackConfiguration
---
