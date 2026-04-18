---
description: Represents an error response from the API
layout: schema
name: Error
properties_list:
- description: The error category
  name: category
  type: string
- description: A unique identifier for the request, useful for debugging
  name: correlationId
  type: string
- description: A human-readable message describing the error
  name: message
  type: string
- description: A more specific category for the error
  name: subCategory
  type: string
- description: Additional context about the error
  name: context
  type: object
- description: Links to documentation or remediation steps
  name: links
  type: object
- description: A list of specific error details
  name: errors
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-domains-error-schema.json
slug: hubspot-domains-error
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
