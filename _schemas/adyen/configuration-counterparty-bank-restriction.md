---
description: CounterpartyBankRestriction schema from Adyen API
layout: schema
name: CounterpartyBankRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: List of counterparty Bank Institutions and the operation.
  name: value
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-counterparty-bank-restriction-schema.json
slug: configuration-counterparty-bank-restriction
tags:
- Payments
- Financial Services
- Fintech
title: CounterpartyBankRestriction
---
