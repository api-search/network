---
description: Phone schema from Adyen API
layout: schema
name: Phone
properties_list:
- description: 'Country code. Length: 1–3 characters.'
  name: cc
  type: string
- description: 'Subscriber number. Maximum length: 15 characters.'
  name: subscriber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-phone-schema.json
slug: checkout-phone
tags:
- Payments
- Financial Services
- Fintech
title: Phone
---
