---
description: DeleteBankAccountRequest schema from Adyen API
layout: schema
name: DeleteBankAccountRequest
properties_list:
- description: The code of the Account Holder from which to delete the Bank Account(s).
  name: accountHolderCode
  type: string
- description: The code(s) of the Bank Accounts to be deleted.
  name: bankAccountUUIDs
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-delete-bank-account-request-schema.json
slug: accounts-delete-bank-account-request
tags:
- Payments
- Financial Services
- Fintech
title: DeleteBankAccountRequest
---
