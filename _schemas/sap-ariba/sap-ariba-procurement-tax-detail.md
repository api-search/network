---
description: Tax calculation details for an invoice or line item
layout: schema
name: TaxDetail
properties_list:
- description: Tax code identifier
  name: taxCode
  type: string
- description: Tax category (e.g., VAT, GST, Sales Tax)
  name: taxCategory
  type: string
- description: Tax rate as a percentage
  name: taxRate
  type: number
- description: Description of the tax
  name: description
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-tax-detail-schema.json
slug: sap-ariba-procurement-tax-detail
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: TaxDetail
---
