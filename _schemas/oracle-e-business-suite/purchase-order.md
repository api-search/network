---
description: Schema representing a purchase order in Oracle E-Business Suite Purchasing module. Maps to PO_HEADERS_ALL, PO_LINES_ALL, PO_LINE_LOCATIONS_ALL, and PO_DISTRIBUTIONS_ALL tables.
layout: schema
name: Oracle EBS Purchase Order
properties_list:
- description: Unique identifier for the purchase order header (PO_HEADERS_ALL.PO_HEADER_ID)
  name: poHeaderId
  type: integer
- description: Purchase order number (PO_HEADERS_ALL.SEGMENT1)
  name: segment1
  type: string
- description: Purchase order type
  name: typeLookupCode
  type: string
- description: Document revision number
  name: revisionNum
  type: integer
- description: Supplier/vendor identifier (AP_SUPPLIERS.VENDOR_ID)
  name: vendorId
  type: integer
- description: Supplier/vendor name
  name: vendorName
  type: string
- description: Vendor site identifier (AP_SUPPLIER_SITES_ALL.VENDOR_SITE_ID)
  name: vendorSiteId
  type: integer
- description: Vendor site code
  name: vendorSiteCode
  type: string
- description: Vendor contact identifier
  name: vendorContactId
  type: integer
- description: Document currency code (ISO 4217)
  name: currencyCode
  type: string
- description: Currency exchange rate type
  name: rateType
  type:
  - string
  - 'null'
- description: Currency exchange rate
  name: rate
  type:
  - number
  - 'null'
- description: Exchange rate date
  name: rateDate
  type:
  - string
  - 'null'
- description: Buyer/agent employee identifier
  name: agentId
  type: integer
- description: Authorization/approval status of the purchase order
  name: authorizationStatus
  type: string
- description: Whether the PO has been approved
  name: approvedFlag
  type: string
- description: Date the purchase order was approved
  name: approvedDate
  type:
  - string
  - 'null'
- description: Close status of the purchase order
  name: closedCode
  type: string
- description: Date the purchase order was closed
  name: closedDate
  type:
  - string
  - 'null'
- description: Default ship-to location identifier (HR_LOCATIONS_ALL.LOCATION_ID)
  name: shipToLocationId
  type: integer
- description: Default bill-to location identifier
  name: billToLocationId
  type: integer
- description: Payment terms identifier (AP_TERMS.TERM_ID)
  name: termsId
  type: integer
- description: Purchase order description
  name: description
  type:
  - string
  - 'null'
- description: Purchase order comments
  name: comments
  type:
  - string
  - 'null'
- description: Total purchase order amount
  name: totalAmount
  type: number
- description: ''
  name: confirmedFlag
  type: string
- description: Number of times the PO has been printed
  name: printCount
  type: integer
- description: Purchase order lines
  name: lines
  type: array
- description: Operating unit identifier (HR_OPERATING_UNITS.ORGANIZATION_ID)
  name: orgId
  type: integer
- description: User who created the record (FND_USER.USER_ID)
  name: createdBy
  type: integer
- description: Record creation date
  name: creationDate
  type: string
- description: User who last updated the record
  name: lastUpdatedBy
  type: integer
- description: Record last update date
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/purchase-order.json
slug: purchase-order
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Oracle EBS Purchase Order
---
