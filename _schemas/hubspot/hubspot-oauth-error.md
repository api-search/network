---
description: Standard error response object
layout: schema
name: Error
properties_list:
- description: The category of the error
  name: category
  type: string
- description: A unique identifier for tracking this error
  name: correlationId
  type: string
- description: A human-readable error message
  name: message
  type: string
- description: A more specific error category
  name: subCategory
  type: string
- description: Additional context about the error
  name: context
  type: object
- description: Links to relevant documentation
  name: links
  type: object
- description: List of specific errors
  name: errors
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-oauth-error-schema.json
slug: hubspot-oauth-error
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
