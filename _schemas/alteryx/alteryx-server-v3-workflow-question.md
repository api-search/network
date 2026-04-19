---
description: An analytic app question (input parameter)
layout: schema
name: WorkflowQuestion
properties_list:
- description: Name of the question
  name: name
  type: string
- description: Type of the question input
  name: questionType
  type: string
- description: Description of the question
  name: description
  type: string
- description: Default value
  name: value
  type: string
- description: Whether multiple selections are allowed
  name: multiple
  type: boolean
- description: Available options for the question
  name: items
  type: array
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-workflow-question-schema.json
slug: alteryx-server-v3-workflow-question
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: WorkflowQuestion
---
