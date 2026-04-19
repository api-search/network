---
description: Represents an Amazon Step Functions state machine with its associated configuration, definition, and metadata.
layout: schema
name: Amazon Step Functions State Machine
properties_list:
- description: The ARN that identifies the state machine
  name: stateMachineArn
  type: string
- description: The name of the state machine
  name: name
  type: string
- description: The current status of the state machine
  name: status
  type: string
- description: The Amazon States Language definition of the state machine as a JSON string
  name: definition
  type: string
- description: The ARN of the IAM role used by the state machine for executions
  name: roleArn
  type: string
- description: The type of the state machine (STANDARD or EXPRESS)
  name: type
  type: string
- description: The date the state machine was created
  name: creationDate
  type: string
- description: ''
  name: loggingConfiguration
  type: object
- description: ''
  name: tracingConfiguration
  type: object
- description: A user-defined or auto-generated string that identifies a Map state
  name: label
  type: string
- description: The revision identifier for the state machine
  name: revisionId
  type: string
- description: A user-defined description of the state machine
  name: description
  type: string
- description: Tags attached to the state machine
  name: tags
  type: array
provider_name: Amazon Step Functions
provider_slug: amazon-step-functions
schema_file: json-schema/amazon-step-functions-state-machine-schema.json
slug: amazon-step-functions-state-machine
tags:
- AWS
- Orchestration
- Serverless
- State Machine
- Workflow
title: Amazon Step Functions State Machine
---
