---
description: RecurringDetail schema from Adyen API
layout: schema
name: RecurringDetail
properties_list:
- description: This field contains additional data, which may be returned in a particular response. The additionalData object consists of entries, each of which includes the key and value.
  name: additionalData
  type: object
- description: The alias of the credit card number. Applies only to recurring contracts storing credit card details
  name: alias
  type: string
- description: The alias type of the credit card number. Applies only to recurring contracts storing credit card details.
  name: aliasType
  type: string
- description: A container for bank account data.
  name: bank
  type: object
- description: The billing address.
  name: billingAddress
  type: object
- description: A container for card data.
  name: card
  type: object
- description: Types of recurring contracts.
  name: contractTypes
  type: array
- description: The date when the recurring details were created.
  name: creationDate
  type: string
- description: The `pspReference` of the first recurring payment that created the recurring detail.
  name: firstPspReference
  type: string
- description: An optional descriptive name for this recurring detail.
  name: name
  type: string
- description: Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa. This contains either the Mastercard Trace ID or
  name: networkTxReference
  type: string
- description: The type or sub-brand of a payment method used, e.g. Visa Debit, Visa Corporate, etc. For more information, refer to [PaymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodva
  name: paymentMethodVariant
  type: string
- description: The reference that uniquely identifies the recurring detail.
  name: recurringDetailReference
  type: string
- description: The name of the shopper.
  name: shopperName
  type: object
- description: A shopper's social security number (only in countries where it is legal to collect).
  name: socialSecurityNumber
  type: string
- description: ''
  name: tokenDetails
  type: object
- description: The payment method, such as “mc", "visa", "ideal", "paypal".
  name: variant
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-recurring-detail-schema.json
slug: recurring-recurring-detail
tags:
- Payments
- Financial Services
- Fintech
title: RecurringDetail
---
