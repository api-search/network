---
description: PaymentInstrumentGroup schema from Adyen API
layout: schema
name: PaymentInstrumentGroup
properties_list:
- description: The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id) to which the payment instrument group belongs.
  name: balancePlatform
  type: string
- description: Your description for the payment instrument group, maximum 300 characters.
  name: description
  type: string
- description: The unique identifier of the payment instrument group.
  name: id
  type: string
- description: Properties of the payment instrument group.
  name: properties
  type: object
- description: Your reference for the payment instrument group, maximum 150 characters.
  name: reference
  type: string
- description: The tx variant of the payment instrument group.
  name: txVariant
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-payment-instrument-group-schema.json
slug: configuration-payment-instrument-group
tags:
- Payments
- Financial Services
- Fintech
title: PaymentInstrumentGroup
---
