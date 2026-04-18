---
description: A line item on an invoice
layout: schema
name: InvoiceLine
properties_list:
- description: The unique identifier for the line item
  name: Id
  type: string
- description: Line number within the transaction
  name: LineNum
  type: integer
- description: Free-form text description of the line item
  name: Description
  type: string
- description: The total amount for the line item
  name: Amount
  type: number
- description: Specifies the type of line detail
  name: DetailType
  type: string
- description: ''
  name: LinkedTxn
  type: array
provider_name: Intuit
provider_slug: intuit
schema_file: json-schema/quickbooks-accounting-invoice-line-schema.json
slug: quickbooks-accounting-invoice-line
tags:
- Accounting
- Custom Fields
- Financial
- Financial Services
- Invoicing
- Payments
- Payroll
- Project Management
- Sales Tax
- Small Business
- Tax
- Tax Preparation
- Taxes
- Time Tracking
title: InvoiceLine
---
