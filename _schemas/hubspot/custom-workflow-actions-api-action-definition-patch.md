---
description: Input for updating an action definition
layout: schema
name: ActionDefinitionPatch
properties_list:
- description: The URL that HubSpot will call when the action executes
  name: actionUrl
  type: string
- description: Human-readable labels for the action
  name: labels
  type: object
- description: ''
  name: inputFields
  type: array
- description: ''
  name: outputFields
  type: array
- description: ''
  name: objectTypes
  type: array
- description: Options for requesting CRM object data
  name: objectRequestOptions
  type: object
- description: ''
  name: published
  type: boolean
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/custom-workflow-actions-api-action-definition-patch-schema.json
slug: custom-workflow-actions-api-action-definition-patch
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
title: ActionDefinitionPatch
---
