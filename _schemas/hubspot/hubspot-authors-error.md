---
description: Standard error response returned when an API request fails
layout: schema
name: Error
properties_list:
- description: High-level error category
  name: category
  type: string
- description: Unique identifier for tracking and debugging
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
- description: Related links for error resolution
  name: links
  type: object
- description: List of specific errors
  name: errors
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-authors-error-schema.json
slug: hubspot-authors-error
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
