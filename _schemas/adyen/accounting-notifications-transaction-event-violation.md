---
description: TransactionEventViolation schema from Adyen API
layout: schema
name: TransactionEventViolation
properties_list:
- description: An explanation about why the transaction rule failed.
  name: reason
  type: string
- description: Contains information about the transaction rule.
  name: transactionRule
  type: object
- description: Contains the type and ID of the resource to which the transaction rule is linked.
  name: transactionRuleSource
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-transaction-event-violation-schema.json
slug: accounting-notifications-transaction-event-violation
tags:
- Payments
- Financial Services
- Fintech
title: TransactionEventViolation
---
