---
description: PaymentInstrumentUpdateRequest schema from Adyen API
layout: schema
name: PaymentInstrumentUpdateRequest
properties_list:
- description: The unique identifier of the balance account associated with this payment instrument. >You can only change the balance account ID if the payment instrument has **inactive** status.
  name: balanceAccountId
  type: string
- description: Object that contains information about the card payment instrument.
  name: card
  type: object
- description: The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set to **active** by default. However, there can be exceptions for cards based on the `card
  name: status
  type: string
- description: Comment for the status of the payment instrument. Required if `statusReason` is **other**.
  name: statusComment
  type: string
- description: 'The reason for updating the status of the payment instrument. Possible values: **lost**, **stolen**, **damaged**, **suspectedFraud**, **expired**, **endOfLife**, **accountClosure**, **other**. If the '
  name: statusReason
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-payment-instrument-update-request-schema.json
slug: configuration-payment-instrument-update-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentInstrumentUpdateRequest
---
