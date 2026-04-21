---
consumed_apis:
- amdocs-connectx
description: Unified workflow for telecom operators managing customer accounts, subscriptions, billing, and service catalog via Amdocs connectX BSS API. Supports BSS operators, customer care agents, and billing teams.
layout: capability
name: Amdocs Telco Customer Management
operations:
- description: List all customer accounts
  method: GET
  name: list-customers
  path: /v1/customers
- description: Onboard a new customer
  method: POST
  name: create-customer
  path: /v1/customers
- description: List subscriptions for a customer
  method: GET
  name: list-subscriptions
  path: /v1/subscriptions
- description: Add a service subscription
  method: POST
  name: create-subscription
  path: /v1/subscriptions
- description: List invoices for a customer
  method: GET
  name: list-invoices
  path: /v1/invoices
- description: Browse available products and plans
  method: GET
  name: list-products
  path: /v1/products
personas: []
provider_name: Amdocs
provider_slug: amdocs
search_terms:
- BSS Operator
- onboard a new customer
- Billing Team
- list service subscriptions for a customer
- list products
- Customer Care Agent
- list all customer accounts
- billing
- telecom customer account management
- list invoices
- add a service subscription
- list subscriptions
- onboard a new telecom customer
- customer subscription management
- list subscriptions for a customer
- amdocs
- mvno
- product and service catalog
- handles customer inquiries and account management
- oss
- manages invoicing, payments, and revenue assurance
- add a service subscription to a customer account
- customer billing invoices
- saas
- bss
- create customer
- telecom
- list customers
- retrieve billing invoices for a customer
- create subscription
- list telecom customer accounts
- unified bss workflow for customer onboarding, billing, and service management
- list invoices for a customer
- browse available products and plans
- manages telco bss operations and system configuration
- customer management
- browse the service catalog and available plans
- 5g
slug: telco-customer-management
tags:
- Amdocs
- Telecom
- BSS
- Customer Management
- Billing
tools:
- description: List telecom customer accounts
  hints:
    openWorld: true
    readOnly: true
  name: list-customers
- description: Onboard a new telecom customer
  hints:
    readOnly: false
  name: create-customer
- description: List service subscriptions for a customer
  hints:
    openWorld: true
    readOnly: true
  name: list-subscriptions
- description: Add a service subscription to a customer account
  hints:
    readOnly: false
  name: create-subscription
- description: Retrieve billing invoices for a customer
  hints:
    openWorld: true
    readOnly: true
  name: list-invoices
- description: Browse the service catalog and available plans
  hints:
    openWorld: true
    readOnly: true
  name: list-products
---
