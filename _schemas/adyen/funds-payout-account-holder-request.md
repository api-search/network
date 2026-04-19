---
description: PayoutAccountHolderRequest schema from Adyen API
layout: schema
name: PayoutAccountHolderRequest
properties_list:
- description: The code of the account from which the payout is to be made.
  name: accountCode
  type: string
- description: The code of the Account Holder who owns the account from which the payout is to be made. The Account Holder is the party to which the payout will be made.
  name: accountHolderCode
  type: string
- description: An object containing the currency and value of the payout. If the account has multiple currencies, specify the currency to be used. If the `bankAccountUUID` is provided in the request, the currency su
  name: amount
  type: object
- description: The unique ID of the Bank Account held by the Account Holder to which the payout is to be made. If left blank, a bank account is automatically selected.
  name: bankAccountUUID
  type: string
- description: 'A description of the payout. Maximum 200 characters. Allowed: **abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?:().,''+ ";**'
  name: description
  type: string
- description: A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.
  name: merchantReference
  type: string
- description: The unique ID of the payout method held by the Account Holder to which the payout is to be made. If left blank, a payout instrument is automatically selected.
  name: payoutMethodCode
  type: string
- description: 'Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.'
  name: payoutSpeed
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-payout-account-holder-request-schema.json
slug: funds-payout-account-holder-request
tags:
- Payments
- Financial Services
- Fintech
title: PayoutAccountHolderRequest
---
