---
description: TriggerConfig schema from Amazon AppFlow API
layout: schema
name: TriggerConfig
properties_list:
- description: Specifies the type of flow trigger. It can be OnDemand, Scheduled, or Event.
  name: triggerType
  type: string
- description: Specifies the configuration details of a schedule-triggered flow as defined by the user.
  name: triggerProperties
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-trigger-config-schema.json
slug: appflow-trigger-config
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: TriggerConfig
---
