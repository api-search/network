---
description: Instalment schema from Adyen API
layout: schema
name: Instalment
properties_list:
- description: ''
  name: InstalmentType
  type: object
- description: ''
  name: SequenceNumber
  type: integer
- description: ''
  name: PlanID
  type: string
- description: ''
  name: Period
  type: integer
- description: ''
  name: PeriodUnit
  type: object
- description: ''
  name: FirstPaymentDate
  type: string
- description: ''
  name: TotalNbOfPayments
  type: integer
- description: ''
  name: CumulativeAmount
  type: number
- description: ''
  name: FirstAmount
  type: number
- description: ''
  name: Charges
  type: number
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-instalment-schema.json
slug: terminal-instalment
tags:
- Payments
- Financial Services
- Fintech
title: Instalment
---
