---
description: Result of file validation
layout: schema
name: ValidationResult
properties_list:
- description: Whether the file passed validation
  name: valid
  type: boolean
- description: List of validation errors (if any)
  name: errors
  type: array
- description: List of validation warnings (if any)
  name: warnings
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-source-code-validation-result-schema.json
slug: hubspot-source-code-validation-result
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
title: ValidationResult
---
