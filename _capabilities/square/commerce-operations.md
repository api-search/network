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
- refund a payment.
- subscriptions
- point of sale
- locations
- accept a dispute.
- refunds
- team
- list payment disputes.
- get catalog object
- list disputes.
- search orders
- list payments.
- create an order.
- inventory
- create a subscription.
- get details for a specific payment.
- list catalog objects.
- cancel a payment.
- retrieve inventory counts.
- list refunds.
- get invoice
- create invoice
- bookings
- create subscription
- loyalty
- list invoices.
- search subscriptions.
- ecommerce
- financial technology
- search all orders.
- upsert catalog object
- get order
- manage invoices.
- payments
- manage orders.
- list invoices for a location.
- get dispute
- merchants
- manage disputes.
- complete payment
- manage payments.
- manage a specific order.
- list payments
- cancel payment
- batch retrieve inventory counts
- get dispute details.
- square
- orders
- search catalog objects
- labor
- invoicing
- list invoices
- create payment
- manage payment links.
- retail
- manage a specific payment.
- create a payment.
- search subscriptions
- create payment link
- create a draft invoice.
- create order
- create a checkout payment link.
- create a payment link.
- get payment
- catalog
- list catalog
- create refund
- disputes
- gift cards
- manage refunds.
- refund payment
- create or update a catalog object.
- list payment links
- terminal
- get order details.
- get a single catalog object.
- apply inventory adjustments.
- get an invoice.
- retrieve an order by id.
- batch change inventory
- create a new order.
- list payment refunds.
- manage subscriptions.
- list disputes
- customers
- list refunds
- complete a payment.
- list payments taken by the account.
- manage catalog items.
- commerce
- accept dispute
- search catalog objects.
- get payment details.
- checkout
- webhooks
- list payment links.
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
