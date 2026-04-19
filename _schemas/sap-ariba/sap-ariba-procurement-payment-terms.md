---
description: Payment terms governing when and how invoices should be paid
layout: schema
name: PaymentTerms
properties_list:
- description: Payment terms code
  name: code
  type: string
- description: Human-readable payment terms description
  name: description
  type: string
- description: Number of days until payment is due
  name: netDays
  type: integer
- description: Early payment discount percentage
  name: discountPercent
  type: number
- description: Number of days within which discount applies
  name: discountDays
  type: integer
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-payment-terms-schema.json
slug: sap-ariba-procurement-payment-terms
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: PaymentTerms
---
