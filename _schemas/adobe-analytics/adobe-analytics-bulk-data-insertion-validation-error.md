---
description: A single validation error from file validation
layout: schema
name: ValidationError
properties_list:
- description: Row number where the error occurred (1-indexed)
  name: row
  type: integer
- description: Column name where the error occurred
  name: column
  type: string
- description: Description of the validation error
  name: message
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-bulk-data-insertion-validation-error-schema.json
slug: adobe-analytics-bulk-data-insertion-validation-error
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: ValidationError
---
