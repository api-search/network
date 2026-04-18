---
description: Response from batch association operations
layout: schema
name: BatchAssociationResponse
properties_list:
- description: Status of the batch operation
  name: status
  type: string
- description: Successfully processed associations
  name: results
  type: array
- description: When the batch was requested
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
schema_file: json-schema/hubspot-crm-associations-batch-association-response-schema.json
slug: hubspot-crm-associations-batch-association-response
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
title: BatchAssociationResponse
---
