---
description: A Conductor workflow definition that describes the orchestration of tasks, their sequencing, input/output mappings, failure handling, and timeout policies.
layout: schema
name: WorkflowDef
properties_list:
- description: The name of the workflow definition
  name: name
  type: string
- description: Description of the workflow
  name: description
  type: string
- description: The version of the workflow definition
  name: version
  type: integer
- description: The list of tasks in the workflow
  name: tasks
  type: array
- description: List of input parameter names for the workflow
  name: inputParameters
  type: array
- description: Mapping of output parameters
  name: outputParameters
  type: object
- description: Name of the workflow to execute when this workflow fails
  name: failureWorkflow
  type: string
- description: Schema version (currently 2)
  name: schemaVersion
  type: integer
- description: Whether the workflow is restartable
  name: restartable
  type: boolean
- description: Whether to enable workflow status listener
  name: workflowStatusListenerEnabled
  type: boolean
- description: Email of the workflow definition owner
  name: ownerEmail
  type: string
- description: Timeout policy for the workflow
  name: timeoutPolicy
  type: string
- description: Timeout in seconds for the workflow
  name: timeoutSeconds
  type: integer
- description: Workflow level variables
  name: variables
  type: object
- description: Default input template
  name: inputTemplate
  type: object
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/workflow-def.json
slug: workflow-def
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: WorkflowDef
---
