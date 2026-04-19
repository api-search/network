---
description: Request payload for creating an invoice.
layout: schema
name: InvoiceRequest
properties_list:
- description: Project to associate the invoice with.
  name: project_id
  type: string
- description: Vendor identifier.
  name: vendor_id
  type: string
- description: Vendor invoice number.
  name: invoice_number
  type: string
- description: Invoice amount in USD.
  name: amount
  type: number
- description: Invoice date.
  name: invoice_date
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-invoice-request-schema.json
slug: unified-api-invoice-request
tags:
- Accounting
- Construction
- Integration
title: InvoiceRequest
---
