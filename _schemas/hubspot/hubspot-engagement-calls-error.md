---
description: Error response
layout: schema
name: Error
properties_list:
- description: The error category
  name: category
  type: string
- description: Unique request identifier for debugging
  name: correlationId
  type: string
- description: Human-readable error message
  name: message
  type: string
- description: More specific error category
  name: subCategory
  type: string
- description: ''
  name: context
  type: object
- description: ''
  name: links
  type: object
- description: ''
  name: errors
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-engagement-calls-error-schema.json
slug: hubspot-engagement-calls-error
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
