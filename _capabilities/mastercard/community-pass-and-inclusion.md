---
consumed_apis:
- community-pass-identity
- community-pass-payments
description: Unified workflow for development organizations and financial inclusion teams to manage digital identities, process payments, and deliver services through the Community Pass ecosystem in underserved communities.
layout: capability
name: Mastercard Community Pass and Financial Inclusion
operations:
- description: Create a digital identity
  method: POST
  name: create-identity
  path: /v1/identities
- description: Process a Community Pass payment
  method: POST
  name: process-payment
  path: /v1/payments
personas: []
provider_name: Mastercard
provider_slug: mastercard
search_terms:
- verify a digital identity
- create a digital identity
- process community payment
- create identity
- verify digital identity
- process payment
- fraud detection
- community pass
- process a payment in the community pass ecosystem
- mastercard
- community pass payments
- open banking
- digital identity
- digital identity management
- process a community pass payment
- payments
- financial services
- create digital identity
- credit cards
- create a digital identity in the community pass ecosystem
- financial inclusion
slug: community-pass-and-inclusion
tags:
- Mastercard
- Community Pass
- Financial Inclusion
- Digital Identity
tools:
- description: Create a digital identity in the Community Pass ecosystem
  hints:
    readOnly: false
  name: create-digital-identity
- description: Verify a digital identity
  hints:
    readOnly: true
  name: verify-digital-identity
- description: Process a payment in the Community Pass ecosystem
  hints:
    readOnly: false
  name: process-community-payment
---
