---
description: BankAccountV3 schema from Adyen API
layout: schema
name: BankAccountV3
properties_list:
- description: Information about the owner of the bank account.
  name: accountHolder
  type: object
- description: Contains the bank account details. The fields required in this object depend on the country of the bank account and the currency of the transfer.
  name: accountIdentification
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-bank-account-v3-schema.json
slug: transfers-bank-account-v3
tags:
- Payments
- Financial Services
- Fintech
title: BankAccountV3
---
