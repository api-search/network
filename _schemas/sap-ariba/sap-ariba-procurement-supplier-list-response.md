---
description: Paginated list of suppliers
layout: schema
name: SupplierListResponse
properties_list:
- description: Total number of matching suppliers
  name: totalCount
  type: integer
- description: Number of records skipped
  name: skip
  type: integer
- description: Maximum records per page
  name: limit
  type: integer
- description: ''
  name: suppliers
  type: array
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-supplier-list-response-schema.json
slug: sap-ariba-procurement-supplier-list-response
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: SupplierListResponse
---
