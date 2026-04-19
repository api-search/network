---
description: PersonalData schema from Adyen API
layout: schema
name: PersonalData
properties_list:
- description: The date of birth of the person. The date should be in ISO-8601 format yyyy-mm-dd (e.g. 2000-01-31).
  name: dateOfBirth
  type: string
- description: An ID number of the person.
  name: idNumber
  type: string
- description: The nationality of the person represented by a two-character country code. >The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
  name: nationality
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-personal-data-schema.json
slug: configuration-webhooks-personal-data
tags:
- Payments
- Financial Services
- Fintech
title: PersonalData
---
