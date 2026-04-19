---
description: AccountHolderPayoutNotificationContent schema from Adyen API
layout: schema
name: AccountHolderPayoutNotificationContent
properties_list:
- description: The code of the account from which the payout was made.
  name: accountCode
  type: string
- description: The code of the Account Holder to which the payout was made.
  name: accountHolderCode
  type: string
- description: The payout amounts (per currency).
  name: amounts
  type: array
- description: Details of the Bank Account to which the payout was made.
  name: bankAccountDetail
  type: object
- description: A description of the payout.
  name: description
  type: string
- description: The estimated date of arrival.
  name: estimatedArrivalDate
  type: object
- description: Invalid fields list.
  name: invalidFields
  type: array
- description: The merchant reference.
  name: merchantReference
  type: string
- description: The PSP reference of the original payout.
  name: originalPspReference
  type: string
- description: The country code of the bank from which the payout was initiated.
  name: payoutAccountCountry
  type: string
- description: The account number of the bank from which the payout was initiated.
  name: payoutAccountNumber
  type: string
- description: The balance account id to which payment was made
  name: payoutBalanceAccountId
  type: string
- description: The name of the bank the payout from which the payout was initiated.
  name: payoutBankName
  type: string
- description: The branch code of the bank from which the payout was initiated.
  name: payoutBranchCode
  type: string
- description: The unique payout identifier.
  name: payoutReference
  type: integer
- description: 'Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.'
  name: payoutSpeed
  type: string
- description: The payout status.
  name: status
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-account-holder-payout-notification-content-schema.json
slug: notifications-account-holder-payout-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderPayoutNotificationContent
---
