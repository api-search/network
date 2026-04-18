---
description: Response from batch operations
layout: schema
name: BatchResponse
properties_list:
- description: Current status of the batch operation
  name: status
  type: string
- description: Successfully processed posts
  name: results
  type: array
- description: ISO 8601 timestamp when the batch was requested
  name: requestedAt
  type: string
- description: ISO 8601 timestamp when processing started
  name: startedAt
  type: string
- description: ISO 8601 timestamp when processing completed
  name: completedAt
  type: string
- description: Related links
  name: links
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-blog-posts-batch-response-schema.json
slug: hubspot-blog-posts-batch-response
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
title: BatchResponse
---
