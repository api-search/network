---
description: Paginated list of purchase order line items
layout: schema
name: LineItemListResponse
properties_list:
- description: Total number of line items
  name: totalCount
  type: integer
- description: Number of records skipped
  name: skip
  type: integer
- description: Maximum records per page
  name: limit
  type: integer
- description: ''
  name: lineItems
  type: array
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-line-item-list-response-schema.json
slug: sap-ariba-procurement-line-item-list-response
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: LineItemListResponse
---
