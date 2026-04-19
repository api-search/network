---
consumed_apis:
- id-verification
- id-trust-providers
- id-identity-providers
- authentication-consent
- authentication-facilitator
- identity-insights-accounts
- identity-insights-transactions
description: Unified workflow for identity managers and compliance teams to verify identities, manage authentication consent, and leverage identity intelligence for fraud prevention across Mastercard's identity services.
layout: capability
name: Mastercard Identity and Authentication
operations:
- description: Verify a consumer identity
  method: POST
  name: verify-identity
  path: /v1/verifications
- description: Create authentication consent
  method: POST
  name: create-consent
  path: /v1/consents
- description: Get identity insights for an account
  method: POST
  name: get-account-insights
  path: /v1/account-insights
- description: Get identity insights for a transaction
  method: POST
  name: get-transaction-insights
  path: /v1/transaction-insights
personas: []
provider_name: Mastercard
provider_slug: mastercard
search_terms:
- verify a consumer identity using mastercard id
- get transaction identity insights
- fraud detection
- verify a consumer identity
- create auth consent
- identity insights for transactions
- authentication
- verify identity
- submit trust verification
- financial services
- get identity insights for a transaction
- payments
- authentication consent management
- initiate strong customer authentication
- get authentication consent status
- get account insights
- create consent
- create authentication consent
- get identity intelligence insights for an account
- identity
- get consent status
- submit identity verification as a trust provider
- mastercard
- get identity intelligence insights for a transaction
- kyc
- verification
- credit cards
- identity verification
- open banking
- identity insights for accounts
- get identity insights for an account
- initiate authentication
- get transaction insights
- get account identity insights
- digital identity
- create an authentication consent request
slug: identity-and-authentication
tags:
- Mastercard
- Identity
- Authentication
- Verification
- KYC
tools:
- description: Verify a consumer identity using Mastercard ID
  hints:
    readOnly: true
  name: verify-identity
- description: Create an authentication consent request
  hints:
    readOnly: false
  name: create-auth-consent
- description: Get authentication consent status
  hints:
    readOnly: true
  name: get-consent-status
- description: Initiate strong customer authentication
  hints:
    readOnly: false
  name: initiate-authentication
- description: Get identity intelligence insights for an account
  hints:
    readOnly: true
  name: get-account-identity-insights
- description: Get identity intelligence insights for a transaction
  hints:
    readOnly: true
  name: get-transaction-identity-insights
- description: Submit identity verification as a trust provider
  hints:
    readOnly: false
  name: submit-trust-verification
---
