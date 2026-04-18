---
description: Response for asynchronous action status
layout: schema
name: ActionResponse
properties_list:
- description: Current status of the action
  name: status
  type: string
- description: When the action was requested
  name: requestedAt
  type: string
- description: When the action started processing
  name: startedAt
  type: string
- description: When the action completed
  name: completedAt
  type: string
- description: Related links
  name: links
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-source-code-action-response-schema.json
slug: hubspot-source-code-action-response
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
title: ActionResponse
---
