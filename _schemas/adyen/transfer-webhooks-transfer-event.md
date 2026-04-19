---
description: TransferEvent schema from Adyen API
layout: schema
name: TransferEvent
properties_list:
- description: The original journal amount.
  name: amount
  type: object
- description: The amount adjustments in this transfer.
  name: amountAdjustments
  type: array
- description: The date when the transfer request was sent.
  name: bookingDate
  type: string
- description: The estimated time the beneficiary should have access to the funds.
  name: estimatedArrivalTime
  type: string
- description: The unique identifier of the transfer event.
  name: id
  type: string
- description: Payment modification.
  name: modification
  type: object
- description: The list of the balance mutation per event.
  name: mutations
  type: array
- description: The amount in the original currency.
  name: originalAmount
  type: object
- description: The reason for the transfer status.
  name: reason
  type: string
- description: The status of the transfer event.
  name: status
  type: string
- description: The id of the transaction that is related to this accounting event. Only sent for events of type **accounting** where the balance changes.
  name: transactionId
  type: string
- description: 'The type of the transfer event. Possible values: **accounting**, **tracking**.'
  name: type
  type: string
- description: The date when the tracking status was updated.
  name: updateDate
  type: string
- description: A future date, when the funds are expected to be deducted from or credited to the balance account.
  name: valueDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-transfer-event-schema.json
slug: transfer-webhooks-transfer-event
tags:
- Payments
- Financial Services
- Fintech
title: TransferEvent
---
