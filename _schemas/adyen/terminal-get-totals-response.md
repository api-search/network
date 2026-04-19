---
description: It conveys Information related to the Reconciliation transaction processed by the POI System. Content of the Reconciliation Response message.
layout: schema
name: GetTotalsResponse
properties_list:
- description: ''
  name: Response
  type: object
- description: Identification of the reconciliation period between Sale and POI.
  name: POIReconciliationID
  type: integer
- description: ''
  name: TransactionTotals
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-get-totals-response-schema.json
slug: terminal-get-totals-response
tags:
- Payments
- Financial Services
- Fintech
title: GetTotalsResponse
---
