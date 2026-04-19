---
description: TransactionRulesResult schema from Adyen API
layout: schema
name: TransactionRulesResult
properties_list:
- description: Indicates whether the transaction passed the evaluation for all transaction rules.
  name: allRulesPassed
  type: boolean
- description: Array containing all the transaction rules that the transaction violated. This list is only sent when `allRulesPassed` is **false**.
  name: failedTransactionRules
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-transaction-rules-result-schema.json
slug: notification-webhooks-transaction-rules-result
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRulesResult
---
