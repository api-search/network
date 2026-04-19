---
description: InvalidField schema from Adyen API
layout: schema
name: InvalidField
properties_list:
- description: Description of the validation error.
  name: message
  type: string
- description: The field that has an invalid value.
  name: name
  type: string
- description: The invalid value.
  name: value
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-invalid-field-schema.json
slug: configuration-invalid-field
tags:
- Payments
- Financial Services
- Fintech
title: InvalidField
---
