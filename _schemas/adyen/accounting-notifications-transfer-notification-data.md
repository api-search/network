---
description: TransferNotificationData schema from Adyen API
layout: schema
name: TransferNotificationData
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
- description: The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id).
  name: balanceAccountId
  type: string
- description: The list of the latest balance statuses in the transfer.
  name: balances
  type: array
- description: 'The type of transfer. Possible values: - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account'
  name: category
  type: string
- description: The other party in the transfer.
  name: counterparty
  type: object
- description: A human-readable description for the transfer. You can use alphanumeric characters and hyphens. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.
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
- description: The capture's merchant reference included in the transfer.
  name: modificationMerchantReference
  type: string
- description: The capture reference included in the transfer.
  name: modificationPspReference
  type: string
- description: 'Indicates the method used for entering the PAN to initiate a transaction. Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**.'
  name: panEntryMode
  type: string
- description: Contains information about the payment instrument used in the transfer.
  name: paymentInstrument
  type: object
- description: The unique identifier of the source [payment instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/paymentInstruments__resParam_id).
  name: paymentInstrumentId
  type: string
- description: The payment's merchant reference included in the transfer.
  name: paymentMerchantReference
  type: string
- description: 'The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**. Possible values: * **regular**'
  name: priority
  type: string
- description: Contains information about how the payment was processed. For example, **ecommerce** for online or **pos** for in-person payments.
  name: processingType
  type: string
- description: The payment reference included in the transfer.
  name: pspPaymentReference
  type: string
- description: Additional information about the status of the transfer.
  name: reason
  type: string
- description: Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.
  name: reference
  type: string
- description: A reference that is sent to the recipient. This reference is also sent in all notification webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of fu
  name: referenceForBeneficiary
  type: string
- description: If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server.
  name: relayedAuthorisationData
  type: object
- description: 'The sequence number of the transfer notification. The numbers start from 1 and increase with each new notification for a specific transfer. It can help you restore the correct sequence of events even '
  name: sequenceNumber
  type: integer
- description: The result of the transfer. For example, **authorised**, **refused**, or **error**.
  name: status
  type: string
- description: The tracking information for the transfer.
  name: tracking
  type: object
- description: The ID of the transaction that is created based on the transfer.
  name: transactionId
  type: string
- description: Contains the results of the evaluation of the transaction rules.
  name: transactionRulesResult
  type: object
- description: The type of transfer or transaction. For example, **refund**, **payment**, **internalTransfer**, **bankTransfer**.
  name: type
  type: string
- description: The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information.
  name: validationFacts
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-transfer-notification-data-schema.json
slug: accounting-notifications-transfer-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: TransferNotificationData
---
