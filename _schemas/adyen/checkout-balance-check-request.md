---
description: BalanceCheckRequest schema from Adyen API
layout: schema
name: BalanceCheckRequest
properties_list:
- description: Shopper account information for 3D Secure 2. > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow.
  name: accountInfo
  type: object
- description: If you want a [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) request to use a non-zero value, assign this value to `additionalAmount` (while th
  name: additionalAmount
  type: object
- description: This field contains additional data, which may be required for a particular payment request. The `additionalData` object consists of entries, each of which includes the key and value.
  name: additionalData
  type: object
- description: The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/
  name: amount
  type: object
- description: Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).
  name: applicationInfo
  type: object
- description: The address where to send the invoice. > The `billingAddress` object is required in the following scenarios. Include all of the fields within this object. >* For 3D Secure 2 transactions in all browse
  name: billingAddress
  type: object
- description: The shopper's browser information. > For 3D Secure, the full object is required for web integrations. For mobile app integrations, include the `userAgent` and `acceptHeader` fields to indicate that yo
  name: browserInfo
  type: object
- description: The delay between the authorisation and scheduled auto-capture, specified in hours.
  name: captureDelayHours
  type: integer
- description: 'The shopper''s date of birth. Format [ISO-8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DD'
  name: dateOfBirth
  type: string
- description: The forex quote as returned in the response of the forex service.
  name: dccQuote
  type: object
- description: The address where the purchased goods should be delivered.
  name: deliveryAddress
  type: object
- description: 'The date and time the purchased goods should be delivered. Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DDThh:mm:ss.sssTZD Example: 2017-07-17T13:42:40.428+01:00'
  name: deliveryDate
  type: string
- description: A string containing the shopper's device fingerprint. For more information, refer to [Device fingerprinting](https://docs.adyen.com/risk-management/device-fingerprinting).
  name: deviceFingerprint
  type: string
- description: An integer value that is added to the normal fraud score. The value can be either positive or negative.
  name: fraudOffset
  type: integer
- description: Contains installment settings. For more information, refer to [Installments](https://docs.adyen.com/payment-methods/cards/credit-card-installments).
  name: installments
  type: object
- description: The `localizedShopperStatement` field lets you use dynamic values for your shopper statement in a local character set. If not supplied, left empty, or for cross-border transactions, **shopperStatement
  name: localizedShopperStatement
  type: object
- description: The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activi
  name: mcc
  type: string
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle. The same merchant order reference sho
  name: merchantOrderReference
  type: string
- description: Additional risk fields for 3D Secure 2. > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow.
  name: merchantRiskIndicator
  type: object
- description: 'Metadata consists of entries, each of which includes a key and a value. Limits: * Maximum 20 key-value pairs per request. When exceeding, the "177" error occurs: "Metadata size exceeds limit". * Maxim'
  name: metadata
  type: object
- description: When you are doing multiple partial (gift card) payments, this is the `pspReference` of the first payment. We use this to link the multiple payments to each other. As your own reference for linking mu
  name: orderReference
  type: string
- description: The collection that contains the type of the payment method and its specific information.
  name: paymentMethod
  type: object
- description: The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/classic-integration/recurring-payments).
  name: recurring
  type: object
- description: 'Defines a recurring payment type. Required when creating a token to store payment details or using stored payment details. Allowed values: * `Subscription` – A transaction for a fixed or variable amou'
  name: recurringProcessingModel
  type: string
- description: The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a require
  name: reference
  type: string
- description: 'Some payment methods require defining a value for this field to specify how to process the transaction. For the Bancontact payment method, it can be set to: * `maestro` (default), to be processed like'
  name: selectedBrand
  type: string
- description: The `recurringDetailReference` you want to use for this payment. The value `LATEST` can be used to select the most recently stored recurring detail.
  name: selectedRecurringDetailReference
  type: string
- description: A session ID used to identify a payment session.
  name: sessionId
  type: string
- description: The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. > For 3D Secure 2 transactions, schemes require `shopperEmail` for all browser-based and m
  name: shopperEmail
  type: string
- description: The shopper's IP address. In general, we recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks). > For 3D Se
  name: shopperIP
  type: string
- description: Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction b
  name: shopperInteraction
  type: string
- description: The combination of a language code and a country code to specify the language to be used in the payment.
  name: shopperLocale
  type: string
- description: The shopper's full name.
  name: shopperName
  type: object
- description: 'Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identif'
  name: shopperReference
  type: string
- description: 'The text to be shown on the shopper''s bank statement. We recommend sending a maximum of 22 characters, otherwise banks might truncate the string. Allowed characters: **a-z**, **A-Z**, **0-9**, spaces,'
  name: shopperStatement
  type: string
- description: The shopper's social security number.
  name: socialSecurityNumber
  type: string
- description: An array of objects specifying how the payment should be split when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information) or [I
  name: splits
  type: array
- description: Required for Adyen for Platforms integrations if you have a platform setup. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-referen
  name: store
  type: string
- description: The shopper's telephone number.
  name: telephoneNumber
  type: string
- description: Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer to [Online payments](https://docs.adyen.com/online-payments) or [Classic integration](h
  name: threeDS2RequestData
  type: object
- description: If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation.
  name: threeDSAuthenticationOnly
  type: boolean
- description: The reference value to aggregate sales totals in reporting. When not specified, the store field is used (if available).
  name: totalsGroup
  type: string
- description: Set to true if the payment should be routed to a trusted MID.
  name: trustedShopper
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-balance-check-request-schema.json
slug: checkout-balance-check-request
tags:
- Payments
- Financial Services
- Fintech
title: BalanceCheckRequest
---
