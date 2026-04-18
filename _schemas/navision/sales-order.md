---
description: Represents a sales order entity in Dynamics 365 Business Central. Sales orders are documents used to record the sale of goods or services to customers. They include header information (customer, dates, payment terms) and line items specifying the products or services being sold.
layout: schema
name: Sales Order
properties_list:
- description: ETag for optimistic concurrency control
  name: '@odata.etag'
  type: string
- description: The unique identifier (GUID) of the sales order
  name: id
  type: string
- description: The sales order number assigned from a number series
  name: number
  type: string
- description: An external reference number (e.g., a customer PO number)
  name: externalDocumentNumber
  type: string
- description: The date when the sales order was created
  name: orderDate
  type: string
- description: The date used for posting the sales order to the general ledger
  name: postingDate
  type: string
- description: The unique identifier of the sell-to customer
  name: customerId
  type: string
- description: The customer number of the sell-to customer
  name: customerNumber
  type: string
- description: The name of the sell-to customer
  name: customerName
  type: string
- description: The name of the bill-to party
  name: billToName
  type: string
- description: The unique identifier of the bill-to customer
  name: billToCustomerId
  type: string
- description: The customer number of the bill-to customer
  name: billToCustomerNumber
  type: string
- description: The name for the ship-to address
  name: shipToName
  type: string
- description: The contact person at the ship-to address
  name: shipToContact
  type: string
- description: First line of the sell-to address
  name: sellToAddressLine1
  type: string
- description: Second line of the sell-to address
  name: sellToAddressLine2
  type: string
- description: The city of the sell-to address
  name: sellToCity
  type: string
- description: The country/region code of the sell-to address
  name: sellToCountry
  type: string
- description: The state or province code of the sell-to address
  name: sellToState
  type: string
- description: The postal code of the sell-to address
  name: sellToPostCode
  type: string
- description: The unique identifier of the currency
  name: currencyId
  type: string
- description: The currency code (e.g., USD, EUR) for the sales order
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
- description: The salesperson code assigned to the order
  name: salesperson
  type: string
- description: The date the customer has requested delivery
  name: requestedDeliveryDate
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
- description: Indicates whether all lines on the order have been fully shipped (read-only)
  name: fullyShipped
  type: boolean
- description: The current status of the sales order (read-only)
  name: status
  type: string
- description: The date and time the sales order was last modified (read-only)
  name: lastModifiedDateTime
  type: string
- description: The phone number associated with the order
  name: phoneNumber
  type: string
- description: The email address associated with the order
  name: email
  type: string
- description: The line items on the sales order
  name: salesOrderLines
  type: array
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/sales-order.json
slug: sales-order
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: Sales Order
---
