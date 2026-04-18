---
description: ''
layout: schema
name: SalesOrder
properties_list:
- description: ''
  name: '@odata.etag'
  type: string
- description: The unique identifier of the sales order
  name: id
  type: string
- description: The sales order number
  name: number
  type: string
- description: The external document number
  name: externalDocumentNumber
  type: string
- description: The order date
  name: orderDate
  type: string
- description: The posting date
  name: postingDate
  type: string
- description: The customer ID
  name: customerId
  type: string
- description: The customer number
  name: customerNumber
  type: string
- description: The customer name
  name: customerName
  type: string
- description: The bill-to name
  name: billToName
  type: string
- description: The bill-to customer ID
  name: billToCustomerId
  type: string
- description: The bill-to customer number
  name: billToCustomerNumber
  type: string
- description: The ship-to name
  name: shipToName
  type: string
- description: The ship-to contact
  name: shipToContact
  type: string
- description: ''
  name: sellToAddressLine1
  type: string
- description: ''
  name: sellToAddressLine2
  type: string
- description: ''
  name: sellToCity
  type: string
- description: ''
  name: sellToCountry
  type: string
- description: ''
  name: sellToState
  type: string
- description: ''
  name: sellToPostCode
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
  name: salesperson
  type: string
- description: ''
  name: requestedDeliveryDate
  type: string
- description: The total discount amount
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
  name: fullyShipped
  type: boolean
- description: The order status
  name: status
  type: string
- description: ''
  name: lastModifiedDateTime
  type: string
- description: ''
  name: phoneNumber
  type: string
- description: ''
  name: email
  type: string
- description: ''
  name: salesOrderLines
  type: array
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/business-central-v2-sales-order-schema.json
slug: business-central-v2-sales-order
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: SalesOrder
---
