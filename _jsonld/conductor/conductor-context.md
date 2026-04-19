---
class_count: 7
classes:
- WorkflowDef
- TaskDef
- WorkflowExecution
- Task
- EventHandler
- EventHandlerAction
- WorkflowTask
context_file: json-ld/conductor-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/conductor/refs/heads/main/json-ld/conductor-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Conductor from Conductor.
layout: jsonld
name: Conductor Context
namespaces:
- prefix: conductor
  uri: https://conductor-oss.github.io/conductor/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: version
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: workflowId
  type: string
- container: ''
  name: workflowName
  type: string
- container: ''
  name: workflowVersion
  type: integer
- container: ''
  name: correlationId
  type: string
- container: ''
  name: taskId
  type: string
- container: ''
  name: taskType
  type: string
- container: ''
  name: taskReferenceName
  type: string
- container: ''
  name: taskDefName
  type: string
- container: ''
  name: referenceTaskName
  type: string
- container: list
  name: tasks
  type: ''
- container: list
  name: actions
  type: ''
- container: ''
  name: inputParameters
  type: ''
- container: ''
  name: outputParameters
  type: ''
- container: ''
  name: input
  type: ''
- container: ''
  name: output
  type: ''
- container: ''
  name: inputData
  type: ''
- container: ''
  name: outputData
  type: ''
- container: ''
  name: ownerEmail
  type: string
- container: ''
  name: failureWorkflow
  type: string
- container: ''
  name: timeoutPolicy
  type: string
- container: ''
  name: timeoutSeconds
  type: integer
- container: ''
  name: retryCount
  type: integer
- container: ''
  name: retryLogic
  type: string
- container: ''
  name: retryDelaySeconds
  type: integer
- container: ''
  name: startTime
  type: integer
- container: ''
  name: endTime
  type: integer
- container: ''
  name: updateTime
  type: integer
- container: ''
  name: createTime
  type: integer
- container: ''
  name: priority
  type: integer
- container: ''
  name: event
  type: string
- container: ''
  name: condition
  type: string
- container: ''
  name: active
  type: boolean
- container: ''
  name: restartable
  type: boolean
- container: ''
  name: reasonForIncompletion
  type: string
- container: ''
  name: workerId
  type: string
- container: ''
  name: parentWorkflowId
  type: string
property_count: 40
provider_name: Conductor
provider_slug: conductor
slug: conductor-context
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
- JSON-LD
- Linked Data
- Semantic Web
---
