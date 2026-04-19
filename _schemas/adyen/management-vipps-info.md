---
description: VippsInfo schema from Adyen API
layout: schema
name: VippsInfo
properties_list:
- description: 'Vipps logo. Format: Base64-encoded string.'
  name: logo
  type: string
- description: Vipps subscription cancel url (required in case of [recurring payments](https://docs.adyen.com/online-payments/tokenization))
  name: subscriptionCancelUrl
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-vipps-info-schema.json
slug: management-vipps-info
tags:
- Payments
- Financial Services
- Fintech
title: VippsInfo
---
