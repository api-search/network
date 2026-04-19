---
description: It conveys Information related to the Reconciliation requested by the Sale System. Content of the Reconciliation Request message.
layout: schema
name: ReconciliationRequest
properties_list:
- description: ''
  name: ReconciliationType
  type: object
- description: ''
  name: AcquirerID
  type: array
- description: Absent if ReconciliationType is not PreviousReconciliation.
  name: POIReconciliationID
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-reconciliation-request-schema.json
slug: terminal-reconciliation-request
tags:
- Payments
- Financial Services
- Fintech
title: ReconciliationRequest
---
