---
description: StoreDetailResponse schema from Adyen API
layout: schema
name: StoreDetailResponse
properties_list:
- description: This field contains additional data, which may be returned in a particular response.
  name: additionalData
  type: object
- description: A new reference to uniquely identify this request.
  name: pspReference
  type: string
- description: The token which you can use later on for submitting the payout.
  name: recurringDetailReference
  type: string
- description: The result code of the transaction. `Success` indicates that the details were stored successfully.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-store-detail-response-schema.json
slug: payouts-store-detail-response
tags:
- Payments
- Financial Services
- Fintech
title: StoreDetailResponse
---
