---
description: TransactionRulesResult schema from Adyen API
layout: schema
name: TransactionRulesResult
properties_list:
- description: The advice given by the Risk analysis.
  name: advice
  type: string
- description: Indicates whether the transaction passed the evaluation for all transaction rules.
  name: allRulesPassed
  type: boolean
- description: Array containing all the transaction rules that the transaction violated. This list is only sent when `allRulesPassed` is **false**.
  name: failedTransactionRules
  type: array
- description: The score of the Risk analysis.
  name: score
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-transaction-rules-result-schema.json
slug: accounting-notifications-transaction-rules-result
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRulesResult
---
