---
description: KlarnaInfo schema from Adyen API
layout: schema
name: KlarnaInfo
properties_list:
- description: 'Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). Default value: **false**.'
  name: autoCapture
  type: boolean
- description: The email address for disputes.
  name: disputeEmail
  type: string
- description: The region of operation. For example, **NA**, **EU**, **CH**, **AU**.
  name: region
  type: string
- description: The email address of merchant support.
  name: supportEmail
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-klarna-info-schema.json
slug: management-klarna-info
tags:
- Payments
- Financial Services
- Fintech
title: KlarnaInfo
---
