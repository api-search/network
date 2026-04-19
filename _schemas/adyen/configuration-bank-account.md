---
description: BankAccount schema from Adyen API
layout: schema
name: BankAccount
properties_list:
- description: Contains the bank account details. The fields required in this object depend on the country of the bank account and the currency of the transfer.
  name: accountIdentification
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-bank-account-schema.json
slug: configuration-bank-account
tags:
- Payments
- Financial Services
- Fintech
title: BankAccount
---
