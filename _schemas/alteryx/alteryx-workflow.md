---
description: Schema for an Alteryx Server workflow resource as returned by the Alteryx Server API V3. Represents workflows uploaded to and managed on Alteryx Server, including version history, execution settings, and access permissions.
layout: schema
name: Alteryx Workflow
properties_list:
- description: Unique identifier for the workflow assigned by Alteryx Server.
  name: id
  type: string
- description: Source application identifier used for migration tracking between Server environments.
  name: sourceAppId
  type: string
- description: Display name of the workflow.
  name: name
  type: string
- description: Unique identifier of the user who owns the workflow.
  name: ownerId
  type: string
- description: ISO 8601 date and time when the workflow was first created on the server.
  name: dateCreated
  type: string
- description: Version number of the currently published version of the workflow.
  name: publishedVersionNumber
  type: integer
- description: Unique identifier of the currently published workflow version.
  name: publishedVersionId
  type: string
- description: Indicates whether the workflow uses the AMP (Alteryx Multi-threaded Processing) engine.
  name: isAmp
  type: boolean
- description: Execution mode controlling which tools and operations are permitted. Safe mode restricts potentially dangerous operations, SemiSafe allows some, and Standard allows all.
  name: executionMode
  type: string
- description: Total number of times the workflow has been executed.
  name: runCount
  type: integer
- description: Worker tag used to route execution to specific worker nodes.
  name: workerTag
  type: string
- description: District tags assigned to the workflow for organizational grouping.
  name: districtTags
  type: array
- description: User-provided comments or notes about the workflow.
  name: comments
  type: string
- description: Whether the workflow is publicly accessible to all Server users.
  name: isPublic
  type: boolean
- description: Whether the workflow is flagged as ready for migration to another Server environment.
  name: isReadyForMigration
  type: boolean
- description: Whether users other than the owner may download the workflow package.
  name: othersMayDownload
  type: boolean
- description: Whether users other than the owner can view execution history.
  name: othersCanViewHistory
  type: boolean
- description: Whether users other than the owner can execute the workflow.
  name: othersCanExecute
  type: boolean
- description: Whether the workflow has an exemption from private data restrictions.
  name: hasPrivateDataExemption
  type: boolean
- description: Specifies how credentials are handled for workflow execution. Default uses the system default, Required prompts the user, and Specific uses a designated credential.
  name: workflowCredentialType
  type: string
- description: Identifier of the specific credential to use when workflowCredentialType is set to Specific.
  name: credentialId
  type: string
- description: List of all versions of this workflow.
  name: versions
  type: array
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-workflow-schema.json
slug: alteryx-workflow
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: Alteryx Workflow
---
