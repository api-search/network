---
description: DebitAccountHolderResponse schema from Adyen API
layout: schema
name: DebitAccountHolderResponse
properties_list:
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account.
  name: bankAccountUUID
  type: string
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: List of the `reference` values from the `split` array in the request.
  name: merchantReferences
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-debit-account-holder-response-schema.json
slug: funds-debit-account-holder-response
tags:
- Payments
- Financial Services
- Fintech
title: DebitAccountHolderResponse
---
