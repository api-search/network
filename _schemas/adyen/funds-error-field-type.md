---
description: ErrorFieldType schema from Adyen API
layout: schema
name: ErrorFieldType
properties_list:
- description: The validation error code.
  name: errorCode
  type: integer
- description: A description of the validation error.
  name: errorDescription
  type: string
- description: The type of error field.
  name: fieldType
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-error-field-type-schema.json
slug: funds-error-field-type
tags:
- Payments
- Financial Services
- Fintech
title: ErrorFieldType
---
