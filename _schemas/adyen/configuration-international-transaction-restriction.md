---
description: InternationalTransactionRestriction schema from Adyen API
layout: schema
name: InternationalTransactionRestriction
properties_list:
- description: Defines how the condition must be evaluated.
  name: operation
  type: string
- description: 'Boolean indicating whether transaction is an international transaction. Possible values: - **true**: The transaction is an international transaction. - **false**: The transaction is a domestic transac'
  name: value
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-international-transaction-restriction-schema.json
slug: configuration-international-transaction-restriction
tags:
- Payments
- Financial Services
- Fintech
title: InternationalTransactionRestriction
---
