---
description: Request body for creating a new purchase order
layout: schema
name: PurchaseOrderCreate
properties_list:
- description: ERP system purchase order number
  name: erpPONumber
  type: string
- description: ISO 4217 currency code
  name: currency
  type: string
- description: Purchasing organization identifier
  name: purchaseOrg
  type: string
- description: Purchasing group identifier
  name: purchaseGroup
  type: string
- description: Company code
  name: companyCode
  type: string
- description: ''
  name: lineItems
  type: array
- description: Reference to originating requisition
  name: requisitionId
  type: string
- description: Reference to master agreement
  name: contractId
  type: string
- description: Header-level comments
  name: comments
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-purchase-order-create-schema.json
slug: sap-ariba-procurement-purchase-order-create
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: PurchaseOrderCreate
---
