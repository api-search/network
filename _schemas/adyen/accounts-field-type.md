---
description: FieldType schema from Adyen API
layout: schema
name: FieldType
properties_list:
- description: The full name of the property.
  name: field
  type: string
- description: The type of the field.
  name: fieldName
  type: string
- description: The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
  name: shareholderCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-field-type-schema.json
slug: accounts-field-type
tags:
- Payments
- Financial Services
- Fintech
title: FieldType
---
