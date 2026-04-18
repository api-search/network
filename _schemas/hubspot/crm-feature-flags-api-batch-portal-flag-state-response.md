---
description: Response for successful batch portal flag state operations
layout: schema
name: BatchPortalFlagStateResponse
properties_list:
- description: The overall status of the batch operation
  name: status
  type: string
- description: List of portal flag states that were successfully affected
  name: results
  type: array
- description: Timestamp when the batch operation started
  name: startedAt
  type: string
- description: Timestamp when the batch operation completed
  name: completedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-feature-flags-api-batch-portal-flag-state-response-schema.json
slug: crm-feature-flags-api-batch-portal-flag-state-response
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
title: BatchPortalFlagStateResponse
---
