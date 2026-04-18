---
description: Represents a Square customer profile in the Customer Directory of a Square seller. Customers can be associated with payments, orders, loyalty programs, gift cards, and bookings.
layout: schema
name: Square Customer
properties_list:
- description: A unique Square-assigned ID for the customer profile.
  name: id
  type: string
- description: The timestamp when the customer profile was created, in RFC 3339 format.
  name: created_at
  type: string
- description: The timestamp when the customer profile was last updated, in RFC 3339 format.
  name: updated_at
  type: string
- description: The given name (that is, the first name) associated with the customer profile.
  name: given_name
  type: string
- description: The family name (that is, the last name) associated with the customer profile.
  name: family_name
  type: string
- description: A nickname for the customer profile.
  name: nickname
  type: string
- description: A business name associated with the customer profile.
  name: company_name
  type: string
- description: The email address associated with the customer profile.
  name: email_address
  type: string
- description: The physical address associated with the customer profile.
  name: address
  type: object
- description: The phone number associated with the customer profile.
  name: phone_number
  type: string
- description: The birthday associated with the customer profile, in YYYY-MM-DD format. For example, 1998-09-21 represents September 21, 1998, and 0000-09-21 represents September 21 (without a birth year).
  name: birthday
  type: string
- description: An optional second ID used to associate the customer profile with an entity in another system.
  name: reference_id
  type: string
- description: A custom note associated with the customer profile.
  name: note
  type: string
- description: Represents general customer preferences.
  name: preferences
  type: object
- description: The method used to create the customer profile.
  name: creation_source
  type: string
- description: The IDs of customer groups the customer belongs to.
  name: group_ids
  type: array
- description: The IDs of customer segments the customer belongs to.
  name: segment_ids
  type: array
- description: The Square-assigned version number of the customer profile. The version number is incremented each time an update is committed to the customer profile.
  name: version
  type: integer
- description: The tax IDs associated with the customer profile. This field is available for customers of sellers in EU countries or the United Kingdom.
  name: tax_ids
  type: object
provider_name: Square
provider_slug: square
schema_file: json-schema/customer.json
slug: customer
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
title: Square Customer
---
