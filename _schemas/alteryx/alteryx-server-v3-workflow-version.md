---
description: A specific version of a workflow
layout: schema
name: WorkflowVersion
properties_list:
- description: Unique version identifier
  name: versionId
  type: string
- description: Sequential version number
  name: versionNumber
  type: integer
- description: Date the version was created
  name: dateCreated
  type: string
- description: Source from which the version was uploaded
  name: uploadSource
  type: string
- description: Date the version was uploaded
  name: uploadDate
  type: string
- description: Type of workflow in the package
  name: packageWorkflowType
  type: string
- description: Whether this version is the published version
  name: published
  type: boolean
- description: Comments about this version
  name: comments
  type: string
- description: Whether execution is disabled for this version
  name: runDisabled
  type: boolean
- description: ''
  name: executionMode
  type: string
- description: ''
  name: workflowCredentialType
  type: string
- description: Credential ID if workflowCredentialType is Specific
  name: credentialId
  type: string
- description: ''
  name: hasPrivateDataExemption
  type: boolean
- description: ''
  name: othersMayDownload
  type: boolean
- description: ''
  name: othersCanViewHistory
  type: boolean
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-workflow-version-schema.json
slug: alteryx-server-v3-workflow-version
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: WorkflowVersion
---
