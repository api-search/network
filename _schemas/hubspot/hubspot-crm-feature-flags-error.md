---
description: Represents an error response from the API
layout: schema
name: Error
properties_list:
- description: The error category
  name: category
  type: string
- description: Unique identifier for the request, useful for debugging
  name: correlationId
  type: string
- description: Human-readable error message
  name: message
  type: string
- description: More specific error classification
  name: subCategory
  type: string
- description: Additional context about the error
  name: context
  type: object
- description: Helpful links related to the error
  name: links
  type: object
- description: List of detailed error information
  name: errors
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-feature-flags-error-schema.json
slug: hubspot-crm-feature-flags-error
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
