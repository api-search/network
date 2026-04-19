---
description: Transaction schema from Adyen API
layout: schema
name: Transaction
properties_list:
- description: The amount of the transaction.
  name: amount
  type: object
- description: The details of the bank account to where a payout was made.
  name: bankAccountDetail
  type: object
- description: The merchant reference of a related capture.
  name: captureMerchantReference
  type: string
- description: The psp reference of a related capture.
  name: capturePspReference
  type: string
- description: The date on which the transaction was performed.
  name: creationDate
  type: string
- description: A description of the transaction.
  name: description
  type: string
- description: The code of the account to which funds were credited during an outgoing fund transfer.
  name: destinationAccountCode
  type: string
- description: The psp reference of the related dispute.
  name: disputePspReference
  type: string
- description: The reason code of a dispute.
  name: disputeReasonCode
  type: string
- description: The merchant reference of a transaction.
  name: merchantReference
  type: string
- description: The psp reference of the related authorisation or transfer.
  name: paymentPspReference
  type: string
- description: The psp reference of the related payout.
  name: payoutPspReference
  type: string
- description: The psp reference of a transaction.
  name: pspReference
  type: string
- description: The code of the account from which funds were debited during an incoming fund transfer.
  name: sourceAccountCode
  type: string
- description: 'The status of the transaction. >Permitted values: `PendingCredit`, `CreditFailed`, `CreditClosed`, `CreditSuspended`, `Credited`, `Converted`, `PendingDebit`, `DebitFailed`, `Debited`, `DebitReversedR'
  name: transactionStatus
  type: string
- description: The transfer code of the transaction.
  name: transferCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-transaction-schema.json
slug: notifications-transaction
tags:
- Payments
- Financial Services
- Fintech
title: Transaction
---
