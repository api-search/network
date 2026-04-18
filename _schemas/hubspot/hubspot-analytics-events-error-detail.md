---
description: Detailed information about a specific error
layout: schema
name: ErrorDetail
properties_list:
- description: Human-readable error message
  name: message
  type: string
- description: Machine-readable error code
  name: code
  type: string
- description: Specific error subcategory
  name: subCategory
  type: string
- description: Location where the error occurred (e.g., query, path, body)
  name: in
  type: string
- description: Additional context about the specific error
  name: context
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-analytics-events-error-detail-schema.json
slug: hubspot-analytics-events-error-detail
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
