---
description: SplitConfigurationLogic schema from Adyen API
layout: schema
name: SplitConfigurationLogic
properties_list:
- description: 'Specifies the logic to apply when booking the transaction fees. Should be combined with adyenFees. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.'
  name: acquiringFees
  type: string
- description: Contains the logic used to calculate your user's commission, booked directly to their balance account.
  name: additionalCommission
  type: object
- description: 'Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, interchange & adyenMarkup. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccoun'
  name: adyenCommission
  type: string
- description: 'Specifies the logic to apply when booking the transaction fees. Should be combined with acquiringFees. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.'
  name: adyenFees
  type: string
- description: 'Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, adyenCommission & interchange. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAc'
  name: adyenMarkup
  type: string
- description: 'Specifies the logic to apply when booking the chargeback amount. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**.'
  name: chargeback
  type: string
- description: 'Specifies the logic to apply when allocating the chargeback costs. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**'
  name: chargebackCostAllocation
  type: string
- description: Contains the logic used to the calculate your platform's commission, booked to your liable balance account.
  name: commission
  type: object
- description: 'Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, adyenCommission & adyenMarkup. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAc'
  name: interchange
  type: string
- description: 'Specifies the logic to apply when booking the transaction fees. Cannot be combined with other fees. Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.'
  name: paymentFee
  type: string
- description: 'Specifies the logic to apply when booking the amount left over after currency conversion. Possible values: **addToLiableAccount**, **addToOneBalanceAccount**.'
  name: remainder
  type: string
- description: 'Specifies the logic to apply when booking the transaction fees. Should be combined with interchange, adyenCommission & adyenMarkup. Possible values: **deductFromLiableAccount**, **deductFromOneBalance'
  name: schemeFee
  type: string
- description: Unique identifier of the split logic that is applied when the split configuration conditions are met.
  name: splitLogicId
  type: string
- description: 'Specifies the logic to apply when booking the surcharge amount. Possible values: **addToLiableAccount**, **addToOneBalanceAccount**'
  name: surcharge
  type: string
- description: 'Specifies the logic to apply when booking tips (gratuity). Possible values: **addToLiableAccount**, **addToOneBalanceAccount**.'
  name: tip
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-split-configuration-logic-schema.json
slug: management-split-configuration-logic
tags:
- Payments
- Financial Services
- Fintech
title: SplitConfigurationLogic
---
