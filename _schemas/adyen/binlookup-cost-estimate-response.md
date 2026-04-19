---
description: CostEstimateResponse schema from Adyen API
layout: schema
name: CostEstimateResponse
properties_list:
- description: Card BIN details.
  name: cardBin
  type: object
- description: The estimated cost (scheme fee + interchange) in the settlement currency. If the settlement currency cannot be determined, the fee in EUR is returned.
  name: costEstimateAmount
  type: object
- description: Adyen's 16-character reference associated with the request.
  name: costEstimateReference
  type: string
- description: The result of the cost estimation.
  name: resultCode
  type: string
- description: 'Indicates the way the charges can be passed on to the cardholder. The following values are possible: * `ZERO` - the charges are not allowed to pass on * `PASSTHROUGH` - the charges can be passed on * '
  name: surchargeType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-cost-estimate-response-schema.json
slug: binlookup-cost-estimate-response
tags:
- Payments
- Financial Services
- Fintech
title: CostEstimateResponse
---
