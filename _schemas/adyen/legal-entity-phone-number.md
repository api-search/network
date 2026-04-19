---
description: PhoneNumber schema from Adyen API
layout: schema
name: PhoneNumber
properties_list:
- description: The full phone number, including the country code. For example, **+3112345678**.
  name: number
  type: string
- description: 'The type of phone number. Possible values: **mobile**, **landline**, **sip**, **fax.**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-phone-number-schema.json
slug: legal-entity-phone-number
tags:
- Payments
- Financial Services
- Fintech
title: PhoneNumber
---
