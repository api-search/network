---
description: A complete purchase order document representing a buyer's commitment to purchase goods or services from a supplier through the SAP Ariba Network
layout: schema
name: PurchaseOrder
properties_list:
- description: Unique purchase order identifier (UniqueName) including version
  name: orderId
  type: string
- description: ERP system purchase order number. Unique ID for every version of the purchase order in the backend ERP system.
  name: erpPONumber
  type: string
- description: Supplemental version number of the order. Incremented with each change request.
  name: versionNumber
  type: integer
- description: Date and time when the purchase order was created
  name: orderDate
  type: string
- description: Ordering method category indicating how the order was generated (e.g., manual, automatic, blanket release)
  name: orderMethodCategory
  type: string
- description: ISO 4217 currency code for the order
  name: currency
  type: string
- description: Purchasing organization identifier
  name: purchaseOrg
  type: string
- description: Purchasing group identifier
  name: purchaseGroup
  type: string
- description: Company code for the buying entity
  name: companyCode
  type: string
- description: Line items contained in the purchase order
  name: lineItems
  type: array
- description: Reference to the originating purchase requisition
  name: requisitionId
  type: string
- description: Reference to a master agreement or contract
  name: contractId
  type: string
- description: Header-level comments on the purchase order
  name: comments
  type: string
- description: Timestamp when the order was first created
  name: createdDate
  type: string
- description: Timestamp of the most recent modification
  name: lastModifiedDate
  type: string
- description: Timestamp when the order was closed
  name: closedDate
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-purchase-order-schema.json
slug: sap-ariba-procurement-purchase-order
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: PurchaseOrder
---
