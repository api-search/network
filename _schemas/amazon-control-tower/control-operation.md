---
description: An operation performed on a control.
layout: schema
name: ControlOperation
properties_list:
- description: The identifier of the control.
  name: controlIdentifier
  type: string
- description: The ARN of the enabled control.
  name: enabledControlIdentifier
  type: string
- description: ''
  name: endTime
  type: string
- description: The unique identifier of the operation.
  name: operationIdentifier
  type: string
- description: The type of operation.
  name: operationType
  type: string
- description: ''
  name: startTime
  type: string
- description: The status of the operation.
  name: status
  type: string
- description: An error message if the operation failed.
  name: statusMessage
  type: string
- description: The ARN of the organizational unit.
  name: targetIdentifier
  type: string
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
schema_file: json-schema/control-operation-schema.json
slug: control-operation
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
title: ControlOperation
---
