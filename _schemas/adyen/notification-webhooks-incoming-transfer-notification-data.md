---
description: IncomingTransferNotificationData schema from Adyen API
layout: schema
name: IncomingTransferNotificationData
properties_list:
- description: Contains information about the account holder.
  name: accountHolder
  type: object
- description: The amount converted to the balance account's currency, in case the original transaction currency is different. * A _positive_ value means the amount is added to the balance account. * A _negative_ va
  name: amount
  type: object
- description: Contains information about the balance account.
  name: balanceAccount
  type: object
- description: Unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: Contains information about the other party in the transaction.
  name: counterparty
  type: object
- description: Date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**.
  name: creationDate
  type: string
- description: Your description for the transfer. If you send a description longer than 140 characters, the text is truncated.
  name: description
  type: string
- description: The ID of the resource.
  name: id
  type: string
- description: Contains the amount and type of modification that triggered the notification. For example, this object contains the amount of a partial cancellation or partial expired authorisation.
  name: modification
  type: object
- description: The amount in the original currency of the transaction. * A _positive_ value means the amount is added to the balance account. * A _negative_ value means the amount is deducted from the balance accoun
  name: originalAmount
  type: object
- description: The ID of the original payment authorisation, refund, or funds transfer request. Use this to trace the original request from the `balancePlatform.payment.created` webhook.
  name: paymentId
  type: string
- description: Contains information about the payment instrument.
  name: paymentInstrument
  type: object
- description: Contains information about the related platform payment.
  name: platformPayment
  type: object
- description: An Adyen-generated unique reference for the transfer.
  name: reference
  type: string
- description: The reference sent to or received from the counterparty. * For outgoing funds, this is the [`referenceForBeneficiary`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_r
  name: referenceForBeneficiary
  type: string
- description: The event status. The possible values depend on the `type`. * **Authorised**, **Refused**, or **Error** for type `balancePlatform.payment.created` * **Expired** or **Cancelled** for type `balancePlatf
  name: status
  type: string
- description: Indicates the expected settlement date of this transaction, in ISO 8601 extended format. For example, **2021-08-17T15:34:37+02:00**.
  name: valueDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-incoming-transfer-notification-data-schema.json
slug: notification-webhooks-incoming-transfer-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: IncomingTransferNotificationData
---
