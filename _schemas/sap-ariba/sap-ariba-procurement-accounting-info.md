---
description: Accounting assignment information for cost allocation on purchase order line items
layout: schema
name: AccountingInfo
properties_list:
- description: Cost center identifier for expenditure allocation
  name: costCenter
  type: string
- description: General ledger account number
  name: generalLedger
  type: string
- description: Fixed asset number
  name: asset
  type: string
- description: Internal order number
  name: internalOrder
  type: string
- description: Work Breakdown Structure element
  name: wbsElement
  type: string
- description: Percentage of line item amount allocated to this accounting assignment
  name: percentage
  type: number
- description: SAP distribution indicator flag
  name: sapDistributionFlag
  type: string
- description: Account assignment category code for the line item expenditure
  name: accountCategory
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-accounting-info-schema.json
slug: sap-ariba-procurement-accounting-info
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: AccountingInfo
---
