---
description: Detailed error information
layout: schema
name: ErrorDetail
properties_list:
- description: Error message
  name: message
  type: string
- description: Error code
  name: code
  type: string
- description: Error subcategory
  name: subCategory
  type: string
- description: Location of the error
  name: in
  type: string
- description: Additional context
  name: context
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-source-code-error-detail-schema.json
slug: hubspot-source-code-error-detail
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
