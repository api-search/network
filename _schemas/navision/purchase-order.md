---
description: Represents a purchase order entity in Dynamics 365 Business Central. Purchase orders are documents used to record the purchase of goods or services from vendors. They include header information (vendor, dates, payment terms) and line items specifying the products or services being purchased.
layout: schema
name: Purchase Order
properties_list:
- description: ETag for optimistic concurrency control
  name: '@odata.etag'
  type: string
- description: The unique identifier (GUID) of the purchase order
  name: id
  type: string
- description: The purchase order number assigned from a number series
  name: number
  type: string
- description: The date when the purchase order was created
  name: orderDate
  type: string
- description: The date used for posting the purchase order to the general ledger
  name: postingDate
  type: string
- description: The unique identifier of the buy-from vendor
  name: vendorId
  type: string
- description: The vendor number of the buy-from vendor
  name: vendorNumber
  type: string
- description: The name of the buy-from vendor
  name: vendorName
  type: string
- description: The name of the pay-to party
  name: payToName
  type: string
- description: The unique identifier of the pay-to vendor
  name: payToVendorId
  type: string
- description: The vendor number of the pay-to vendor
  name: payToVendorNumber
  type: string
- description: The name for the ship-to (receiving) address
  name: shipToName
  type: string
- description: The contact person at the ship-to address
  name: shipToContact
  type: string
- description: First line of the buy-from vendor address
  name: buyFromAddressLine1
  type: string
- description: Second line of the buy-from vendor address
  name: buyFromAddressLine2
  type: string
- description: The city of the buy-from vendor address
  name: buyFromCity
  type: string
- description: The country/region code of the buy-from vendor address
  name: buyFromCountry
  type: string
- description: The state or province code of the buy-from vendor address
  name: buyFromState
  type: string
- description: The postal code of the buy-from vendor address
  name: buyFromPostCode
  type: string
- description: The unique identifier of the currency
  name: currencyId
  type: string
- description: The currency code (e.g., USD, EUR) for the purchase order
  name: currencyCode
  type: string
- description: Indicates whether the prices on the order include tax
  name: pricesIncludeTax
  type: boolean
- description: The unique identifier of the payment terms
  name: paymentTermsId
  type: string
- description: The unique identifier of the shipment method
  name: shipmentMethodId
  type: string
- description: The purchaser/buyer code assigned to the order
  name: purchaser
  type: string
- description: The date the goods are requested to be received
  name: requestedReceiptDate
  type: string
- description: The total invoice discount amount applied to the order
  name: discountAmount
  type: number
- description: Indicates whether discounts are applied before tax calculation
  name: discountAppliedBeforeTax
  type: boolean
- description: The total amount of the order excluding tax (read-only)
  name: totalAmountExcludingTax
  type: number
- description: The total tax amount on the order (read-only)
  name: totalTaxAmount
  type: number
- description: The total amount of the order including tax (read-only)
  name: totalAmountIncludingTax
  type: number
- description: Indicates whether all lines on the order have been fully received (read-only)
  name: fullyReceived
  type: boolean
- description: The current status of the purchase order (read-only)
  name: status
  type: string
- description: The date and time the purchase order was last modified (read-only)
  name: lastModifiedDateTime
  type: string
- description: The line items on the purchase order
  name: purchaseOrderLines
  type: array
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/purchase-order.json
slug: purchase-order
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: Purchase Order
---
