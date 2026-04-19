---
description: Request body for reporting a payment overdue
layout: schema
name: ReportOverdueRequest
properties_list:
- description: Trade credit insurance policy identifier
  name: policyId
  type: string
- description: Overdue category type code
  name: overdueCategoryTypeCode
  type: string
- description: Name of the debtor
  name: debtorName
  type: string
- description: Allianz Trade debtor identifier
  name: debtorId
  type: string
- description: Amount overdue
  name: overdueAmount
  type: number
- description: ISO 4217 currency code
  name: currency
  type: string
- description: Original invoice due date
  name: dueDate
  type: string
- description: Customer invoice reference
  name: invoiceReference
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-payment-overdues-report_overdue_request-schema.json
slug: trade-payment-overdues-report_overdue_request
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: ReportOverdueRequest
---
