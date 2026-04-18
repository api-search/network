---
description: Standard error in batch operations
layout: schema
name: StandardError
properties_list:
- description: Error status
  name: status
  type: string
- description: ID of the failed item
  name: id
  type: string
- description: Error category
  name: category
  type: string
- description: Error message
  name: message
  type: string
- description: Detailed errors
  name: errors
  type: array
- description: ''
  name: context
  type: object
- description: ''
  name: links
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-blog-posts-standard-error-schema.json
slug: hubspot-blog-posts-standard-error
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
