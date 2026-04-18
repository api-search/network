---
description: Response for batch operations that had some failures
layout: schema
name: BatchPortalFlagStateResponseWithErrors
properties_list:
- description: The overall status of the batch operation
  name: status
  type: string
- description: List of portal flag states that were successfully affected
  name: results
  type: array
- description: List of errors that occurred during the batch operation
  name: errors
  type: array
- description: Timestamp when the batch operation started
  name: startedAt
  type: string
- description: Timestamp when the batch operation completed
  name: completedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-feature-flags-api-batch-portal-flag-state-response-with-errors-schema.json
slug: crm-feature-flags-api-batch-portal-flag-state-response-with-errors
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
title: BatchPortalFlagStateResponseWithErrors
---
