---
description: PayoutResponse schema from Adyen API
layout: schema
name: PayoutResponse
properties_list:
- description: 'Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**.'
  name: additionalData
  type: object
- description: 'Authorisation code: * When the payment is authorised successfully, this field holds the authorisation code for the payment. * When the payment is not authorised, this field is empty.'
  name: authCode
  type: string
- description: Includes the currency of the conversion and the value of the transaction. > This value only applies if you have implemented Dynamic Currency Conversion. For more information, [contact Support](https:/
  name: dccAmount
  type: object
- description: Cryptographic signature used to verify `dccQuote`. > This value only applies if you have implemented Dynamic Currency Conversion. For more information, [contact Support](https://www.adyen.help/hc/en-u
  name: dccSignature
  type: string
- description: The fraud result properties of the payment.
  name: fraudResult
  type: object
- description: The URL to direct the shopper to. > In case of SecurePlus, do not redirect a shopper to this URL.
  name: issuerUrl
  type: string
- description: The payment session.
  name: md
  type: string
- description: 'The 3D request data for the issuer. If the value is **CUPSecurePlus-CollectSMSVerificationCode**, collect an SMS code from the shopper and pass it in the `/authorise3D` request. For more information, '
  name: paRequest
  type: string
- description: Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the a
  name: refusalReason
  type: string
- description: 'The result of the payment. For more information, see [Result codes](https://docs.adyen.com/online-payments/payment-result-codes). Possible values: * **AuthenticationFinished** – The payment has been s'
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-payout-response-schema.json
slug: payouts-payout-response
tags:
- Payments
- Financial Services
- Fintech
title: PayoutResponse
---
