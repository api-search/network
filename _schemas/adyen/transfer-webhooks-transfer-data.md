---
description: TransferData schema from Adyen API
layout: schema
name: TransferData
properties_list:
- description: The account holder associated with the balance account used in the transfer.
  name: accountHolder
  type: object
- description: The amount of the transfer.
  name: amount
  type: object
- description: Contains information about the balance account involved in the transfer.
  name: balanceAccount
  type: object
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: The list of the latest balance statuses in the transfer.
  name: balances
  type: array
- description: 'The category of transfer. Possible values: - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank acc'
  name: category
  type: string
- description: The relevant data according to the transfer category.
  name: categoryData
  type: object
- description: The other party in the transfer.
  name: counterparty
  type: object
- description: The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**.
  name: creationDate
  type: string
- description: Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated. Supported charact
  name: description
  type: string
- description: 'The direction of the transfer. Possible values: **incoming**, **outgoing**.'
  name: direction
  type: string
- description: The list of events leading up to the current status of the transfer.
  name: events
  type: array
- description: The ID of the resource.
  name: id
  type: string
- description: Contains information about the payment instrument used in the transfer.
  name: paymentInstrument
  type: object
- description: Additional information about the status of the transfer.
  name: reason
  type: string
- description: Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.
  name: reference
  type: string
- description: A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds. Supporte
  name: referenceForBeneficiary
  type: string
- description: 'The sequence number of the transfer notification. The numbers start from 1 and increase with each new notification for a specific transfer. It can help you restore the correct sequence of events even '
  name: sequenceNumber
  type: integer
- description: The result of the transfer. For example, **authorised**, **refused**, or **error**.
  name: status
  type: string
- description: The tracking information for the transfer.
  name: tracking
  type: object
- description: Contains the results of the evaluation of the transaction rules.
  name: transactionRulesResult
  type: object
- description: The type of transfer or transaction. For example, **refund**, **payment**, **internalTransfer**, **bankTransfer**.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-transfer-data-schema.json
slug: transfer-webhooks-transfer-data
tags:
- Payments
- Financial Services
- Fintech
title: TransferData
---
