---
description: PaymentResponse schema from Adyen API
layout: schema
name: PaymentResponse
properties_list:
- description: Action to be taken for completing the payment.
  name: action
  type: object
- description: 'Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**.'
  name: additionalData
  type: object
- description: Authorised amount in the transaction.
  name: amount
  type: object
- description: Donation Token containing payment details for Adyen Giving.
  name: donationToken
  type: string
- description: The fraud result properties of the payment.
  name: fraudResult
  type: object
- description: The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a require
  name: merchantReference
  type: string
- description: Contains updated information regarding the order in case order information was provided in the request.
  name: order
  type: object
- description: Details about the payment method used in the transaction. Only returned if `resultCode` is **Authorised**.
  name: paymentMethod
  type: object
- description: Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. > For payment methods that require
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
- description: Response of the 3D Secure 2 authentication.
  name: threeDS2ResponseData
  type: object
- description: Result of the 3D Secure 2 authentication.
  name: threeDS2Result
  type: object
- description: When non-empty, contains a value that you must submit to the `/payments/details` endpoint as `paymentData`.
  name: threeDSPaymentData
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-response-schema.json
slug: checkout-payment-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentResponse
---
