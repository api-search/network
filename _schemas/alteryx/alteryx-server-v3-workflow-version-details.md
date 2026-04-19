---
description: Metadata details for a workflow version
layout: schema
name: WorkflowVersionDetails
properties_list:
- description: Whether the version uses AMP engine
  name: isAmp
  type: boolean
- description: Name of the workflow file
  name: fileName
  type: string
- description: Author of the workflow
  name: author
  type: string
- description: Copyright information
  name: copyright
  type: string
- description: Description of the workflow
  name: description
  type: string
- description: Display name of the workflow
  name: name
  type: string
- description: Message shown when no output files are generated
  name: noOutputFilesMessage
  type: string
- description: Message shown with output files
  name: outputMessage
  type: string
- description: Related URL
  name: url
  type: string
- description: Display text for the related URL
  name: urlText
  type: string
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-workflow-version-details-schema.json
slug: alteryx-server-v3-workflow-version-details
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: WorkflowVersionDetails
---
