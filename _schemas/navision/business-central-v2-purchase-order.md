---
description: ''
layout: schema
name: PurchaseOrder
properties_list:
- description: ''
  name: '@odata.etag'
  type: string
- description: The unique identifier of the purchase order
  name: id
  type: string
- description: The purchase order number
  name: number
  type: string
- description: The order date
  name: orderDate
  type: string
- description: The posting date
  name: postingDate
  type: string
- description: The vendor ID
  name: vendorId
  type: string
- description: The vendor number
  name: vendorNumber
  type: string
- description: The vendor name
  name: vendorName
  type: string
- description: ''
  name: payToName
  type: string
- description: ''
  name: payToVendorId
  type: string
- description: ''
  name: payToVendorNumber
  type: string
- description: ''
  name: shipToName
  type: string
- description: ''
  name: shipToContact
  type: string
- description: ''
  name: buyFromAddressLine1
  type: string
- description: ''
  name: buyFromAddressLine2
  type: string
- description: ''
  name: buyFromCity
  type: string
- description: ''
  name: buyFromCountry
  type: string
- description: ''
  name: buyFromState
  type: string
- description: ''
  name: buyFromPostCode
  type: string
- description: ''
  name: currencyId
  type: string
- description: ''
  name: currencyCode
  type: string
- description: ''
  name: pricesIncludeTax
  type: boolean
- description: ''
  name: paymentTermsId
  type: string
- description: ''
  name: shipmentMethodId
  type: string
- description: ''
  name: purchaser
  type: string
- description: ''
  name: requestedReceiptDate
  type: string
- description: ''
  name: discountAmount
  type: number
- description: ''
  name: discountAppliedBeforeTax
  type: boolean
- description: ''
  name: totalAmountExcludingTax
  type: number
- description: ''
  name: totalTaxAmount
  type: number
- description: ''
  name: totalAmountIncludingTax
  type: number
- description: ''
  name: fullyReceived
  type: boolean
- description: ''
  name: status
  type: string
- description: ''
  name: lastModifiedDateTime
  type: string
- description: ''
  name: purchaseOrderLines
  type: array
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/business-central-v2-purchase-order-schema.json
slug: business-central-v2-purchase-order
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: PurchaseOrder
---
