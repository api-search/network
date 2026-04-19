---
description: A lifecycle action hook for a source server
layout: schema
name: SourceServerAction
properties_list:
- description: Action ID
  name: actionID
  type: string
- description: Action name
  name: actionName
  type: string
- description: Whether the action is active
  name: active
  type: boolean
- description: Action category
  name: category
  type: string
- description: Action description
  name: description
  type: string
- description: SSM document identifier
  name: documentIdentifier
  type: string
- description: SSM document version
  name: documentVersion
  type: string
- description: External parameters for the action
  name: externalParameters
  type: object
- description: Whether action must succeed for cutover
  name: mustSucceedForCutover
  type: boolean
- description: Execution order
  name: order
  type: integer
- description: Action parameters
  name: parameters
  type: object
- description: Timeout in seconds
  name: timeoutSeconds
  type: integer
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-source-server-action-schema.json
slug: application-migration-service-source-server-action
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: SourceServerAction
---
