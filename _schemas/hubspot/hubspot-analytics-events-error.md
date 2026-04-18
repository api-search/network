---
description: Standard error response returned when an API request fails
layout: schema
name: Error
properties_list:
- description: High-level error category
  name: category
  type: string
- description: Unique identifier for tracking and debugging the error
  name: correlationId
  type: string
- description: Human-readable error message
  name: message
  type: string
- description: Specific error subcategory for detailed classification
  name: subCategory
  type: string
- description: Additional context about the error
  name: context
  type: object
- description: Relevant links for error resolution and documentation
  name: links
  type: object
- description: List of specific errors encountered
  name: errors
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-analytics-events-error-schema.json
slug: hubspot-analytics-events-error
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
