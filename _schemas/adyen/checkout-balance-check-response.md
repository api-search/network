---
description: BalanceCheckResponse schema from Adyen API
layout: schema
name: BalanceCheckResponse
properties_list:
- description: 'Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**.'
  name: additionalData
  type: object
- description: The balance for the payment method.
  name: balance
  type: object
- description: The fraud result properties of the payment.
  name: fraudResult
  type: object
- description: Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the a
  name: refusalReason
  type: string
- description: 'The result of the cancellation request. Possible values: * **Success** – Indicates that the balance check was successful. * **NotEnoughBalance** – Commonly indicates that the card did not have enough '
  name: resultCode
  type: string
- description: The maximum spendable balance for a single transaction. Applicable to some gift cards.
  name: transactionLimit
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-balance-check-response-schema.json
slug: checkout-balance-check-response
tags:
- Payments
- Financial Services
- Fintech
title: BalanceCheckResponse
---
