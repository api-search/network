---
description: BcmcInfo schema from Adyen API
layout: schema
name: BcmcInfo
properties_list:
- description: Indicates if [Bancontact mobile](https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile) is enabled.
  name: enableBcmcMobile
  type: boolean
- description: Information regarding the transaction description.
  name: transactionDescription
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-bcmc-info-schema.json
slug: management-bcmc-info
tags:
- Payments
- Financial Services
- Fintech
title: BcmcInfo
---
