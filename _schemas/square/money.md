---
description: Represents an amount of money. Money fields can be signed or unsigned. The amount is specified in the smallest denomination of the applicable currency (for example, US dollar amounts are specified in cents).
layout: schema
name: Square Money
properties_list:
- description: The amount of money, in the smallest denomination of the currency indicated by currency. For example, when currency is USD, amount is in cents.
  name: amount
  type: integer
- description: The type of currency, in ISO 4217 format. For example, the currency code for US dollars is USD.
  name: currency
  type: string
provider_name: Square
provider_slug: square
schema_file: json-schema/money.json
slug: money
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
title: Square Money
---
