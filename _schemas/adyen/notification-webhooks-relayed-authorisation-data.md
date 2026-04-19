---
description: RelayedAuthorisationData schema from Adyen API
layout: schema
name: RelayedAuthorisationData
properties_list:
- description: The `metadata` object from the relayed authorisation response from your server.
  name: metadata
  type: object
- description: The `reference` from the relayed authorisation response from your server.
  name: reference
  type: string
- description: The value can be **Authorised** or **Refused**, based on the `authorisationDecision.status` in the relayed authorisation response from your server.
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-relayed-authorisation-data-schema.json
slug: notification-webhooks-relayed-authorisation-data
tags:
- Payments
- Financial Services
- Fintech
title: RelayedAuthorisationData
---
