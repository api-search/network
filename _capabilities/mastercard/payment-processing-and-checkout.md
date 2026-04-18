---
consumed_apis:
- checkout-solutions
- unified-checkout
- cloud-commerce
- contactless-reader
- gateway
- merchant-qr
- installments
description: Unified workflow for merchants and payment processors to manage checkout experiences, process payments, and accept contactless transactions across Mastercard's payment gateway, checkout solutions, and commerce APIs.
layout: capability
name: Mastercard Payment Processing and Checkout
operations:
- description: Create a new checkout session
  method: POST
  name: create-checkout-session
  path: /v1/checkout-sessions
- description: Create a unified checkout session
  method: POST
  name: create-unified-session
  path: /v1/unified-sessions
- description: Process a payment through the gateway
  method: POST
  name: process-payment
  path: /v1/payments
- description: Get payment details
  method: GET
  name: get-payment
  path: /v1/payments
- description: Generate a merchant QR code for payment
  method: POST
  name: generate-qr-code
  path: /v1/qr-payments
- description: Create an installment plan
  method: POST
  name: create-installment-plan
  path: /v1/installment-plans
personas: []
provider_name: Mastercard
provider_slug: mastercard
search_terms:
- process a payment through the gateway
- process a payment through the mastercard gateway
- qr code payment acceptance
- create unified session
- unified checkout sessions
- create checkout session
- create an installment plan
- create installment plan
- register contactless reader
- create a unified checkout session supporting multiple payment methods
- generate qr code
- retrieve payment transaction details
- process a cloud commerce transaction
- register a contactless reader device
- merchant
- buy-now-pay-later installment plans
- process payment
- generate a merchant qr code for payment
- fraud detection
- open banking
- mastercard
- checkout session management
- digital identity
- checkout
- get payment
- get payment details
- generate a merchant-presented qr code for payment
- create a new checkout session for a merchant
- process cloud transaction
- create a new checkout session
- payment processing
- payments
- financial services
- credit cards
- create a unified checkout session
- create a buy-now-pay-later installment plan
- e-commerce
slug: payment-processing-and-checkout
tags:
- Mastercard
- Payment Processing
- Checkout
- E-Commerce
- Merchant
tools:
- description: Create a new checkout session for a merchant
  hints:
    idempotent: false
    readOnly: false
  name: create-checkout-session
- description: Create a unified checkout session supporting multiple payment methods
  hints:
    idempotent: false
    readOnly: false
  name: create-unified-session
- description: Process a payment through the Mastercard gateway
  hints:
    idempotent: false
    readOnly: false
  name: process-payment
- description: Retrieve payment transaction details
  hints:
    idempotent: true
    readOnly: true
  name: get-payment-details
- description: Generate a merchant-presented QR code for payment
  hints:
    idempotent: false
    readOnly: false
  name: generate-qr-code
- description: Process a cloud commerce transaction
  hints:
    idempotent: false
    readOnly: false
  name: process-cloud-transaction
- description: Register a contactless reader device
  hints:
    idempotent: false
    readOnly: false
  name: register-contactless-reader
- description: Create a buy-now-pay-later installment plan
  hints:
    idempotent: false
    readOnly: false
  name: create-installment-plan
---
