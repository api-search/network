---
description: StoredValueBalanceCheckResponse schema from Adyen API
layout: schema
name: StoredValueBalanceCheckResponse
properties_list:
- description: The balance currently on the payment method.
  name: currentBalance
  type: object
- description: Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: If the transaction is refused or an error occurs, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `r
  name: refusalReason
  type: string
- description: 'The result of the payment. Possible values: * **Success** – The operation has been completed successfully. * **Refused** – The operation was refused. The reason is given in the `refusalReason` field. '
  name: resultCode
  type: string
- description: Raw refusal reason received from the third party, where available
  name: thirdPartyRefusalReason
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/stored-value-stored-value-balance-check-response-schema.json
slug: stored-value-stored-value-balance-check-response
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueBalanceCheckResponse
---
