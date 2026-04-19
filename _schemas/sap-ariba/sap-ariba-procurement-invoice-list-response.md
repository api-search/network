---
description: Paginated list of invoices
layout: schema
name: InvoiceListResponse
properties_list:
- description: Total number of matching invoices
  name: totalCount
  type: integer
- description: Number of records skipped
  name: skip
  type: integer
- description: Maximum records per page
  name: limit
  type: integer
- description: ''
  name: invoices
  type: array
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-invoice-list-response-schema.json
slug: sap-ariba-procurement-invoice-list-response
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: InvoiceListResponse
---
