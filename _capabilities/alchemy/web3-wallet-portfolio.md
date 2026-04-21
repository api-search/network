---
consumed_apis:
- token-api
- transfers-api
description: Unified capability for building Web3 wallet and portfolio applications. Combines the Token API for balance and metadata queries with the Transfers API for transaction history. Designed for wallet developers, DeFi app builders, and portfolio tracker teams who need comprehensive on-chain data for any EVM-compatible wallet address.
layout: capability
name: Alchemy Web3 Wallet Portfolio
operations:
- description: Get ERC-20 token balances for a wallet address.
  method: POST
  name: get-token-balances
  path: /v1/token-balances
- description: Get metadata for an ERC-20 token contract.
  method: POST
  name: get-token-metadata
  path: /v1/token-metadata
- description: Query historical asset transfers for a wallet address.
  method: POST
  name: get-asset-transfers
  path: /v1/transfers
personas:
- description: Builds EVM wallet applications needing token balances and transaction history.
  id: wallet-developer
  name: Wallet Developer
- description: Develops DeFi applications requiring portfolio tracking and token data.
  id: defi-builder
  name: DeFi Builder
provider_name: Alchemy
provider_slug: alchemy
search_terms:
- get erc-20 token balances for a wallet address.
- get token metadata
- erc-20 token balances for a wallet.
- web3
- get metadata (name, symbol, decimals, logo) for an erc-20 token contract.
- query historical on-chain asset transfers for a wallet by address, block range, and category.
- gas fee sponsorship and erc-4337 account abstraction.
- cryptocurrency
- manages gas sponsorship infrastructure and erc-4337 policies.
- develops defi applications requiring portfolio tracking and token data.
- ethereum
- get erc-20 token balances for a wallet address across evm networks.
- portfolio
- blockchain
- wallet developer
- defi builder
- wallet balance and asset portfolio management.
- manages gasless transaction sponsorship using erc-4337 account abstraction via gas manager api.
- transfers
- historical on-chain asset transfers.
- alchemy
- account abstraction
- on-chain asset transfer history.
- tokens
- web3 platform engineer
- combines token api and transfers api for wallet portfolio applications.
- get metadata for an erc-20 token contract.
- builds evm wallet applications needing token balances and transaction history.
- creates decentralized applications with gasless ux for end users.
- erc-20 token metadata.
- query historical asset transfers for a wallet address.
- dapp developer
- get asset transfers
- erc-20 token data and metadata.
- get token balances
slug: web3-wallet-portfolio
tags:
- Alchemy
- Blockchain
- Portfolio
- Tokens
- Transfers
- Web3
tools:
- description: Get ERC-20 token balances for a wallet address across EVM networks.
  hints:
    idempotent: true
    readOnly: true
  name: get-token-balances
- description: Get metadata (name, symbol, decimals, logo) for an ERC-20 token contract.
  hints:
    idempotent: true
    readOnly: true
  name: get-token-metadata
- description: Query historical on-chain asset transfers for a wallet by address, block range, and category.
  hints:
    idempotent: true
    readOnly: true
  name: get-asset-transfers
---
