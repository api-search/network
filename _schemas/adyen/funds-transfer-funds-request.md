---
description: TransferFundsRequest schema from Adyen API
layout: schema
name: TransferFundsRequest
properties_list:
- description: The amount to be transferred.
  name: amount
  type: object
- description: The code of the account to which the funds are to be credited. >The state of the Account Holder of this account must be Active.
  name: destinationAccountCode
  type: string
- description: A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.
  name: merchantReference
  type: string
- description: The code of the account from which the funds are to be debited. >The state of the Account Holder of this account must be Active and allow payouts.
  name: sourceAccountCode
  type: string
- description: The code related to the type of transfer being performed. >The permitted codes differ for each platform account and are defined in their service level agreement.
  name: transferCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-transfer-funds-request-schema.json
slug: funds-transfer-funds-request
tags:
- Payments
- Financial Services
- Fintech
title: TransferFundsRequest
---
