---
description: Detailed information about a specific error
layout: schema
name: ErrorDetail
properties_list:
- description: A human-readable message describing the specific error
  name: message
  type: string
- description: An error code for this specific error
  name: code
  type: string
- description: The field or parameter where the error occurred
  name: in
  type: string
- description: A specific subcategory for this error
  name: subCategory
  type: string
- description: Additional context for this error
  name: context
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-domains-error-detail-schema.json
slug: hubspot-domains-error-detail
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
