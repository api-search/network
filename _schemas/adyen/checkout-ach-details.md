---
description: AchDetails schema from Adyen API
layout: schema
name: AchDetails
properties_list:
- description: The bank account number (without separators).
  name: bankAccountNumber
  type: string
- description: The bank account type (checking, savings...).
  name: bankAccountType
  type: string
- description: The bank routing number of the account. The field value is `nil` in most cases.
  name: bankLocationId
  type: string
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: Encrypted bank account number. The bank account number (without separators).
  name: encryptedBankAccountNumber
  type: string
- description: Encrypted location id. The bank routing number of the account. The field value is `nil` in most cases.
  name: encryptedBankLocationId
  type: string
- description: The name of the bank account holder. If you submit a name with non-Latin characters, we automatically replace some of them with corresponding Latin characters to meet the FATF recommendations. For exa
  name: ownerName
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**ach**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-ach-details-schema.json
slug: checkout-ach-details
tags:
- Payments
- Financial Services
- Fintech
title: AchDetails
---
