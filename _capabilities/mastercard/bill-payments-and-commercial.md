---
consumed_apis:
- bill-pay
- bill-payment-validator
- business-payment-controls
- in-control-commercial
- commercial-notifications
description: Unified workflow for treasury teams and accounts payable to manage bill payments, business payment controls, virtual cards, commercial event notifications, and installment plans.
layout: capability
name: Mastercard Bill Payments and Commercial
operations:
- description: Search for billers
  method: POST
  name: search-billers
  path: /v1/billers
- description: Validate a bill payment
  method: POST
  name: validate-payment
  path: /v1/payment-validations
- description: Create a spending control rule
  method: POST
  name: create-spending-control
  path: /v1/spending-controls
- description: Create a virtual card
  method: POST
  name: create-virtual-card
  path: /v1/virtual-cards
personas: []
provider_name: Mastercard
provider_slug: mastercard
search_terms:
- search for billers
- list spending controls
- credit cards
- business payments
- create a spending control rule
- validate payment
- search for billers in the rpps network
- bill payment validation
- virtual card management
- create a business spending control rule
- financial services
- create virtual card
- commercial
- retrieve commercial event notifications
- create a virtual card
- mastercard
- get biller details
- validate a bill payment before processing
- get commercial notifications
- payments
- digital identity
- open banking
- list business spending control rules
- fraud detection
- business spending controls
- search billers
- create a virtual card for commercial payments
- biller management
- create spending control
- bill payments
- validate bill payment
- validate a bill payment
- treasury
slug: bill-payments-and-commercial
tags:
- Mastercard
- Bill Payments
- Commercial
- Treasury
- Business Payments
tools:
- description: Search for billers in the RPPS network
  hints:
    readOnly: true
  name: search-billers
- description: Get biller details
  hints:
    readOnly: true
  name: get-biller-details
- description: Validate a bill payment before processing
  hints:
    readOnly: true
  name: validate-bill-payment
- description: Create a business spending control rule
  hints:
    readOnly: false
  name: create-spending-control
- description: List business spending control rules
  hints:
    readOnly: true
  name: list-spending-controls
- description: Create a virtual card for commercial payments
  hints:
    readOnly: false
  name: create-virtual-card
- description: Retrieve commercial event notifications
  hints:
    readOnly: true
  name: get-commercial-notifications
---
