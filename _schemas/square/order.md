---
description: Contains all information related to a single order to process with Square, including line items that specify the products to purchase. Order objects also include information about any associated tenders, refunds, and returns.
layout: schema
name: Square Order
properties_list:
- description: The order's unique ID.
  name: id
  type: string
- description: The ID of the seller location that this order is associated with.
  name: location_id
  type: string
- description: A client-specified ID to associate an entity in another system with this order.
  name: reference_id
  type: string
- description: The origination details of the order.
  name: source
  type: object
- description: The ID of the customer associated with the order.
  name: customer_id
  type: string
- description: The line items included in the order.
  name: line_items
  type: array
- description: The list of all taxes associated with the order.
  name: taxes
  type: array
- description: The list of all discounts associated with the order.
  name: discounts
  type: array
- description: A list of service charges applied to the order.
  name: service_charges
  type: array
- description: Details about order fulfillment.
  name: fulfillments
  type: array
- description: A collection of items from sale orders being returned in this one.
  name: returns
  type: array
- description: The rollup of the returned money amounts.
  name: return_amounts
  type: object
- description: The net money amounts (sale money - return money).
  name: net_amounts
  type: object
- description: A positive rounding adjustment to the total of the order.
  name: rounding_adjustment
  type: object
- description: The tenders that were used to pay for the order.
  name: tenders
  type: array
- description: The refunds that are part of this order.
  name: refunds
  type: array
- description: Application-defined data attached to this order. Metadata fields are intended to store descriptive references or associations with an entity in another system.
  name: metadata
  type: object
- description: The timestamp for when the order was created, in RFC 3339 format.
  name: created_at
  type: string
- description: The timestamp for when the order was last updated, in RFC 3339 format.
  name: updated_at
  type: string
- description: The timestamp for when the order reached a terminal state, in RFC 3339 format.
  name: closed_at
  type: string
- description: The current state of the order.
  name: state
  type: string
- description: The version number, incremented each time an update is committed to the order.
  name: version
  type: integer
- description: The total amount of money to collect for the order.
  name: total_money
  type: object
- description: The total amount of tax money to collect for the order.
  name: total_tax_money
  type: object
- description: The total amount of discount money to collect for the order.
  name: total_discount_money
  type: object
- description: The total amount of tip money to collect for the order.
  name: total_tip_money
  type: object
- description: The total amount of service charge money to collect for the order.
  name: total_service_charge_money
  type: object
- description: A short-term identifier for the order used on receipts, the Seller Dashboard, and the Point of Sale device.
  name: ticket_name
  type: string
- description: Pricing options for an order.
  name: pricing_options
  type: object
provider_name: Square
provider_slug: square
schema_file: json-schema/order.json
slug: order
tags:
- Bookings
- Catalog
- Checkout
- Customers
- Disputes
- Ecommerce
- Financial Technology
- Gift Cards
- Inventory
- Invoicing
- Labor
- Locations
- Loyalty
- Merchants
- Orders
- Payments
- Point of Sale
- Refunds
- Retail
- Subscriptions
- Team
- Terminal
- Webhooks
title: Square Order
---
