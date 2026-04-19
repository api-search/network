---
description: CreateAccountResponse schema from Adyen API
layout: schema
name: CreateAccountResponse
properties_list:
- description: The code of the new account.
  name: accountCode
  type: string
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank acco
  name: bankAccountUUID
  type: string
- description: The description of the account.
  name: description
  type: string
- description: A list of fields that caused the `/createAccount` request to fail.
  name: invalidFields
  type: array
- description: A set of key and value pairs containing metadata.
  name: metadata
  type: object
- description: The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code.
  name: payoutMethodCode
  type: string
- description: The payout schedule of the account.
  name: payoutSchedule
  type: object
- description: 'Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.'
  name: payoutSpeed
  type: string
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
- description: 'The status of the account. >Permitted values: `Active`.'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-create-account-response-schema.json
slug: accounts-create-account-response
tags:
- Payments
- Financial Services
- Fintech
title: CreateAccountResponse
---
