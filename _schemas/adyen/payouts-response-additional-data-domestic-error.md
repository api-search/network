---
description: ResponseAdditionalDataDomesticError schema from Adyen API
layout: schema
name: ResponseAdditionalDataDomesticError
properties_list:
- description: The reason the transaction was declined, given by the local issuer. Currently available for merchants in Japan.
  name: domesticRefusalReasonRaw
  type: string
- description: The action the shopper should take, in a local language. Currently available in Japanese, for merchants in Japan.
  name: domesticShopperAdvice
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-response-additional-data-domestic-error-schema.json
slug: payouts-response-additional-data-domestic-error
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataDomesticError
---
