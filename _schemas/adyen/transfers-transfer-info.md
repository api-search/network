---
description: TransferInfo schema from Adyen API
layout: schema
name: TransferInfo
properties_list:
- description: The amount of the transfer.
  name: amount
  type: object
- description: The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id).
  name: balanceAccountId
  type: string
- description: 'The type of transfer. Possible values: - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account'
  name: category
  type: string
- description: The recipient of the funds transfer. A bank account, a balance account, or a transfer instrument is required.
  name: counterparty
  type: object
- description: Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated. Supported charact
  name: description
  type: string
- description: The unique identifier of the source [payment instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/paymentInstruments__resParam_id).
  name: paymentInstrumentId
  type: string
- description: 'The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**. Possible values: * **regular**'
  name: priority
  type: string
- description: Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.
  name: reference
  type: string
- description: A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds. Supporte
  name: referenceForBeneficiary
  type: string
- description: The ultimate sender of the funds of the transfer (ultimate debtor).
  name: ultimateParty
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-transfer-info-schema.json
slug: transfers-transfer-info
tags:
- Payments
- Financial Services
- Fintech
title: TransferInfo
---
