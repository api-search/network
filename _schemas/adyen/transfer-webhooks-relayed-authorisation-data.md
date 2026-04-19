---
description: RelayedAuthorisationData schema from Adyen API
layout: schema
name: RelayedAuthorisationData
properties_list:
- description: Contains key-value pairs of your references and descriptions, for example, `customId`:`your-own-custom-field-12345`.
  name: metadata
  type: object
- description: Your reference for the relayed authorisation data.
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-relayed-authorisation-data-schema.json
slug: transfer-webhooks-relayed-authorisation-data
tags:
- Payments
- Financial Services
- Fintech
title: RelayedAuthorisationData
---
