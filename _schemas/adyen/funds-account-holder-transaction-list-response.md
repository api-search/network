---
description: AccountHolderTransactionListResponse schema from Adyen API
layout: schema
name: AccountHolderTransactionListResponse
properties_list:
- description: A list of the transactions.
  name: accountTransactionLists
  type: array
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-account-holder-transaction-list-response-schema.json
slug: funds-account-holder-transaction-list-response
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderTransactionListResponse
---
