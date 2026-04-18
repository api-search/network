---
description: Detailed error information for specific validation failures
layout: schema
name: ErrorDetail
properties_list:
- description: Specific error message
  name: message
  type: string
- description: Error code
  name: code
  type: string
- description: Error sub-category
  name: subCategory
  type: string
- description: Location of the error (e.g., path, body, query)
  name: in
  type: string
- description: Additional context for the error
  name: context
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-feature-flags-error-detail-schema.json
slug: hubspot-crm-feature-flags-error-detail
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
