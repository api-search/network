---
description: Represents one of a business's locations where transactions occur, inventory is managed, and team members work.
layout: schema
name: Square Location
properties_list:
- description: A short generated string of letters and numbers that uniquely identifies this location instance.
  name: id
  type: string
- description: The name of the location. This information appears in the Seller Dashboard as the nickname. A location name must be unique within a seller account.
  name: name
  type: string
- description: The physical address of the location.
  name: address
  type: object
- description: The IANA time zone identifier for the time zone of the location. For example, America/Los_Angeles.
  name: timezone
  type: string
- description: The Square features that are enabled for the location.
  name: capabilities
  type: array
- description: The status of the location.
  name: status
  type: string
- description: The time when the location was created, in RFC 3339 format.
  name: created_at
  type: string
- description: The ID of the merchant that owns the location.
  name: merchant_id
  type: string
- description: The country of the location, in the two-letter format of ISO 3166. For example, US or JP.
  name: country
  type: string
- description: The language associated with the location, in BCP 47 format.
  name: language_code
  type: string
- description: The currency used for all transactions at this location, in ISO 4217 format. For example, USD.
  name: currency
  type: string
- description: The phone number of the location. For example, +1 855-700-6000.
  name: phone_number
  type: string
- description: The name of the location's overall business. This name is present on receipts and other customer-facing branding.
  name: business_name
  type: string
- description: The type of the location.
  name: type
  type: string
- description: The website URL of the location.
  name: website_url
  type: string
- description: The hours of operation for the location.
  name: business_hours
  type: object
- description: The email address of the location.
  name: business_email
  type: string
- description: The description of the location. For example, Main Street location.
  name: description
  type: string
- description: The Twitter username of the location without the '@' symbol.
  name: twitter_username
  type: string
- description: The Instagram username of the location without the '@' symbol.
  name: instagram_username
  type: string
- description: The Facebook profile URL of the location.
  name: facebook_url
  type: string
- description: The physical coordinates (latitude and longitude) of the location.
  name: coordinates
  type: object
- description: The URL of the logo image for the location.
  name: logo_url
  type: string
- description: The URL of the Point of Sale background image for the location.
  name: pos_background_url
  type: string
- description: The merchant category code (MCC) of the location as standardized by ISO 18245.
  name: mcc
  type: string
- description: The URL of a full-format logo image for the location.
  name: full_format_logo_url
  type: string
- description: The tax IDs for this location.
  name: tax_ids
  type: object
provider_name: Square
provider_slug: square
schema_file: json-schema/location.json
slug: location
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
title: Square Location
---
