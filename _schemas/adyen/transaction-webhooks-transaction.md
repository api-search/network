---
description: Transaction schema from Adyen API
layout: schema
name: Transaction
properties_list:
- description: Contains information about the account holder associated with the `balanceAccount`.
  name: accountHolder
  type: object
- description: Contains information about the amount of the transaction.
  name: amount
  type: object
- description: Contains information about the balance account involved in the transaction.
  name: balanceAccount
  type: object
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: The date the transaction was booked into the balance account.
  name: bookingDate
  type: string
- description: The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**.
  name: creationDate
  type: string
- description: The unique identifier of the transaction.
  name: id
  type: string
- description: 'The status of the transaction. Possible values: * **pending**: The transaction is still pending. * **booked**: The transaction has been booked to the balance account.'
  name: status
  type: string
- description: Contains information about the transfer related to the transaction.
  name: transfer
  type: object
- description: The date the transfer amount becomes available in the balance account.
  name: valueDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transaction-webhooks-transaction-schema.json
slug: transaction-webhooks-transaction
tags:
- Payments
- Financial Services
- Fintech
title: Transaction
---
