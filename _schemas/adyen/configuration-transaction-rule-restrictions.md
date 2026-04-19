---
description: TransactionRuleRestrictions schema from Adyen API
layout: schema
name: TransactionRuleRestrictions
properties_list:
- description: 'The total number of tokens that a card can have across different kinds of digital wallets on the user''s phones, watches, or other wearables. Supported operations: **equals**, **notEquals**, **greaterT'
  name: activeNetworkTokens
  type: object
- description: 'List of card brand variants and the operation. Supported operations: **anyMatch**, **noneMatch**.'
  name: brandVariants
  type: object
- description: 'List of counterparty Institutions and the operation. Supported operations: **anyMatch**, **noneMatch**.'
  name: counterpartyBank
  type: object
- description: 'List of countries and the operation. Supported operations: **anyMatch**, **noneMatch**.'
  name: countries
  type: object
- description: 'List of week days and the operation. Supported operations: **anyMatch**, **noneMatch**.'
  name: dayOfWeek
  type: object
- description: 'Compares the currency of the payment against the currency of the payment instrument, and specifies the operation. Supported operations: **equals**, **notEquals**.'
  name: differentCurrencies
  type: object
- description: 'List of point-of-sale entry modes and the operation.. Supported operations: **anyMatch**, **noneMatch**.'
  name: entryModes
  type: object
- description: 'Indicates whether transaction is an international transaction and specifies the operation. Supported operations: **equals**, **notEquals**.'
  name: internationalTransaction
  type: object
- description: 'The number of transactions and the operation. Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.'
  name: matchingTransactions
  type: object
- description: 'List of merchant category codes (MCCs) and the operation. Supported operations: **anyMatch**, **noneMatch**.'
  name: mccs
  type: object
- description: 'List of names that will be compared to the merchant name according to the matching type. Supported operations: **anyMatch**, **noneMatch**.'
  name: merchantNames
  type: object
- description: 'List of merchant ID and acquirer ID pairs, and the operation. Supported operations: **anyMatch**, **noneMatch**.'
  name: merchants
  type: object
- description: 'List of processing types and the operation. Supported operations: **anyMatch**, **noneMatch**.'
  name: processingTypes
  type: object
- description: 'Checks if a user has recently sent the same amount of funds in multiple transfers. To use this restriction, you must: - Set the rule `type` to **velocity**. - Specify a time `interval`. - Specify a nu'
  name: sameAmountRestriction
  type: object
- description: 'Checks if a user has recently made multiple transfers to the same counterparty. To use this restriction, you must: - Set the rule `type` to **velocity**. - Specify a time `interval`. - Specify a numbe'
  name: sameCounterpartyRestriction
  type: object
- description: 'A start and end time in a time-only ISO-8601 extended offset format. Supported operations: **equals**, **notEquals**.'
  name: timeOfDay
  type: object
- description: 'The total amount and the operation. Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.'
  name: totalAmount
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-transaction-rule-restrictions-schema.json
slug: configuration-transaction-rule-restrictions
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRuleRestrictions
---
