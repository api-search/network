---
description: PaymentLinkRequest schema from Adyen API
layout: schema
name: PaymentLinkRequest
properties_list:
- description: 'List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types). Example: `"allowedPay'
  name: allowedPaymentMethods
  type: array
- description: The payment amount and currency.
  name: amount
  type: object
- description: Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).
  name: applicationInfo
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
- description: The shopper's two-letter country code.
  name: countryCode
  type: string
- description: 'The shopper''s date of birth. Format [ISO-8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DD'
  name: dateOfBirth
  type: string
- description: 'The date and time when the purchased goods should be delivered. [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**.'
  name: deliverAt
  type: string
- description: The address where the purchased goods should be delivered.
  name: deliveryAddress
  type: object
- description: 'A short description visible on the payment page. Maximum length: 280 characters.'
  name: description
  type: string
- description: 'The date when the payment link expires. [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format with time zone offset: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. The maximum e'
  name: expiresAt
  type: string
- description: A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example, **card** to specify installment options f
  name: installmentOptions
  type: object
- description: Price and product information about the purchased items, to be included on the invoice sent to the shopper. This parameter is required for open invoice (_buy now, pay later_) payment methods such Afte
  name: lineItems
  type: array
- description: Indicates if the payment must be [captured manually](https://docs.adyen.com/online-payments/capture).
  name: manualCapture
  type: boolean
- description: The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activi
  name: mcc
  type: string
- description: The merchant account identifier for which the payment link is created.
  name: merchantAccount
  type: string
- description: This reference allows linking multiple transactions to each other for reporting purposes (for example, order auth-rate). The reference should be unique per billing cycle.
  name: merchantOrderReference
  type: string
- description: 'Metadata consists of entries, each of which includes a key and a value. Limitations: * Maximum 20 key-value pairs per request. Otherwise, error "177" occurs: "Metadata size exceeds limit" * Maximum 20'
  name: metadata
  type: object
- description: 'Defines a recurring payment type. Required when `storePaymentMethodMode` is set to **askForConsent** or **enabled**. Possible values: * **Subscription** – A transaction for a fixed or variable amount,'
  name: recurringProcessingModel
  type: string
- description: A reference that is used to uniquely identify the payment in future communications about the payment status.
  name: reference
  type: string
- description: List of fields that the shopper has to provide on the payment page before completing the payment. For more information, refer to [Provide shopper information](https://docs.adyen.com/unified-commerce/p
  name: requiredShopperFields
  type: array
- description: Website URL used for redirection after payment is completed. If provided, a **Continue** button will be shown on the payment page. If shoppers select the button, they are redirected to the specified U
  name: returnUrl
  type: string
- description: Indicates whether the payment link can be reused for multiple payments. If not provided, this defaults to **false** which means the link can be used for one successful payment only.
  name: reusable
  type: boolean
- description: Any risk-related settings to apply to the payment.
  name: riskData
  type: object
- description: The shopper's email address.
  name: shopperEmail
  type: string
- description: The language to be used in the payment page, specified by a combination of a language and country code. For example, `en-US`. For a list of shopper locales that Pay by Link supports, refer to [Languag
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
- description: Set to **false** to hide the button that lets the shopper remove a stored payment method.
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
- description: The physical store, for which this payment is processed.
  name: store
  type: string
- description: 'Indicates if the details of the payment method will be stored for the shopper. Possible values: * **disabled** – No details will be stored (default). * **askForConsent** – If the `shopperReference` is'
  name: storePaymentMethodMode
  type: string
- description: The shopper's telephone number.
  name: telephoneNumber
  type: string
- description: A [theme](https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#themes) to customize the appearance of the payment page. If not specified, the payment page is rendered according to the
  name: themeId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-link-request-schema.json
slug: checkout-payment-link-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentLinkRequest
---
