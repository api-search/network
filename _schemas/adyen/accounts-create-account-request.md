---
description: CreateAccountRequest schema from Adyen API
layout: schema
name: CreateAccountRequest
properties_list:
- description: The code of Account Holder under which to create the account.
  name: accountHolderCode
  type: string
- description: The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank acco
  name: bankAccountUUID
  type: string
- description: A description of the account, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`.
  name: description
  type: string
- description: A set of key and value pairs for general use by the merchant. The keys do not have specific names and may be used for storing miscellaneous data as desired. > Note that during an update of metadata, t
  name: metadata
  type: object
- description: The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code.
  name: payoutMethodCode
  type: string
- description: 'The payout schedule of the prospective account. >Permitted values: `DEFAULT`, `HOLD`, `DAILY`, `WEEKLY`, `MONTHLY`.'
  name: payoutSchedule
  type: string
- description: The reason for the payout schedule choice. >Required if the payoutSchedule is `HOLD`.
  name: payoutScheduleReason
  type: string
- description: 'Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.'
  name: payoutSpeed
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-create-account-request-schema.json
slug: accounts-create-account-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateAccountRequest
---
