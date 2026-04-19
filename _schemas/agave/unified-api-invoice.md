---
description: An accounts payable invoice.
layout: schema
name: Invoice
properties_list:
- description: Invoice identifier.
  name: id
  type: string
- description: Associated project identifier.
  name: project_id
  type: string
- description: Vendor who issued the invoice.
  name: vendor_id
  type: string
- description: Vendor invoice number.
  name: invoice_number
  type: string
- description: Invoice total amount in USD.
  name: amount
  type: number
- description: Invoice processing status.
  name: status
  type: string
- description: Invoice date.
  name: invoice_date
  type: string
- description: Invoice due date.
  name: due_date
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-invoice-schema.json
slug: unified-api-invoice
tags:
- Accounting
- Construction
- Integration
title: Invoice
---
