---
description: ''
layout: schema
name: Deployment
properties_list:
- description: Deployment identifier
  name: id
  type: string
- description: Configuration used for this deployment
  name: configurationId
  type: string
- description: Associated scenario
  name: scenarioId
  type: string
- description: Current deployment status
  name: status
  type: string
- description: URL for sending inference requests
  name: deploymentUrl
  type: string
- description: ''
  name: createdAt
  type: string
- description: ''
  name: modifiedAt
  type: string
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-ai-core-deployment-schema.json
slug: sap-ai-core-deployment
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: Deployment
---
