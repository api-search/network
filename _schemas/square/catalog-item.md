---
description: A CatalogObject instance of the ITEM type, also referred to as an item, in the catalog. Represents a product or service that a seller offers for sale.
layout: schema
name: Square Catalog Item
properties_list:
- description: The item's name. This is a searchable attribute for use in applicable query filters.
  name: name
  type: string
- description: The item's description as plain text.
  name: description
  type: string
- description: The item's description as expressed in valid HTML elements.
  name: description_html
  type: string
- description: The text of the item's display label in the Square Point of Sale app. Only up to the first five characters of the string are used.
  name: abbreviation
  type: string
- description: The color of the item's display label in the Square Point of Sale app. This must be a valid hex color code.
  name: label_color
  type: string
- description: Indicates whether the item is taxable (true) or non-taxable (false). Default is true.
  name: is_taxable
  type: boolean
- description: 'The ID of the item''s category, if any. Deprecated: use categories instead.'
  name: category_id
  type: string
- description: The list of categories that this item belongs to.
  name: categories
  type: array
- description: A set of IDs indicating the taxes enabled for this item.
  name: tax_ids
  type: array
- description: A set of CatalogItemModifierListInfo objects representing the modifier lists that apply to this item.
  name: modifier_list_info
  type: array
- description: A list of CatalogItemVariation objects for this item. An item must have at least one variation.
  name: variations
  type: array
- description: The product type of the item. Once set, the product_type value cannot be modified.
  name: product_type
  type: string
- description: If false, the Square Point of Sale app will present the CatalogItem's details screen immediately, allowing the merchant to choose CatalogModifiers before adding the item to the cart.
  name: skip_modifier_screen
  type: boolean
- description: 'List of item options IDs for this item. Used to manage and group item variations in a specified order. Maximum: 6 item options.'
  name: item_options
  type: array
- description: The IDs of images associated with this CatalogItem instance.
  name: image_ids
  type: array
- description: A name to sort the item by. If unspecified, the regular name field is used for sorting.
  name: sort_name
  type: string
- description: The reporting category associated with this item.
  name: reporting_category
  type: object
- description: The channels where this item is available.
  name: channels
  type: array
- description: Whether this item is archived (soft-deleted).
  name: is_archived
  type: boolean
provider_name: Square
provider_slug: square
schema_file: json-schema/catalog-item.json
slug: catalog-item
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
title: Square Catalog Item
---
