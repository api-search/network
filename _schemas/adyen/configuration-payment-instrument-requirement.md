---
description: PaymentInstrumentRequirement schema from Adyen API
layout: schema
name: PaymentInstrumentRequirement
properties_list:
- description: Specifies the requirements for the payment instrument that need to be included in the request for a particular route.
  name: description
  type: string
- description: The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**.
  name: issuingCountryCode
  type: string
- description: Specifies if the requirement only applies to transfers to another balance platform.
  name: onlyForCrossBalancePlatform
  type: boolean
- description: The type of the payment instrument. For example, "BankAccount" or "Card".
  name: paymentInstrumentType
  type: string
- description: '**paymentInstrumentRequirement**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-payment-instrument-requirement-schema.json
slug: configuration-payment-instrument-requirement
tags:
- Payments
- Financial Services
- Fintech
title: PaymentInstrumentRequirement
---
