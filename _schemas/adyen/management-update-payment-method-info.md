---
description: UpdatePaymentMethodInfo schema from Adyen API
layout: schema
name: UpdatePaymentMethodInfo
properties_list:
- description: Bancontact details.
  name: bcmc
  type: object
- description: Cartes Bancaires details.
  name: cartesBancaires
  type: object
- description: The list of countries where a payment method is available. By default, all countries supported by the payment method.
  name: countries
  type: array
- description: China Union Pay details.
  name: cup
  type: object
- description: The list of currencies that a payment method supports. By default, all currencies supported by the payment method.
  name: currencies
  type: array
- description: Custom routing flags for acquirer routing.
  name: customRoutingFlags
  type: array
- description: Diners details.
  name: diners
  type: object
- description: Discover details.
  name: discover
  type: object
- description: Eftpos Australia details.
  name: eftpos_australia
  type: object
- description: Indicates whether the payment method is enabled (**true**) or disabled (**false**).
  name: enabled
  type: boolean
- description: Girocard details.
  name: girocard
  type: object
- description: iDeal details.
  name: ideal
  type: object
- description: Interac Card details.
  name: interac_card
  type: object
- description: JCB details.
  name: jcb
  type: object
- description: Maestro details.
  name: maestro
  type: object
- description: MasterCard details.
  name: mc
  type: object
- description: The list of stores for this payment method
  name: storeIds
  type: array
- description: Visa details.
  name: visa
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-update-payment-method-info-schema.json
slug: management-update-payment-method-info
tags:
- Payments
- Financial Services
- Fintech
title: UpdatePaymentMethodInfo
---
