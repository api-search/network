---
description: Summary representation of an Alteryx workflow
layout: schema
name: WorkflowSummary
properties_list:
- description: Unique workflow identifier
  name: id
  type: string
- description: Source application identifier for migration tracking
  name: sourceAppId
  type: string
- description: Name of the workflow
  name: name
  type: string
- description: ID of the workflow owner
  name: ownerId
  type: string
- description: Date the workflow was created (ISO 8601)
  name: dateCreated
  type: string
- description: Version number of the published version
  name: publishedVersionNumber
  type: integer
- description: Whether the workflow uses AMP engine
  name: isAmp
  type: boolean
- description: Execution mode for the workflow
  name: executionMode
  type: string
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-workflow-summary-schema.json
slug: alteryx-server-v3-workflow-summary
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: WorkflowSummary
---
