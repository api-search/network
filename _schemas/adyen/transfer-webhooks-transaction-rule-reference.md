---
description: TransactionRuleReference schema from Adyen API
layout: schema
name: TransactionRuleReference
properties_list:
- description: The description of the resource.
  name: description
  type: string
- description: The unique identifier of the resource.
  name: id
  type: string
- description: The outcome type of the rule.
  name: outcomeType
  type: string
- description: The reference for the resource.
  name: reference
  type: string
- description: The score of the rule in case it's a scoreBased rule.
  name: score
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-transaction-rule-reference-schema.json
slug: transfer-webhooks-transaction-rule-reference
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRuleReference
---
