---
description: DebitAccountHolderRequest schema from Adyen API
layout: schema
name: DebitAccountHolderRequest
properties_list:
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: The amount to be debited from the account holder's bank account.
  name: amount
  type: object
- description: The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account.
  name: bankAccountUUID
  type: string
- description: 'A description of the direct debit. Maximum length: 35 characters. Allowed characters: **a-z**, **A-Z**, **0-9**, and special characters **/?:().,''+ ";**.'
  name: description
  type: string
- description: Your merchant account.
  name: merchantAccount
  type: string
- description: Contains instructions on how to split the funds between the accounts in your platform. The request must have at least one split item.
  name: splits
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-debit-account-holder-request-schema.json
slug: funds-debit-account-holder-request
tags:
- Payments
- Financial Services
- Fintech
title: DebitAccountHolderRequest
---
