---
description: Detailed representation of an Alteryx workflow including versions
layout: schema
name: WorkflowDetail
properties_list:
- description: Unique workflow identifier
  name: id
  type: string
- description: Source application identifier
  name: sourceAppId
  type: string
- description: Date the workflow was created
  name: dateCreated
  type: string
- description: Total number of times the workflow has been executed
  name: runCount
  type: integer
- description: List of workflow versions
  name: versions
  type: array
- description: Name of the workflow
  name: name
  type: string
- description: ID of the workflow owner
  name: ownerId
  type: string
- description: Worker tag for execution routing
  name: workerTag
  type: string
- description: District tags assigned to the workflow
  name: districtTags
  type: array
- description: Comments about the workflow
  name: comments
  type: string
- description: Whether the workflow is publicly accessible
  name: isPublic
  type: boolean
- description: Whether the workflow is ready for migration
  name: isReadyForMigration
  type: boolean
- description: ID of the currently published version
  name: publishedVersionId
  type: string
- description: Whether other users may download the workflow
  name: othersMayDownload
  type: boolean
- description: Whether other users can view execution history
  name: othersCanViewHistory
  type: boolean
- description: Whether other users can execute the workflow
  name: othersCanExecute
  type: boolean
- description: Whether the workflow has a private data exemption
  name: hasPrivateDataExemption
  type: boolean
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-workflow-detail-schema.json
slug: alteryx-server-v3-workflow-detail
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: WorkflowDetail
---
