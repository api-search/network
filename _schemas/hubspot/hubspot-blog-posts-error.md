---
description: Standard error response
layout: schema
name: Error
properties_list:
- description: Error category
  name: category
  type: string
- description: Unique tracking identifier
  name: correlationId
  type: string
- description: Error message
  name: message
  type: string
- description: Error subcategory
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
schema_file: json-schema/hubspot-blog-posts-error-schema.json
slug: hubspot-blog-posts-error
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
