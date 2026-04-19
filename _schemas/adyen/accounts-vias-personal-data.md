---
description: ViasPersonalData schema from Adyen API
layout: schema
name: ViasPersonalData
properties_list:
- description: The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**.
  name: dateOfBirth
  type: string
- description: Array that contains information about the person's identification document. You can submit only one entry per document type.
  name: documentData
  type: array
- description: The nationality of the person represented by a two-character country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **NL**.
  name: nationality
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-vias-personal-data-schema.json
slug: accounts-vias-personal-data
tags:
- Payments
- Financial Services
- Fintech
title: ViasPersonalData
---
