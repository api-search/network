---
consumed_apis:
- configuration
description: 'Unified capability for building financial products on Adyen''s balance platform. Combines the Configuration API for account holder and card management with the Transfers API for fund movement. Used by marketplace and platform builders to onboard users, issue cards, and manage fund transfers. Primary persona: Platform Engineer or Marketplace Developer.'
layout: capability
name: Adyen Balance Platform
operations:
- description: Create an account holder.
  method: POST
  name: create-account-holder
  path: /v1/account-holders
- description: Get account holder details.
  method: GET
  name: get-account-holder
  path: /v1/account-holders
- description: Create a balance account.
  method: POST
  name: create-balance-account
  path: /v1/balance-accounts
- description: Get balance account details.
  method: GET
  name: get-balance-account
  path: /v1/balance-accounts
- description: Create a payment instrument (card).
  method: POST
  name: create-payment-instrument
  path: /v1/payment-instruments
personas: []
provider_name: Adyen
provider_slug: adyen
search_terms:
- create a balance account.
- balance platform
- issuing
- get balance account details.
- create a new account holder on the adyen balance platform.
- retrieve details of an account holder.
- transfers
- create account holder
- 'unified capability for building financial products on adyen''s balance platform. combines the configuration api for account holder and card management with the transfers api for fund movement. used by marketplace and platform builders to onboard users, issue cards, and manage fund transfers. primary persona: platform engineer or marketplace developer.'
- manage payment instruments including virtual and physical cards.
- issue a virtual or physical payment card for an account holder.
- create a balance account for an account holder.
- create an account holder.
- get balance and details of a balance account.
- manage account holders on the balance platform.
- financial services
- online and in-person payment acceptance.
- builds marketplace and fintech platforms using adyen balance platform.
- payments
- manages merchant accounts, terminals, and dispute responses.
- create a payment instrument (card).
- 'unified capability for accepting and managing online payments. combines the checkout api and payments api to provide merchants and developers with a complete payment acceptance workflow including session creation, payment authorisation, refunds, and cancellations. primary persona: developer or merchant platform engineer.'
- get balance account
- chargeback and dispute handling.
- manage balance accounts.
- create balance account
- create payment instrument
- marketplaces
- get account holder
- get account holder details.
- adyen
- builds payment integrations using adyen apis and sdks.
- fintech
- merchant account and balance platform configuration.
- marketplace and platform fund management.
- issue card
- 'unified capability for managing adyen merchant accounts, stores, payment terminals, and dispute resolution. combines management api and disputes api to give operations teams and platform administrators complete control over merchant configuration and chargeback handling. primary persona: merchant operations team or platform administrator.'
slug: balance-platform
tags:
- Adyen
- Balance Platform
- Marketplaces
- Issuing
- Transfers
- Fintech
tools:
- description: Create a new account holder on the Adyen balance platform.
  hints:
    destructive: false
    readOnly: false
  name: create-account-holder
- description: Retrieve details of an account holder.
  hints:
    destructive: false
    readOnly: true
  name: get-account-holder
- description: Create a balance account for an account holder.
  hints:
    destructive: false
    readOnly: false
  name: create-balance-account
- description: Get balance and details of a balance account.
  hints:
    destructive: false
    readOnly: true
  name: get-balance-account
- description: Issue a virtual or physical payment card for an account holder.
  hints:
    destructive: false
    readOnly: false
  name: issue-card
---
