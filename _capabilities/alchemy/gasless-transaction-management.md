---
consumed_apis:
- gas-manager
description: Capability for managing gasless transaction sponsorship using ERC-4337 Account Abstraction. Combines the Gas Manager API for policy creation and management with paymaster sponsorship. Designed for dApp developers and Web3 platform teams who want to abstract gas fees from end users.
layout: capability
name: Alchemy Gasless Transaction Management
operations:
- description: List all gas sponsorship policies.
  method: GET
  name: list-policies
  path: /v1/policies
- description: Create a new gas sponsorship policy.
  method: POST
  name: create-policy
  path: /v1/policies
- description: Get a specific gas sponsorship policy.
  method: GET
  name: get-policy
  path: /v1/policies/{policyId}
- description: Sponsor a user operation for gasless transactions.
  method: POST
  name: sponsor-user-operation
  path: /v1/sponsor
personas:
- description: Creates decentralized applications with gasless UX for end users.
  id: dapp-developer
  name: dApp Developer
- description: Manages gas sponsorship infrastructure and ERC-4337 policies.
  id: web3-platform-engineer
  name: Web3 Platform Engineer
provider_name: Alchemy
provider_slug: alchemy
search_terms:
- gas manager
- web3
- submit a user operation for erc-4337 gas sponsorship, enabling gasless transactions.
- gas fee sponsorship and erc-4337 account abstraction.
- cryptocurrency
- manages gas sponsorship infrastructure and erc-4337 policies.
- sponsor user operation
- develops defi applications requiring portfolio tracking and token data.
- ethereum
- gas sponsorship for user operations.
- blockchain
- wallet developer
- defi builder
- wallet balance and asset portfolio management.
- manages gasless transaction sponsorship using erc-4337 account abstraction via gas manager api.
- list all gas sponsorship policies.
- create policy
- list all gas manager sponsorship policies for the alchemy application.
- alchemy
- account abstraction
- sponsor a user operation for gasless transactions.
- create a new gas sponsorship policy.
- get a specific gas sponsorship policy.
- on-chain asset transfer history.
- gas sponsorship policies.
- list policies
- get policy
- web3 platform engineer
- get details for a specific gas sponsorship policy by id.
- combines token api and transfers api for wallet portfolio applications.
- builds evm wallet applications needing token balances and transaction history.
- create a new gas sponsorship policy with spend limits and network settings.
- creates decentralized applications with gasless ux for end users.
- dapp developer
- individual gas policy.
- erc-20 token data and metadata.
slug: gasless-transaction-management
tags:
- Alchemy
- Blockchain
- Gas Manager
- Account Abstraction
- Web3
tools:
- description: List all gas manager sponsorship policies for the Alchemy application.
  hints:
    idempotent: true
    readOnly: true
  name: list-policies
- description: Create a new gas sponsorship policy with spend limits and network settings.
  hints:
    idempotent: false
    readOnly: false
  name: create-policy
- description: Get details for a specific gas sponsorship policy by ID.
  hints:
    idempotent: true
    readOnly: true
  name: get-policy
- description: Submit a user operation for ERC-4337 gas sponsorship, enabling gasless transactions.
  hints:
    idempotent: false
    readOnly: false
  name: sponsor-user-operation
---
