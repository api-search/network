---
description: ''
layout: schema
name: Execution
properties_list:
- description: Execution identifier
  name: id
  type: string
- description: Configuration used for this execution
  name: configurationId
  type: string
- description: Associated scenario
  name: scenarioId
  type: string
- description: Current execution status
  name: status
  type: string
- description: Human-readable status message
  name: statusMessage
  type: string
- description: ''
  name: outputArtifacts
  type: array
- description: ''
  name: createdAt
  type: string
- description: ''
  name: modifiedAt
  type: string
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-ai-core-execution-schema.json
slug: sap-ai-core-execution
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: Execution
---
