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
- get billing updates
- look up bin information for a card
- create fulfillment order
- manage a payment account lifecycle
- validate account details
- credit cards
- bin lookup
- issuers
- payments
- submit pan event
- validate account
- list available mastercard bins
- financial services
- automatic billing updates
- retrieve account catalog data
- submit pan-related event for account level management
- issue a new card
- fraud detection
- open banking
- card issuance and management
- request updated card credentials
- query payment account reference to link tokens to accounts
- account management
- create a physical card fulfillment order
- issue card
- issue a new mastercard card
- payment account management
- look up bin information
- mastercard
- manage payment account
- get payment account reference
- manage a payment account
- manage account
- get account catalog
- request updated card credentials for card-on-file
- list bins
- card management
- get card details
- lookup bin
- digital identity
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
