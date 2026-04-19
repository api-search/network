---
description: BankAccount schema from Adyen API
layout: schema
name: BankAccount
properties_list:
- description: The bank account number (without separators).
  name: bankAccountNumber
  type: string
- description: The bank city.
  name: bankCity
  type: string
- description: The location id of the bank. The field value is `nil` in most cases.
  name: bankLocationId
  type: string
- description: The name of the bank.
  name: bankName
  type: string
- description: The [Business Identifier Code](https://en.wikipedia.org/wiki/ISO_9362) (BIC) is the SWIFT address assigned to a bank. The field value is `nil` in most cases.
  name: bic
  type: string
- description: Country code where the bank is located. A valid value is an ISO two-character country code (e.g. 'NL').
  name: countryCode
  type: string
- description: The [International Bank Account Number](https://en.wikipedia.org/wiki/International_Bank_Account_Number) (IBAN).
  name: iban
  type: string
- description: The name of the bank account holder. If you submit a name with non-Latin characters, we automatically replace some of them with corresponding Latin characters to meet the FATF recommendations. For exa
  name: ownerName
  type: string
- description: The bank account holder's tax ID.
  name: taxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-bank-account-schema.json
slug: payouts-bank-account
tags:
- Payments
- Financial Services
- Fintech
title: BankAccount
---
