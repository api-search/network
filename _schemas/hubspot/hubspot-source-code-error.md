---
description: Standard error response
layout: schema
name: Error
properties_list:
- description: Error category
  name: category
  type: string
- description: Unique identifier for error tracking
  name: correlationId
  type: string
- description: Human-readable error message
  name: message
  type: string
- description: Specific error subcategory
  name: subCategory
  type: string
- description: Additional error context
  name: context
  type: object
- description: Links to relevant documentation
  name: links
  type: object
- description: Detailed error information
  name: errors
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-source-code-error-schema.json
slug: hubspot-source-code-error
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
