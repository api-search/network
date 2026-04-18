---
description: Response for batch call operations
layout: schema
name: BatchCallsResponse
properties_list:
- description: The status of the batch operation
  name: status
  type: string
- description: The results of the batch operation
  name: results
  type: array
- description: When the batch was requested
  name: requestedAt
  type: string
- description: When the batch processing started
  name: startedAt
  type: string
- description: When the batch processing completed
  name: completedAt
  type: string
- description: Any errors that occurred during batch processing
  name: errors
  type: array
- description: ''
  name: links
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/engagement-calls-api-batch-calls-response-schema.json
slug: engagement-calls-api-batch-calls-response
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
title: BatchCallsResponse
---
