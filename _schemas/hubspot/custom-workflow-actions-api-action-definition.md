---
description: A custom workflow action definition
layout: schema
name: ActionDefinition
properties_list:
- description: The unique identifier of the action definition
  name: id
  type: string
- description: The current revision identifier
  name: revisionId
  type: string
- description: The URL that HubSpot will call when the action executes
  name: actionUrl
  type: string
- description: Human-readable labels for the action
  name: labels
  type: object
- description: Input fields that users can configure for the action
  name: inputFields
  type: array
- description: Output fields that the action returns
  name: outputFields
  type: array
- description: CRM object types this action can operate on
  name: objectTypes
  type: array
- description: Options for requesting CRM object data
  name: objectRequestOptions
  type: object
- description: Whether the action is published and available for use
  name: published
  type: boolean
- description: Functions associated with this action
  name: functions
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/custom-workflow-actions-api-action-definition-schema.json
slug: custom-workflow-actions-api-action-definition
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: ActionDefinition
---
