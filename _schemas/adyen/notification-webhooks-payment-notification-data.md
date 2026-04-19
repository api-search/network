---
description: PaymentNotificationData schema from Adyen API
layout: schema
name: PaymentNotificationData
properties_list:
- description: Contains information about the account holder.
  name: accountHolder
  type: object
- description: The amount converted to the balance account's currency, in case the original transaction currency is different. * A _positive_ value means the amount is added to the balance account. * A _negative_ va
  name: amount
  type: object
- description: The authorisation code for the payment.
  name: authCode
  type: string
- description: Contains information about the balance account.
  name: balanceAccount
  type: object
- description: Unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: Date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**.
  name: creationDate
  type: string
- description: Your description for the transfer. If you send a description longer than 140 characters, the text is truncated.
  name: description
  type: string
- description: The ID of the resource.
  name: id
  type: string
- description: Contains information about the merchant that processed the payment. This object is only included for payment authorisation requests and captures.
  name: merchantData
  type: object
- description: Contains the amount and type of modification that triggered the notification. For example, this object contains the amount of a partial cancellation or partial expired authorisation.
  name: modification
  type: object
- description: The amount in the original currency of the transaction. * A _positive_ value means the amount is added to the balance account. * A _negative_ value means the amount is deducted from the balance accoun
  name: originalAmount
  type: object
- description: Contains information about the payment instrument.
  name: paymentInstrument
  type: object
- description: Contains information about the related platform payment.
  name: platformPayment
  type: object
- description: Contains information about how the payment was processed. For example, **ecommerce** for online or **pos** for point-of-sale payments.
  name: processingType
  type: string
- description: The [`reference`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the `/transfers` request. If you haven't provided any, Adyen generates a unique refere
  name: reference
  type: string
- description: The reference sent to or received from the counterparty. * For outgoing funds, this is the [`referenceForBeneficiary`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_r
  name: referenceForBeneficiary
  type: string
- description: If you're using [relayed authorisation](https://docs.adyen.com/issuing/processing-payments-for-cards#relayed-authorisation), this object contains information from the relayed authorisation response fr
  name: relayedAuthorisationData
  type: object
- description: The event status. The possible values depend on the `type`. * **Authorised**, **Refused**, or **Error** for type `balancePlatform.payment.created` * **Expired** or **Cancelled** for type `balancePlatf
  name: status
  type: string
- description: Contains results from the evaluation of [transaction rules](https://docs.adyen.com/issuing/transaction-rules).
  name: transactionRulesResult
  type: object
- description: Array of checks that Adyen performed to validate the payment and the result of each.
  name: validationResult
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-payment-notification-data-schema.json
slug: notification-webhooks-payment-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: PaymentNotificationData
---
