---
description: PeopleSoft purchasing purchase order.
layout: schema
name: PurchaseOrder
properties_list:
- description: Business unit.
  name: BUSINESS_UNIT
  type: string
- description: Purchase order ID.
  name: PO_ID
  type: string
- description: Vendor ID.
  name: VENDOR_ID
  type: string
- description: PO date.
  name: PO_DT
  type: string
- description: PO status.
  name: PO_STATUS
  type: string
- description: Currency.
  name: CURRENCY_CD
  type: string
- description: Buyer ID.
  name: BUYER_ID
  type: string
- description: Ship-to location.
  name: SHIP_TO_LOCATION
  type: string
- description: PO lines.
  name: LINES
  type: array
provider_name: PeopleSoft
provider_slug: peoplesoft
schema_file: json-schema/peoplesoft-supply-chain-management-purchase-order-schema.json
slug: peoplesoft-supply-chain-management-purchase-order
tags:
- Campus Solutions
- CRM
- Enterprise Software
- ERP
- Financial Management
- HCM
- Supply Chain Management
title: PurchaseOrder
---
