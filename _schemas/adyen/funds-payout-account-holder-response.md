---
description: PayoutAccountHolderResponse schema from Adyen API
layout: schema
name: PayoutAccountHolderResponse
properties_list:
- description: The unique ID of the Bank Account to which the payout was made.
  name: bankAccountUUID
  type: string
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The value supplied by the executing user when initiating the transfer; may be used to link multiple transactions.
  name: merchantReference
  type: string
- description: 'Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.'
  name: payoutSpeed
  type: string
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-payout-account-holder-response-schema.json
slug: funds-payout-account-holder-response
tags:
- Payments
- Financial Services
- Fintech
title: PayoutAccountHolderResponse
---
