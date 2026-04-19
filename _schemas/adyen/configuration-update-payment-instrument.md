---
description: UpdatePaymentInstrument schema from Adyen API
layout: schema
name: UpdatePaymentInstrument
properties_list:
- description: The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id) associated with the payment instrument.
  name: balanceAccountId
  type: string
- description: Contains the business account details. Returned when you create a payment instrument with `type` **bankAccount**.
  name: bankAccount
  type: object
- description: Contains information about the card payment instrument. Returned when you create a payment instrument with `type` **card**.
  name: card
  type: object
- description: Your description for the payment instrument, maximum 300 characters.
  name: description
  type: string
- description: The unique identifier of the payment instrument.
  name: id
  type: string
- description: The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**.
  name: issuingCountryCode
  type: string
- description: The unique identifier of the [payment instrument group](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id) to which the payment instrument belongs.
  name: paymentInstrumentGroupId
  type: string
- description: Your reference for the payment instrument, maximum 150 characters.
  name: reference
  type: string
- description: The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set to **active** by default. However, there can be exceptions for cards based on the `card
  name: status
  type: string
- description: Comment for the status of the payment instrument. Required if `statusReason` is **other**.
  name: statusComment
  type: string
- description: 'The reason for the status of the payment instrument. Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**, **suspectedFraud**, **transactionRule**, **othe'
  name: statusReason
  type: string
- description: 'Type of payment instrument. Possible value: **card**, **bankAccount**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-update-payment-instrument-schema.json
slug: configuration-update-payment-instrument
tags:
- Payments
- Financial Services
- Fintech
title: UpdatePaymentInstrument
---
