---
description: A billing invoice from a core facility.
layout: schema
name: Invoice
properties_list:
- description: Unique identifier for the invoice.
  name: id
  type: integer
- description: Billing period (YYYY-MM format).
  name: period
  type: string
- description: Current invoice status.
  name: status
  type: string
- description: Total invoice amount.
  name: total_amount
  type: number
- description: Currency code (ISO 4217).
  name: currency
  type: string
- description: Timestamp when the invoice was issued.
  name: issued_at
  type: string
provider_name: agilent-technologies
provider_slug: agilent-technologies
schema_file: json-schema/ilab-operations-api-invoice-schema.json
slug: ilab-operations-api-invoice
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
title: Invoice
---
