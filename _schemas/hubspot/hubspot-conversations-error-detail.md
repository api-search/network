---
description: Detailed information about a specific error.
layout: schema
name: ErrorDetail
properties_list:
- description: Human-readable error message
  name: message
  type: string
- description: Error code
  name: code
  type: string
- description: Error subcategory
  name: subCategory
  type: string
- description: Location where error occurred
  name: in
  type: string
- description: ''
  name: context
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-conversations-error-detail-schema.json
slug: hubspot-conversations-error-detail
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
title: ErrorDetail
---
