---
consumed_apis:
- square
description: Unified workflow for commerce operations combining payments, orders, catalog, inventory, checkout, invoicing, subscriptions, and refunds. Used by commerce developers and business operators to manage the full sales lifecycle.
layout: capability
name: Square Commerce Operations
operations:
- description: List payments.
  method: GET
  name: list-payments
  path: /v1/payments
- description: Create a payment.
  method: POST
  name: create-payment
  path: /v1/payments
- description: Get payment details.
  method: GET
  name: get-payment
  path: /v1/payments/{payment_id}
- description: List refunds.
  method: GET
  name: list-refunds
  path: /v1/refunds
- description: Refund a payment.
  method: POST
  name: create-refund
  path: /v1/refunds
- description: Create an order.
  method: POST
  name: create-order
  path: /v1/orders
- description: Get order details.
  method: GET
  name: get-order
  path: /v1/orders/{order_id}
- description: List catalog objects.
  method: GET
  name: list-catalog
  path: /v1/catalog
- description: List invoices.
  method: GET
  name: list-invoices
  path: /v1/invoices
- description: Create a subscription.
  method: POST
  name: create-subscription
  path: /v1/subscriptions
- description: List payment links.
  method: GET
  name: list-payment-links
  path: /v1/checkout
- description: Create a payment link.
  method: POST
  name: create-payment-link
  path: /v1/checkout
- description: List disputes.
  method: GET
  name: list-disputes
  path: /v1/disputes
personas: []
provider_name: Square
provider_slug: square
search_terms:
- ecommerce
- retail
- manage invoices.
- create subscription
- list invoices for a location.
- retrieve inventory counts.
- manage payment links.
- search catalog objects.
- refund payment
- customers
- financial technology
- search subscriptions.
- manage a specific order.
- search all orders.
- list refunds
- search orders
- get a single catalog object.
- upsert catalog object
- get dispute
- bookings
- manage a specific payment.
- merchants
- webhooks
- create a subscription.
- get payment
- create an order.
- create refund
- get an invoice.
- get order details.
- manage catalog items.
- manage refunds.
- create a new order.
- manage payments.
- locations
- orders
- list disputes.
- complete payment
- catalog
- accept dispute
- labor
- point of sale
- list disputes
- create a draft invoice.
- create a payment.
- checkout
- get payment details.
- list catalog objects.
- retrieve an order by id.
- list payments
- get invoice
- loyalty
- get order
- batch retrieve inventory counts
- create payment
- list payments taken by the account.
- search subscriptions
- accept a dispute.
- create order
- team
- payments
- manage orders.
- list payments.
- complete a payment.
- manage disputes.
- commerce
- manage subscriptions.
- get dispute details.
- get details for a specific payment.
- list payment refunds.
- list payment links.
- invoicing
- gift cards
- list invoices.
- create or update a catalog object.
- list refunds.
- inventory
- cancel a payment.
- list payment disputes.
- list catalog
- square
- create payment link
- create a checkout payment link.
- cancel payment
- refunds
- refund a payment.
- create invoice
- search catalog objects
- create a payment link.
- terminal
- subscriptions
- get catalog object
- apply inventory adjustments.
- disputes
- list invoices
- list payment links
- batch change inventory
slug: commerce-operations
tags:
- Square
- Commerce
- Payments
- Orders
- Catalog
- Inventory
tools:
- description: List payments taken by the account.
  hints:
    openWorld: true
    readOnly: true
  name: list-payments
- description: Create a payment.
  hints:
    idempotent: false
    readOnly: false
  name: create-payment
- description: Get details for a specific payment.
  hints:
    openWorld: true
    readOnly: true
  name: get-payment
- description: Cancel a payment.
  hints:
    destructive: true
    readOnly: false
  name: cancel-payment
- description: Complete a payment.
  hints:
    idempotent: false
    readOnly: false
  name: complete-payment
- description: List payment refunds.
  hints:
    openWorld: true
    readOnly: true
  name: list-refunds
- description: Refund a payment.
  hints:
    idempotent: false
    readOnly: false
  name: refund-payment
- description: Create a new order.
  hints:
    idempotent: false
    readOnly: false
  name: create-order
- description: Search all orders.
  hints:
    openWorld: true
    readOnly: true
  name: search-orders
- description: Retrieve an order by ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-order
- description: List catalog objects.
  hints:
    openWorld: true
    readOnly: true
  name: list-catalog
- description: Create or update a catalog object.
  hints:
    idempotent: true
    readOnly: false
  name: upsert-catalog-object
- description: Get a single catalog object.
  hints:
    openWorld: true
    readOnly: true
  name: get-catalog-object
- description: Search catalog objects.
  hints:
    openWorld: true
    readOnly: true
  name: search-catalog-objects
- description: Retrieve inventory counts.
  hints:
    openWorld: true
    readOnly: true
  name: batch-retrieve-inventory-counts
- description: Apply inventory adjustments.
  hints:
    idempotent: false
    readOnly: false
  name: batch-change-inventory
- description: List invoices for a location.
  hints:
    openWorld: true
    readOnly: true
  name: list-invoices
- description: Create a draft invoice.
  hints:
    idempotent: false
    readOnly: false
  name: create-invoice
- description: Get an invoice.
  hints:
    openWorld: true
    readOnly: true
  name: get-invoice
- description: Create a subscription.
  hints:
    idempotent: false
    readOnly: false
  name: create-subscription
- description: Search subscriptions.
  hints:
    openWorld: true
    readOnly: true
  name: search-subscriptions
- description: List payment links.
  hints:
    openWorld: true
    readOnly: true
  name: list-payment-links
- description: Create a checkout payment link.
  hints:
    idempotent: false
    readOnly: false
  name: create-payment-link
- description: List payment disputes.
  hints:
    openWorld: true
    readOnly: true
  name: list-disputes
- description: Get dispute details.
  hints:
    openWorld: true
    readOnly: true
  name: get-dispute
- description: Accept a dispute.
  hints:
    idempotent: true
    readOnly: false
  name: accept-dispute
---
