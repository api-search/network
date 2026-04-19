---
description: Configuration schema from Adyen API
layout: schema
name: Configuration
properties_list:
- description: Describes the configuration for AVS ([Address Verification System](https://en.wikipedia.org/wiki/Address_Verification_System)).
  name: avs
  type: object
- description: 'Determines whether the cardholder name should be provided or not. Permitted values: * NONE * OPTIONAL * REQUIRED'
  name: cardHolderName
  type: string
- description: Describes the configuration for [installment payments](https://docs.adyen.com/payment-methods/cards/credit-card-installments).
  name: installments
  type: object
- description: Determines how to display the details fields.
  name: shopperInput
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-configuration-schema.json
slug: checkout-configuration
tags:
- Payments
- Financial Services
- Fintech
title: Configuration
---
