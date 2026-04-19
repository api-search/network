---
consumed_apis:
- core-banking
description: Unified digital banking capability combining account management, customer operations, payment processing, deposits, loans, and reference data for retail and corporate banking applications. Used by digital banking developers and fintech integration teams.
layout: capability
name: Temenos Digital Banking
operations:
- description: List customer accounts
  method: GET
  name: list-accounts
  path: /v1/accounts
- description: Get account details
  method: GET
  name: get-account
  path: /v1/accounts/{accountId}
- description: Get account balances
  method: GET
  name: get-account-balances
  path: /v1/accounts/{accountId}/balances
- description: Get transaction history
  method: GET
  name: get-account-transactions
  path: /v1/accounts/{accountId}/transactions
- description: List customers
  method: GET
  name: list-customers
  path: /v1/customers
- description: Create a customer
  method: POST
  name: create-customer
  path: /v1/customers
- description: List payment orders
  method: GET
  name: list-payment-orders
  path: /v1/payments
- description: Create a payment order
  method: POST
  name: create-payment-order
  path: /v1/payments
- description: Initiate a fund transfer
  method: POST
  name: create-fund-transfer
  path: /v1/transfers
personas: []
provider_name: Temenos Transact
provider_slug: temenos-transact
search_terms:
- transaction history
- list payment beneficiaries
- list banking products from the catalog
- create a payment order
- get account details by id
- list deposit arrangements
- initiate a fund transfer between accounts
- list customer accounts with optional filters
- create beneficiary
- fintech
- list cards
- list customer accounts
- get transaction history for an account
- get customer details
- banking
- payments
- get account
- create a new customer
- validate an iban and resolve bank details
- get transaction history
- account balances
- list products
- register a new payment beneficiary
- list loan arrangements
- account details
- list accounts
- financial services
- create payment order
- get account balances
- get customer
- get fund transfer status and details
- submit a payment order
- list beneficiaries
- fund transfers
- get customer accounts
- list accounts for a customer
- cancel payment order
- list debit and credit cards
- get account details
- cancel a pending payment order
- get account balance information
- list customers
- create customer
- temenos
- create fund transfer
- account management
- create a customer
- customer management
- core banking
- get account transactions
- list currencies
- validate iban
- payment operations
- list loans
- enterprise
- list deposits
- list payment orders
- initiate a fund transfer
- digital banking
- list available currencies
- get fund transfer
slug: digital-banking
tags:
- Temenos
- Digital Banking
- Core Banking
- Payments
tools:
- description: List customer accounts with optional filters
  hints:
    openWorld: true
    readOnly: true
  name: list-accounts
- description: Get account details by ID
  hints:
    readOnly: true
  name: get-account
- description: Get account balance information
  hints:
    readOnly: true
  name: get-account-balances
- description: Get transaction history for an account
  hints:
    readOnly: true
  name: get-account-transactions
- description: List customers
  hints:
    openWorld: true
    readOnly: true
  name: list-customers
- description: Get customer details
  hints:
    readOnly: true
  name: get-customer
- description: Create a new customer
  hints: {}
  name: create-customer
- description: List accounts for a customer
  hints:
    readOnly: true
  name: get-customer-accounts
- description: Initiate a fund transfer between accounts
  hints: {}
  name: create-fund-transfer
- description: Get fund transfer status and details
  hints:
    readOnly: true
  name: get-fund-transfer
- description: List payment orders
  hints:
    openWorld: true
    readOnly: true
  name: list-payment-orders
- description: Submit a payment order
  hints: {}
  name: create-payment-order
- description: Cancel a pending payment order
  hints:
    destructive: true
  name: cancel-payment-order
- description: List deposit arrangements
  hints:
    readOnly: true
  name: list-deposits
- description: List loan arrangements
  hints:
    readOnly: true
  name: list-loans
- description: List payment beneficiaries
  hints:
    readOnly: true
  name: list-beneficiaries
- description: Register a new payment beneficiary
  hints: {}
  name: create-beneficiary
- description: List banking products from the catalog
  hints:
    readOnly: true
  name: list-products
- description: List available currencies
  hints:
    readOnly: true
  name: list-currencies
- description: Validate an IBAN and resolve bank details
  hints:
    readOnly: true
  name: validate-iban
- description: List debit and credit cards
  hints:
    readOnly: true
  name: list-cards
---
