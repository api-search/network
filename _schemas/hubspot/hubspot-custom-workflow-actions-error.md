---
description: An error response
layout: schema
name: Error
properties_list:
- description: The error category
  name: category
  type: string
- description: A unique identifier for this error instance
  name: correlationId
  type: string
- description: A human-readable error message
  name: message
  type: string
- description: A more specific error category
  name: subCategory
  type: string
- description: Detailed error information
  name: errors
  type: array
- description: Additional context about the error
  name: context
  type: object
- description: Related links
  name: links
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-custom-workflow-actions-error-schema.json
slug: hubspot-custom-workflow-actions-error
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
title: Error
---
