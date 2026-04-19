---
description: Phone schema from Adyen API
layout: schema
name: Phone
properties_list:
- description: The full phone number provided as a single string. For example, **"0031 6 11 22 33 44"**, **"+316/1122-3344"**, or **"(0031) 611223344"**.
  name: number
  type: string
- description: 'Type of phone number. Possible values: **Landline**, **Mobile**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-phone-schema.json
slug: configuration-phone
tags:
- Payments
- Financial Services
- Fintech
title: Phone
---
