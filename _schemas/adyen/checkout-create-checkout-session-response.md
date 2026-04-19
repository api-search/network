---
description: CreateCheckoutSessionResponse schema from Adyen API
layout: schema
name: CreateCheckoutSessionResponse
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
- description: 'List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types). Example: `"allowedPay'
  name: allowedPaymentMethods
  type: array
- description: The amount of the payment.
  name: amount
  type: object
- description: Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).
  name: applicationInfo
  type: object
- description: Configuration data for 3DS payments.
  name: authenticationData
  type: object
- description: The address where to send the invoice.
  name: billingAddress
  type: object
- description: 'List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types). Example: `"blockedPaym'
  name: blockedPaymentMethods
  type: array
- description: The delay between the authorisation and scheduled auto-capture, specified in hours.
  name: captureDelayHours
  type: integer
- description: The platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try
  name: channel
  type: string
- description: Information regarding the company.
  name: company
  type: object
- description: The shopper's two-letter country code.
  name: countryCode
  type: string
- description: The shopper's date of birth in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
  name: dateOfBirth
  type: string
- description: 'The date and time when the purchased goods should be delivered. [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**.'
  name: deliverAt
  type: string
- description: The address where the purchased goods should be delivered.
  name: deliveryAddress
  type: object
- description: When true and `shopperReference` is provided, the shopper will be asked if the payment details should be stored for future one-click payments.
  name: enableOneClick
  type: boolean
- description: When true and `shopperReference` is provided, the payment details will be tokenized for payouts.
  name: enablePayOut
  type: boolean
- description: When true and `shopperReference` is provided, the payment details will be tokenized for recurring payments.
  name: enableRecurring
  type: boolean
- description: The date the session expires in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. When not specified, the expiry date is set to 1 hour after session creation. You cannot set th
  name: expiresAt
  type: string
- description: The person or entity funding the money.
  name: fundOrigin
  type: object
- description: the person or entity receiving the money
  name: fundRecipient
  type: object
- description: A unique identifier of the session.
  name: id
  type: string
- description: A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example, **card** to specify installment options f
  name: installmentOptions
  type: object
- description: Price and product information about the purchased items, to be included on the invoice sent to the shopper. > This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Zi
  name: lineItems
  type: array
- description: The mandate details to initiate recurring transaction.
  name: mandate
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
- description: 'Metadata consists of entries, each of which includes a key and a value. Limits: * Maximum 20 key-value pairs per request. * Maximum 20 characters per key. * Maximum 80 characters per value.'
  name: metadata
  type: object
- description: 'Indicates the type of front end integration. Possible values: * **embedded** (default): Drop-in or Components integration * **hosted**: Hosted Checkout integration'
  name: mode
  type: string
- description: Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires).
  name: mpiData
  type: object
- description: Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#chargebacks-and-disputes).
  name: platformChargebackLogic
  type: object
- description: Date after which no further authorisations shall be performed. Only for 3D Secure 2.
  name: recurringExpiry
  type: string
- description: Minimum number of days between authorisations. Only for 3D Secure 2.
  name: recurringFrequency
  type: string
- description: 'Defines a recurring payment type. Required when creating a token to store payment details. Allowed values: * `Subscription` – A transaction for a fixed or variable amount, which follows a fixed schedu'
  name: recurringProcessingModel
  type: string
- description: Specifies the redirect method (GET or POST) when redirecting back from the issuer.
  name: redirectFromIssuerMethod
  type: string
- description: Specifies the redirect method (GET or POST) when redirecting to the issuer.
  name: redirectToIssuerMethod
  type: string
- description: The reference to uniquely identify a payment.
  name: reference
  type: string
- description: The URL to return to when a redirect payment is completed.
  name: returnUrl
  type: string
- description: Any risk-related settings to apply to the payment.
  name: riskData
  type: object
- description: The payment session data you need to pass to your front end.
  name: sessionData
  type: string
- description: The shopper's email address.
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
- description: The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're enrolled in the PayPal Seller Protection program.
  name: shopperName
  type: object
- description: 'Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identifiable information (PII), for exam'
  name: shopperReference
  type: string
- description: 'The text to be shown on the shopper''s bank statement. We recommend sending a maximum of 22 characters, otherwise banks might truncate the string. Allowed characters: **a-z**, **A-Z**, **0-9**, spaces,'
  name: shopperStatement
  type: string
- description: Set to true to show the payment amount per installment.
  name: showInstallmentAmount
  type: boolean
- description: Set to **true** to show a button that lets the shopper remove a stored payment method.
  name: showRemovePaymentMethodButton
  type: boolean
- description: The shopper's social security number.
  name: socialSecurityNumber
  type: string
- description: Boolean value indicating whether the card payment method should be split into separate debit and credit options.
  name: splitCardFundingSources
  type: boolean
- description: An array of objects specifying how to split a payment when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information), [Classic Plat
  name: splits
  type: array
- description: Required for Adyen for Platforms integrations if you have a platform setup. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-referen
  name: store
  type: string
- description: When this is set to **true** and the `shopperReference` is provided, the payment details will be stored.
  name: storePaymentMethod
  type: boolean
- description: 'Indicates if the details of the payment method will be stored for the shopper. Possible values: * **disabled** – No details will be stored (default). * **askForConsent** – If the `shopperReference` is'
  name: storePaymentMethodMode
  type: string
- description: The shopper's telephone number.
  name: telephoneNumber
  type: string
- description: Sets a custom theme for [Hosted Checkout](https://docs.adyen.com/online-payments/build-your-integration/?platform=Web&integration=Hosted+Checkout). The value can be any of the **Theme ID** values from
  name: themeId
  type: string
- description: If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation.
  name: threeDSAuthenticationOnly
  type: boolean
- description: Set to true if the payment should be routed to a trusted MID.
  name: trustedShopper
  type: boolean
- description: The URL for the Hosted Checkout page. Redirect the shopper to this URL so they can make the payment.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-create-checkout-session-response-schema.json
slug: checkout-create-checkout-session-response
tags:
- Payments
- Financial Services
- Fintech
title: CreateCheckoutSessionResponse
---
