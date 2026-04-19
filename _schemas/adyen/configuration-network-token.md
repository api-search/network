---
description: NetworkToken schema from Adyen API
layout: schema
name: NetworkToken
properties_list:
- description: The card brand variant of the payment instrument associated with the network token. For example, **mc_prepaid_mrw**.
  name: brandVariant
  type: string
- description: Date and time when the network token was created, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) extended format. For example, **2020-12-18T10:15:30+01:00**..
  name: creationDate
  type: string
- description: Device details.
  name: device
  type: object
- description: The unique identifier of the network token.
  name: id
  type: string
- description: The unique identifier of the payment instrument to which this network token belongs to.
  name: paymentInstrumentId
  type: string
- description: 'The status of the network token. Possible values: **active**, **inactive**, **suspended**, **closed**.'
  name: status
  type: string
- description: The last four digits of the network token `id`.
  name: tokenLastFour
  type: string
- description: The type of wallet the network token is associated with. For example, **applePay**.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-network-token-schema.json
slug: configuration-network-token
tags:
- Payments
- Financial Services
- Fintech
title: NetworkToken
---
