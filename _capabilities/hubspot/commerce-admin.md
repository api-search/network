---
consumed_apis:
- commerce-payments
- commerce-subscriptions
- cms-hubdb
- cms-pages
- domains
description: Unified workflow for admins to manage commerce payments, subscriptions, HubDB data tables, CMS pages, and domains. Combines commerce operations with CMS data management for platform administration.
layout: capability
name: HubSpot Commerce Admin
operations:
- description: List payments
  method: GET
  name: list-payments
  path: /v1/payments
- description: Create payment
  method: POST
  name: create-payment
  path: /v1/payments
- description: Get payment
  method: GET
  name: get-payment
  path: /v1/payments/{commercePaymentId}
- description: List subscriptions
  method: GET
  name: list-subscriptions
  path: /v1/subscriptions
- description: Get subscription
  method: GET
  name: get-subscription
  path: /v1/subscriptions/{subscriptionId}
personas: []
provider_name: HubSpot
provider_slug: hubspot
search_terms:
- commerce subscriptions
- get subscription
- cms
- analytics
- hubdb
- update a commerce payment
- search commerce payments
- customer service
- create payment
- search commerce subscriptions
- marketing automation
- hubspot
- list all commerce subscriptions
- search subscriptions
- content
- create a commerce subscription
- commerce payments
- get a subscription by id
- crm
- sales
- update payment
- create a commerce payment
- individual subscription
- marketing
- get a payment by id
- admin
- list subscriptions
- email marketing
- commerce
- list all commerce payments
- individual payment
- operations
- list payments
- get payment
- create subscription
- search payments
slug: commerce-admin
tags:
- HubSpot
- Commerce
- Admin
- CMS
- HubDB
tools:
- description: List all commerce payments
  hints:
    idempotent: true
    readOnly: true
  name: list-payments
- description: Get a payment by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-payment
- description: Create a commerce payment
  hints:
    readOnly: false
  name: create-payment
- description: Update a commerce payment
  hints:
    idempotent: true
    readOnly: false
  name: update-payment
- description: Search commerce payments
  hints:
    idempotent: true
    readOnly: true
  name: search-payments
- description: List all commerce subscriptions
  hints:
    idempotent: true
    readOnly: true
  name: list-subscriptions
- description: Get a subscription by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-subscription
- description: Create a commerce subscription
  hints:
    readOnly: false
  name: create-subscription
- description: Search commerce subscriptions
  hints:
    idempotent: true
    readOnly: true
  name: search-subscriptions
---
