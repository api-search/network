---
description: StoreDetailAndSubmitResponse schema from Adyen API
layout: schema
name: StoreDetailAndSubmitResponse
properties_list:
- description: This field contains additional data, which may be returned in a particular response.
  name: additionalData
  type: object
- description: A new reference to uniquely identify this request.
  name: pspReference
  type: string
- description: In case of refusal, an informational message for the reason.
  name: refusalReason
  type: string
- description: 'The response: * In case of success is payout-submit-received. * In case of an error, an informational message is returned.'
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-store-detail-and-submit-response-schema.json
slug: payouts-store-detail-and-submit-response
tags:
- Payments
- Financial Services
- Fintech
title: StoreDetailAndSubmitResponse
---
