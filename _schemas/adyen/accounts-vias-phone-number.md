---
description: ViasPhoneNumber schema from Adyen API
layout: schema
name: ViasPhoneNumber
properties_list:
- description: The two-character country code of the phone number. >The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
  name: phoneCountryCode
  type: string
- description: The phone number. >The inclusion of the phone number country code is not necessary.
  name: phoneNumber
  type: string
- description: 'The type of the phone number. >The following values are permitted: `Landline`, `Mobile`, `SIP`, `Fax`.'
  name: phoneType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-vias-phone-number-schema.json
slug: accounts-vias-phone-number
tags:
- Payments
- Financial Services
- Fintech
title: ViasPhoneNumber
---
