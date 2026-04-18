---
description: An array of objects to contain DPA registration details.
layout: schema
name: Dpa
properties_list:
- description: 'Card networks that are supported for DPA registration. The following networks are supported: MASTERCARD, VISA, DISCOVER, AMEX.'
  name: supportedCardBrands
  type: array
- description: 'A flag for the Integrator to indicate that they would not like to have their Cardholder''s debit cards tokenized. Conditional: Must be set to true when the Digital Payment Application (DPA) processes i'
  name: debitTokenRequested
  type: boolean
- description: List of checkout types to be supported by the DPA. These include CLICK_TO_PAY, GUEST_CHECKOUT_TOKENIZATION and CARD_ON_FILE_TOKENIZATION.
  name: supportedCheckoutTypes
  type: array
- description: ''
  name: acquirerData
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-unified-checkout-solutions-dpa-schema.json
slug: mastercard-unified-checkout-solutions-dpa
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Dpa
---
