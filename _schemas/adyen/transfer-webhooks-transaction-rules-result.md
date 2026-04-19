---
description: TransactionRulesResult schema from Adyen API
layout: schema
name: TransactionRulesResult
properties_list:
- description: The advice given by the Risk analysis.
  name: advice
  type: string
- description: Indicates whether the transaction passed the evaluation for all hardblock rules
  name: allHardBlockRulesPassed
  type: boolean
- description: The score of the Risk analysis.
  name: score
  type: integer
- description: Array containing all the transaction rules that the transaction triggered.
  name: triggeredTransactionRules
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-transaction-rules-result-schema.json
slug: transfer-webhooks-transaction-rules-result
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRulesResult
---
