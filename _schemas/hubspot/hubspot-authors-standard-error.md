---
description: Standard error in batch operations
layout: schema
name: StandardError
properties_list:
- description: Error status code
  name: status
  type: string
- description: ID of the failed item
  name: id
  type: string
- description: Error category
  name: category
  type: string
- description: Human-readable error message
  name: message
  type: string
- description: List of detailed errors
  name: errors
  type: array
- description: Additional error context
  name: context
  type: object
- description: Related links for error resolution
  name: links
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-authors-standard-error-schema.json
slug: hubspot-authors-standard-error
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
title: StandardError
---
