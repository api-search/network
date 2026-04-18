---
description: Represents a subscription purchased by a customer. Subscriptions enable sellers to generate recurring revenue by offering scheduled fulfillment of products or services with configurable billing periods, pricing, and discounts.
layout: schema
name: Square Subscription
properties_list:
- description: The Square-assigned ID of the subscription.
  name: id
  type: string
- description: The ID of the location associated with the subscription.
  name: location_id
  type: string
- description: The ID of the subscribed-to subscription plan variation.
  name: plan_variation_id
  type: string
- description: The ID of the subscribing customer profile.
  name: customer_id
  type: string
- description: The YYYY-MM-DD-formatted date to start the subscription.
  name: start_date
  type: string
- description: The YYYY-MM-DD-formatted date to cancel the subscription, when the subscription status changes to CANCELED and the subscription billing stops.
  name: canceled_date
  type: string
- description: The YYYY-MM-DD-formatted date up to when the subscriber is invoiced for the subscription.
  name: charged_through_date
  type: string
- description: The current status of the subscription.
  name: status
  type: string
- description: 'The tax amount applied when billing the subscription. The percentage is expressed in decimal form, using a ''.'' as the decimal separator and without a ''%'' sign. For example, a value of 7.5 corresponds '
  name: tax_percentage
  type: string
- description: The IDs of the invoices created for the subscription, listed in order when the invoices were created (newest invoices appear first).
  name: invoice_ids
  type: array
- description: A custom price which overrides the cost of a subscription plan variation with STATIC pricing.
  name: price_override_money
  type: object
- description: The version of the object. When updating an object, the version supplied must match the version in the database.
  name: version
  type: integer
- description: The timestamp when the subscription was created, in RFC 3339 format.
  name: created_at
  type: string
- description: The ID of the subscriber's card used to charge for the subscription.
  name: card_id
  type: string
- description: 'Timezone that will be used in date calculations for the subscription. Defaults to the timezone of the location based on location_id. Format: the IANA Timezone Database identifier.'
  name: timezone
  type: string
- description: The origination details of the subscription.
  name: source
  type: object
- description: The list of scheduled actions on this subscription.
  name: actions
  type: array
- description: The day of the month on which the subscription will issue invoices and publish orders.
  name: monthly_billing_anchor_date
  type: integer
- description: The subscription phases that define the billing schedule.
  name: phases
  type: array
provider_name: Square
provider_slug: square
schema_file: json-schema/subscription.json
slug: subscription
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
title: Square Subscription
---
