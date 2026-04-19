---
description: Account schema from Adyen API
layout: schema
name: Account
properties_list:
- description: The code of the account.
  name: accountCode
  type: string
- description: The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank acco
  name: bankAccountUUID
  type: string
- description: The beneficiary of the account.
  name: beneficiaryAccount
  type: string
- description: The reason that a beneficiary has been set up for this account. This may have been supplied during the setup of a beneficiary at the discretion of the executing user.
  name: beneficiaryMerchantReference
  type: string
- description: A description of the account.
  name: description
  type: string
- description: A set of key and value pairs for general use by the merchant. The keys do not have specific names and may be used for storing miscellaneous data as desired. > Note that during an update of metadata, t
  name: metadata
  type: object
- description: The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code.
  name: payoutMethodCode
  type: string
- description: The account's payout schedule.
  name: payoutSchedule
  type: object
- description: 'Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.'
  name: payoutSpeed
  type: string
- description: 'The status of the account. Possible values: `Active`, `Inactive`, `Suspended`, `Closed`.'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-account-schema.json
slug: accounts-account
tags:
- Payments
- Financial Services
- Fintech
title: Account
---
