---
consumed_apis:
- card-issuance
- traditional-fulfillment
- bin-lookup
- automatic-billing-updater
- payment-account-mgmt
- payment-account-ref
- account-catalog
- universal-spec
- account-validation
description: Unified workflow for issuers and card managers to handle card issuance, fulfillment, BIN lookups, billing updates, payment account management, and account catalog services.
layout: capability
name: Mastercard Card and Account Management
operations:
- description: Issue a new card
  method: POST
  name: issue-card
  path: /v1/cards
- description: Look up BIN information
  method: POST
  name: lookup-bin
  path: /v1/bins
- description: Request updated card credentials
  method: POST
  name: get-billing-updates
  path: /v1/billing-updates
- description: Manage a payment account
  method: POST
  name: manage-account
  path: /v1/accounts
personas: []
provider_name: Mastercard
provider_slug: mastercard
search_terms:
- look up bin information for a card
- submit pan event
- mastercard
- card issuance and management
- request updated card credentials for card-on-file
- create a physical card fulfillment order
- list available mastercard bins
- manage a payment account
- manage account
- digital identity
- issue a new card
- retrieve account catalog data
- request updated card credentials
- list bins
- submit pan-related event for account level management
- get card details
- validate account details
- payments
- automatic billing updates
- query payment account reference to link tokens to accounts
- validate account
- credit cards
- create fulfillment order
- fraud detection
- account management
- card management
- get payment account reference
- manage payment account
- issue a new mastercard card
- manage a payment account lifecycle
- open banking
- get account catalog
- payment account management
- lookup bin
- financial services
- get billing updates
- issue card
- issuers
- look up bin information
- bin lookup
slug: card-and-account-management
tags:
- Mastercard
- Card Management
- Account Management
- Issuers
tools:
- description: Issue a new Mastercard card
  hints:
    readOnly: false
  name: issue-card
- description: Get card details
  hints:
    readOnly: true
  name: get-card-details
- description: Create a physical card fulfillment order
  hints:
    readOnly: false
  name: create-fulfillment-order
- description: Look up BIN information for a card
  hints:
    readOnly: true
  name: lookup-bin
- description: List available Mastercard BINs
  hints:
    idempotent: true
    readOnly: true
  name: list-bins
- description: Request updated card credentials for card-on-file
  hints:
    readOnly: true
  name: get-billing-updates
- description: Manage a payment account lifecycle
  hints:
    readOnly: false
  name: manage-payment-account
- description: Query payment account reference to link tokens to accounts
  hints:
    readOnly: true
  name: get-payment-account-reference
- description: Validate account details
  hints:
    readOnly: true
  name: validate-account
- description: Retrieve account catalog data
  hints:
    idempotent: true
    readOnly: true
  name: get-account-catalog
- description: Submit PAN-related event for account level management
  hints:
    readOnly: false
  name: submit-pan-event
---
