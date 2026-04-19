---
description: Status of a long-running operation such as an application package installation.
layout: schema
name: OperationStatus
properties_list:
- description: The unique identifier of the operation.
  name: id
  type: string
- description: The current status of the operation.
  name: status
  type: string
- description: The timestamp when the operation was created.
  name: createdDateTime
  type: string
- description: The timestamp of the last status update.
  name: lastActionDateTime
  type: string
- description: Error details if the operation failed.
  name: error
  type: '[''object'', ''null'']'
provider_name: Microsoft Power Platform APIs
provider_slug: power-platform
schema_file: json-schema/power-platform-operation-status-schema.json
slug: power-platform-operation-status
tags:
- Business Applications
- Copilot Studio
- Dataverse
- Low-Code
- Microsoft
- No-Code
- Power Pages
- Power Platform
title: OperationStatus
---
