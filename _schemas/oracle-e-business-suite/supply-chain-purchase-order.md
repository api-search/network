---
description: ''
layout: schema
name: PurchaseOrder
properties_list:
- description: Purchase order header identifier
  name: poHeaderId
  type: integer
- description: Purchase order number
  name: segment1
  type: string
- description: Purchase order type
  name: typeLookupCode
  type: string
- description: Supplier/vendor identifier
  name: vendorId
  type: integer
- description: Supplier/vendor name
  name: vendorName
  type: string
- description: Vendor site identifier
  name: vendorSiteId
  type: integer
- description: Currency code (ISO 4217)
  name: currencyCode
  type: string
- description: Authorization status
  name: authorizationStatus
  type: string
- description: Approved flag
  name: approvedFlag
  type: string
- description: Close status
  name: closedCode
  type: string
- description: Total purchase order amount
  name: totalAmount
  type: number
- description: Creation date
  name: creationDate
  type: string
- description: Approval date
  name: approvedDate
  type: string
- description: Buyer employee identifier
  name: buyerId
  type: integer
- description: Ship-to location identifier
  name: shipToLocationId
  type: integer
- description: Bill-to location identifier
  name: billToLocationId
  type: integer
- description: Payment terms identifier
  name: termsId
  type: integer
- description: Purchase order description
  name: description
  type: string
- description: ''
  name: lines
  type: array
- description: Operating unit identifier
  name: orgId
  type: integer
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-purchase-order-schema.json
slug: supply-chain-purchase-order
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: PurchaseOrder
---
