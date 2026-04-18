---
description: A validation error
layout: schema
name: ValidationError
properties_list:
- description: Error description
  name: message
  type: string
- description: Line number where the error occurred
  name: line
  type: integer
- description: Column number where the error occurred
  name: column
  type: integer
- description: Error category
  name: category
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-source-code-validation-error-schema.json
slug: hubspot-source-code-validation-error
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
title: ValidationError
---
