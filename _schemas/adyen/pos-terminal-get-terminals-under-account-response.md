---
description: GetTerminalsUnderAccountResponse schema from Adyen API
layout: schema
name: GetTerminalsUnderAccountResponse
properties_list:
- description: Your company account.
  name: companyAccount
  type: string
- description: Array that returns a list of all terminals that are in the inventory of the company account.
  name: inventoryTerminals
  type: array
- description: Array that returns a list of all merchant accounts belonging to the company account.
  name: merchantAccounts
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-get-terminals-under-account-response-schema.json
slug: pos-terminal-get-terminals-under-account-response
tags:
- Payments
- Financial Services
- Fintech
title: GetTerminalsUnderAccountResponse
---
