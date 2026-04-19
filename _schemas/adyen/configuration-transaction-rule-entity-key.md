---
description: TransactionRuleEntityKey schema from Adyen API
layout: schema
name: TransactionRuleEntityKey
properties_list:
- description: The unique identifier of the resource.
  name: entityReference
  type: string
- description: 'The type of resource. Possible values: **balancePlatform**, **paymentInstrumentGroup**, **accountHolder**, **balanceAccount**, or **paymentInstrument**.'
  name: entityType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-transaction-rule-entity-key-schema.json
slug: configuration-transaction-rule-entity-key
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRuleEntityKey
---
