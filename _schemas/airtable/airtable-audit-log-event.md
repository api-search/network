---
description: An audit log event recording an action performed within an Airtable enterprise account. Events capture who performed what action, on which resource, and when, for compliance and security monitoring purposes.
layout: schema
name: Airtable Audit Log Event
properties_list:
- description: The unique identifier for the audit log event.
  name: id
  type: string
- description: The exact date and time when the action was logged, in ISO 8601 format.
  name: timestamp
  type: string
- description: The type of action that was performed (e.g., created, updated, deleted, viewed, shared).
  name: action
  type: string
- description: The entity that performed the action.
  name: actor
  type: object
- description: The ID of the model (base, table, field, record, view, etc.) that was affected by the action.
  name: modelId
  type:
  - string
  - 'null'
- description: The type of model affected by the action.
  name: modelType
  type:
  - string
  - 'null'
- description: The category of the event for organizational and filtering purposes.
  name: category
  type: string
- description: Additional context about the event, including related resource identifiers and request metadata.
  name: context
  type: object
- description: The version of the event payload format.
  name: payloadVersion
  type: string
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-audit-log-event-schema.json
slug: airtable-audit-log-event
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Audit Log Event
---
