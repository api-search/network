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
- buy now pay later
- backend developer integrating affirm bnpl into a merchant's e-commerce checkout.
- create an affirm bnpl checkout session for a customer purchase.
- void an authorized affirm transaction before capture.
- affirm
- authorize a transaction.
- refund a transaction.
- get dispute
- list all affirm payment disputes for a merchant.
- get promo messaging
- checkout session management.
- get promotional financing terms.
- merchant operations team member managing transaction reconciliation and dispute resolution.
- payment ops
- initiation and management of customer financing sessions.
- payment transaction management.
- get promo
- refund a captured affirm transaction partially or fully.
- list disputes
- void transaction
- refund transaction
- merchant engineer
- read an affirm checkout session by token.
- capture an authorized affirm transaction to collect funds.
- submit dispute evidence
- list all disputes.
- promotional messaging.
- create an affirm checkout session.
- list all transactions.
- capture an authorized transaction.
- payments
- specific dispute operations.
- disputes
- handling of customer chargebacks and disputes.
- read checkout
- capture a transaction.
- store checkout
- get dispute details.
- transactions
- get affirm promotional financing terms and messaging for a purchase amount.
- refund a captured transaction.
- list transactions
- authorize an affirm transaction using a checkout token.
- capture transaction
- displaying financing terms and promotional messaging to customers.
- submit evidence to contest an affirm payment dispute.
- full bnpl payment lifecycle from checkout through capture, refund, and dispute management.
- checkout
- dispute management.
- list all affirm payment transactions for reconciliation.
- read a checkout session.
- authorization, capture, void, and refund of payment transactions.
- get details of a specific affirm payment dispute.
- authorize transaction
- retrieve or update a checkout session.
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
