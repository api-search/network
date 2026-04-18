---
description: Detailed information about a specific error
layout: schema
name: ErrorDetail
properties_list:
- description: A human-readable error message
  name: message
  type: string
- description: An error code
  name: code
  type: string
- description: A specific error subcategory
  name: subCategory
  type: string
- description: The location of the error (e.g., body, query, path)
  name: in
  type: string
- description: Additional context about the specific error
  name: context
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-oauth-error-detail-schema.json
slug: hubspot-oauth-error-detail
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
