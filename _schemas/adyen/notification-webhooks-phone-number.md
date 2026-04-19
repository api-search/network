---
description: PhoneNumber schema from Adyen API
layout: schema
name: PhoneNumber
properties_list:
- description: The two-character ISO-3166-1 alpha-2 country code of the phone number. For example, **US** or **NL**.
  name: phoneCountryCode
  type: string
- description: The phone number. The inclusion of the phone number country code is not necessary.
  name: phoneNumber
  type: string
- description: 'The type of the phone number. Possible values: **Landline**, **Mobile**, **SIP**, **Fax**.'
  name: phoneType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-phone-number-schema.json
slug: notification-webhooks-phone-number
tags:
- Payments
- Financial Services
- Fintech
title: PhoneNumber
---
