---
description: Response from a batch read operation
layout: schema
name: BatchReadResponse
properties_list:
- description: The status of the batch operation
  name: status
  type: string
- description: The retrieved commerce payments
  name: results
  type: array
- description: When the request was received
  name: requestedAt
  type: string
- description: When processing started
  name: startedAt
  type: string
- description: When processing completed
  name: completedAt
  type: string
- description: Number of errors encountered
  name: numErrors
  type: integer
- description: List of errors
  name: errors
  type: array
- description: ''
  name: links
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/commerce-payments-api-batch-read-response-schema.json
slug: commerce-payments-api-batch-read-response
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
title: BatchReadResponse
---
