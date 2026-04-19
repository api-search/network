---
description: It conveys Information related to the Reconciliation transaction processed by the POI System. Content of the Reconciliation Response message.
layout: schema
name: ReconciliationResponse
properties_list:
- description: ''
  name: Response
  type: object
- description: ''
  name: ReconciliationType
  type: object
- description: Absent if ReconciliationType is AcquirerReconciliation.
  name: POIReconciliationID
  type: integer
- description: ''
  name: TransactionTotals
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-reconciliation-response-schema.json
slug: terminal-reconciliation-response
tags:
- Payments
- Financial Services
- Fintech
title: ReconciliationResponse
---
