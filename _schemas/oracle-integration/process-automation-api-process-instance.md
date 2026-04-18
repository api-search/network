---
description: ProcessInstance schema from Oracle Integration Process Automation API.
layout: schema
name: ProcessInstance
properties_list:
- description: Process instance identifier.
  name: processId
  type: string
- description: Process name.
  name: processName
  type: string
- description: Process definition identifier.
  name: processDefId
  type: string
- description: Process state.
  name: state
  type: string
- description: Process priority.
  name: priority
  type: integer
- description: Process title.
  name: title
  type: string
- description: User who created the instance.
  name: createdBy
  type: string
- description: Creation timestamp.
  name: createdDate
  type: string
provider_name: Oracle Integration
provider_slug: oracle-integration
schema_file: json-schema/process-automation-api-process-instance-schema.json
slug: process-automation-api-process-instance
tags:
- API Management
- Automation
- B2B Integration
- Cloud Integration
- Enterprise Integration
- Integration
- iPaaS
- Process Automation
title: ProcessInstance
---
