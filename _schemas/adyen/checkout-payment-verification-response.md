---
description: PaymentVerificationResponse schema from Adyen API
layout: schema
name: PaymentVerificationResponse
properties_list:
- description: 'Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**.'
  name: additionalData
  type: object
- description: The fraud result properties of the payment.
  name: fraudResult
  type: object
- description: A unique value that you provided in the initial `/paymentSession` request as a `reference` field.
  name: merchantReference
  type: string
- description: Contains updated information regarding the order in case order information was provided in the request.
  name: order
  type: object
- description: Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the a
  name: refusalReason
  type: string
- description: Code that specifies the refusal reason. For more information, see [Authorisation refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons).
  name: refusalReasonCode
  type: string
- description: 'The result of the payment. For more information, see [Result codes](https://docs.adyen.com/online-payments/payment-result-codes). Possible values: * **AuthenticationFinished** – The payment has been s'
  name: resultCode
  type: string
- description: The type of the error.
  name: serviceError
  type: object
- description: The shopperLocale value provided in the payment request.
  name: shopperLocale
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-verification-response-schema.json
slug: checkout-payment-verification-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentVerificationResponse
---
