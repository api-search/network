---
description: Paginated list of purchase orders
layout: schema
name: PurchaseOrderListResponse
properties_list:
- description: Total number of matching records
  name: totalCount
  type: integer
- description: Number of records skipped
  name: skip
  type: integer
- description: Maximum records per page
  name: limit
  type: integer
- description: ''
  name: orders
  type: array
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-purchase-order-list-response-schema.json
slug: sap-ariba-procurement-purchase-order-list-response
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: PurchaseOrderListResponse
---
