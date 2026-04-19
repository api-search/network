---
description: TransactionRuleSource schema from Adyen API
layout: schema
name: TransactionRuleSource
properties_list:
- description: ID of the resource, when applicable.
  name: id
  type: string
- description: 'Indicates the type of resource for which the transaction rule is defined. Possible values: * **PaymentInstrumentGroup** * **PaymentInstrument** * **BalancePlatform** * **EntityUsageConfiguration** * *'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-transaction-rule-source-schema.json
slug: notification-webhooks-transaction-rule-source
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRuleSource
---
