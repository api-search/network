---
description: AdditionalDataCommon schema from Adyen API
layout: schema
name: AdditionalDataCommon
properties_list:
- description: 'Triggers test scenarios that allow to replicate certain communication errors. Allowed values: * **NO_CONNECTION_AVAILABLE** – There wasn''t a connection available to service the outgoing communication.'
  name: RequestedTestErrorResponseCode
  type: string
- description: 'Set to true to authorise a part of the requested amount in case the cardholder does not have enough funds on their account. If a payment was partially authorised, the response includes resultCode: Par'
  name: allowPartialAuth
  type: string
- description: Flags a card payment request for either pre-authorisation or final authorisation. For more information, refer to [Authorisation types](https://docs.adyen.com/online-payments/adjust-authorisation#autho
  name: authorisationType
  type: string
- description: Allows you to determine or override the acquirer account that should be used for the transaction. If you need to process a payment with an acquirer different from a default one, you can set up a corre
  name: customRoutingFlag
  type: string
- description: In case of [asynchronous authorisation adjustment](https://docs.adyen.com/online-payments/adjust-authorisation#adjust-authorisation), this field denotes why the additional payment is made. Possible va
  name: industryUsage
  type: string
- description: Set to **true** to require [manual capture](https://docs.adyen.com/online-payments/capture) for the transaction.
  name: manualCapture
  type: string
- description: Allows you to link the transaction to the original or previous one in a subscription/card-on-file chain. This field is required for token-based transactions where Adyen does not tokenize the card. Tra
  name: networkTxReference
  type: string
- description: Boolean indicator that can be optionally used for performing debit transactions on combo cards (for example, combo cards in Brazil). This is not mandatory but we recommend that you set this to true if
  name: overwriteBrand
  type: string
- description: 'This field is required if the transaction is performed by a registered payment facilitator. This field must contain the city of the actual merchant''s address. * Format: alpha-numeric. * Maximum length'
  name: subMerchantCity
  type: string
- description: 'This field is required if the transaction is performed by a registered payment facilitator. This field must contain the three-letter country code of the actual merchant''s address. * Format: alpha-nume'
  name: subMerchantCountry
  type: string
- description: This field contains an identifier of the actual merchant when a transaction is submitted via a payment facilitator. The payment facilitator must send in this unique ID. A unique identifier per submerc
  name: subMerchantID
  type: string
- description: 'This field is required if the transaction is performed by a registered payment facilitator. This field must contain the name of the actual merchant. * Format: alpha-numeric. * Maximum length: 22 chara'
  name: subMerchantName
  type: string
- description: 'This field is required if the transaction is performed by a registered payment facilitator. This field must contain the postal code of the actual merchant''s address. * Format: alpha-numeric. * Maximum'
  name: subMerchantPostalCode
  type: string
- description: This field is required if the transaction is performed by a registered payment facilitator, and if applicable to the country. This field must contain the state code of the actual merchant's address. *
  name: subMerchantState
  type: string
- description: 'This field is required if the transaction is performed by a registered payment facilitator. This field must contain the street of the actual merchant''s address. * Format: alpha-numeric. * Maximum leng'
  name: subMerchantStreet
  type: string
- description: 'This field is required if the transaction is performed by a registered payment facilitator. This field must contain the tax ID of the actual merchant. * Format: alpha-numeric. * Fixed length: 11 or 14'
  name: subMerchantTaxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-additional-data-common-schema.json
slug: checkout-additional-data-common
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataCommon
---
