---
description: Contract for updating an existing workflow
layout: schema
name: UpdateWorkflowContract
properties_list:
- description: Updated workflow name
  name: name
  type: string
- description: Version ID to update
  name: versionId
  type: string
- description: Whether to make the specified version published
  name: makePublished
  type: boolean
- description: Updated owner ID
  name: ownerId
  type: string
- description: Updated worker tag
  name: workerTag
  type: string
- description: Updated district tags
  name: districtTags
  type: array
- description: Updated comments
  name: comments
  type: string
- description: ''
  name: isPublic
  type: boolean
- description: ''
  name: isReadyForMigration
  type: boolean
- description: ''
  name: othersMayDownload
  type: boolean
- description: ''
  name: othersCanExecute
  type: boolean
- description: ''
  name: executionMode
  type: string
- description: ''
  name: hasPrivateDataExemption
  type: boolean
- description: ''
  name: workflowCredentialType
  type: string
- description: ''
  name: credentialId
  type: string
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-update-workflow-contract-schema.json
slug: alteryx-server-v3-update-workflow-contract
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: UpdateWorkflowContract
---
