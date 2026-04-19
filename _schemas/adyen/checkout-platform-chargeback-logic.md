---
description: PlatformChargebackLogic schema from Adyen API
layout: schema
name: PlatformChargebackLogic
properties_list:
- description: 'The method of handling the chargeback. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**.'
  name: behavior
  type: string
- description: The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account.
  name: costAllocationAccount
  type: string
- description: The unique identifier of the balance account against which the disputed amount is booked. Required if `behavior` is **deductFromOneBalanceAccount**.
  name: targetAccount
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-platform-chargeback-logic-schema.json
slug: checkout-platform-chargeback-logic
tags:
- Payments
- Financial Services
- Fintech
title: PlatformChargebackLogic
---
