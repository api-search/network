---
description: Input for creating a new action definition
layout: schema
name: ActionDefinitionInput
properties_list:
- description: The URL that HubSpot will call when the action executes
  name: actionUrl
  type: string
- description: Human-readable labels for the action
  name: labels
  type: object
- description: Input fields for the action
  name: inputFields
  type: array
- description: Output fields for the action
  name: outputFields
  type: array
- description: CRM object types this action can operate on
  name: objectTypes
  type: array
- description: Options for requesting CRM object data
  name: objectRequestOptions
  type: object
- description: Whether to publish the action immediately
  name: published
  type: boolean
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/custom-workflow-actions-api-action-definition-input-schema.json
slug: custom-workflow-actions-api-action-definition-input
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
title: ActionDefinitionInput
---
