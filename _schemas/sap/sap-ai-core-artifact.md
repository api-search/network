---
description: ''
layout: schema
name: Artifact
properties_list:
- description: Artifact identifier
  name: id
  type: string
- description: Artifact name
  name: name
  type: string
- description: Artifact kind
  name: kind
  type: string
- description: Storage URL for the artifact
  name: url
  type: string
- description: Associated scenario
  name: scenarioId
  type: string
- description: Execution that produced this artifact
  name: executionId
  type: string
- description: Artifact description
  name: description
  type: string
- description: ''
  name: createdAt
  type: string
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-ai-core-artifact-schema.json
slug: sap-ai-core-artifact
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: Artifact
---
