---
consumed_apis:
- affirm-checkout
- affirm-transactions
- affirm-disputes
- affirm-promos
description: Unified workflow capability for managing the full Affirm BNPL payment lifecycle — from initiating checkout sessions through transaction authorization, capture, refund, and dispute resolution. Used by merchant engineers and payment operations teams.
layout: capability
name: Affirm Payment Management
operations:
- description: Create an Affirm checkout session.
  method: POST
  name: store-checkout
  path: /v1/checkouts
- description: Read a checkout session.
  method: GET
  name: read-checkout
  path: /v1/checkouts/{token}
- description: List all transactions.
  method: GET
  name: list-transactions
  path: /v1/transactions
- description: Authorize a transaction.
  method: POST
  name: authorize-transaction
  path: /v1/transactions
- description: Capture a transaction.
  method: POST
  name: capture-transaction
  path: /v1/transactions/{id}/capture
- description: Refund a transaction.
  method: POST
  name: refund-transaction
  path: /v1/transactions/{id}/refund
- description: List all disputes.
  method: GET
  name: list-disputes
  path: /v1/disputes
- description: Get dispute details.
  method: GET
  name: get-dispute
  path: /v1/disputes/{dispute_id}
- description: Get promotional financing terms.
  method: GET
  name: get-promo
  path: /v1/promos
personas:
- description: Backend developer integrating Affirm BNPL into a merchant's e-commerce checkout.
  id: merchant-engineer
  name: Merchant Engineer
- description: Merchant operations team member managing transaction reconciliation and dispute resolution.
  id: payment-ops
  name: Payment Operations
provider_name: affirm
provider_slug: affirm
search_terms:
- get dispute
- submit dispute evidence
- submit evidence to contest an affirm payment dispute.
- backend developer integrating affirm bnpl into a merchant's e-commerce checkout.
- authorization, capture, void, and refund of payment transactions.
- read checkout
- specific dispute operations.
- payment transaction management.
- void an authorized affirm transaction before capture.
- disputes
- transactions
- get promotional financing terms.
- get affirm promotional financing terms and messaging for a purchase amount.
- displaying financing terms and promotional messaging to customers.
- capture a transaction.
- dispute management.
- merchant engineer
- affirm
- capture an authorized affirm transaction to collect funds.
- authorize transaction
- list disputes
- read an affirm checkout session by token.
- payments
- promotional messaging.
- retrieve or update a checkout session.
- refund transaction
- refund a transaction.
- merchant operations team member managing transaction reconciliation and dispute resolution.
- void transaction
- get promo messaging
- payment ops
- authorize a transaction.
- checkout session management.
- list transactions
- capture transaction
- refund a captured transaction.
- list all disputes.
- list all affirm payment transactions for reconciliation.
- authorize an affirm transaction using a checkout token.
- refund a captured affirm transaction partially or fully.
- handling of customer chargebacks and disputes.
- get dispute details.
- get promo
- checkout
- read a checkout session.
- list all affirm payment disputes for a merchant.
- initiation and management of customer financing sessions.
- full bnpl payment lifecycle from checkout through capture, refund, and dispute management.
- list all transactions.
- get details of a specific affirm payment dispute.
- store checkout
- create an affirm checkout session.
- capture an authorized transaction.
- buy now pay later
- create an affirm bnpl checkout session for a customer purchase.
slug: payment-management
tags:
- Affirm
- Payments
- Buy Now Pay Later
- Checkout
- Transactions
- Disputes
tools:
- description: Create an Affirm BNPL checkout session for a customer purchase.
  hints:
    destructive: false
    readOnly: false
  name: store-checkout
- description: Read an Affirm checkout session by token.
  hints:
    destructive: false
    readOnly: true
  name: read-checkout
- description: List all Affirm payment transactions for reconciliation.
  hints:
    destructive: false
    readOnly: true
  name: list-transactions
- description: Authorize an Affirm transaction using a checkout token.
  hints:
    destructive: false
    readOnly: false
  name: authorize-transaction
- description: Capture an authorized Affirm transaction to collect funds.
  hints:
    destructive: false
    readOnly: false
  name: capture-transaction
- description: Refund a captured Affirm transaction partially or fully.
  hints:
    destructive: true
    readOnly: false
  name: refund-transaction
- description: Void an authorized Affirm transaction before capture.
  hints:
    destructive: true
    readOnly: false
  name: void-transaction
- description: List all Affirm payment disputes for a merchant.
  hints:
    destructive: false
    readOnly: true
  name: list-disputes
- description: Get details of a specific Affirm payment dispute.
  hints:
    destructive: false
    readOnly: true
  name: get-dispute
- description: Submit evidence to contest an Affirm payment dispute.
  hints:
    destructive: false
    readOnly: false
  name: submit-dispute-evidence
- description: Get Affirm promotional financing terms and messaging for a purchase amount.
  hints:
    destructive: false
    readOnly: true
  name: get-promo-messaging
---
