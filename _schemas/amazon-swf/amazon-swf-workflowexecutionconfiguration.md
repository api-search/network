---
description: The configuration settings for a workflow execution including timeout values, tasklist etc. These configuration settings are determined from the defaults specified when registering the workflow type and those specified when starting the workflow execution.
layout: schema
name: WorkflowExecutionConfiguration
properties_list:
- description: ''
  name: taskStartToCloseTimeout
  type: object
- description: ''
  name: executionStartToCloseTimeout
  type: object
- description: ''
  name: taskList
  type: object
- description: ''
  name: taskPriority
  type: object
- description: ''
  name: childPolicy
  type: object
- description: ''
  name: lambdaRole
  type: object
provider_name: Amazon Simple Workflow Service
provider_slug: amazon-swf
schema_file: json-schema/amazon-swf-workflowexecutionconfiguration-schema.json
slug: amazon-swf-workflowexecutionconfiguration
tags:
- Automation
- AWS
- Task Coordination
- Workflow
title: WorkflowExecutionConfiguration
---
