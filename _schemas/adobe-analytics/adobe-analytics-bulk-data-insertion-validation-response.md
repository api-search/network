---
description: Result of a file validation request
layout: schema
name: ValidationResponse
properties_list:
- description: Whether the file passed all validation checks
  name: success
  type: boolean
- description: Summary validation message
  name: message
  type: string
- description: List of validation errors found in the file
  name: errors
  type: array
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-bulk-data-insertion-validation-response-schema.json
slug: adobe-analytics-bulk-data-insertion-validation-response
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: ValidationResponse
---
