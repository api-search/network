---
description: ModifyResponse schema from Adyen API
layout: schema
name: ModifyResponse
properties_list:
- description: This field contains additional data, which may be returned in a particular response.
  name: additionalData
  type: object
- description: Adyen's 16-character string reference associated with the transaction. This value is globally unique; quote it when communicating with us about this response.
  name: pspReference
  type: string
- description: 'The response: * In case of success, it is either `payout-confirm-received` or `payout-decline-received`. * In case of an error, an informational message is returned.'
  name: response
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-modify-response-schema.json
slug: payouts-modify-response
tags:
- Payments
- Financial Services
- Fintech
title: ModifyResponse
---
