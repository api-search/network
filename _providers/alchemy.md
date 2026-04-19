---
api_count: 4
apis:
- description: The Alchemy Gas Manager API enables developers to sponsor gas fees for end users via the ERC-4337 Account Abstraction standard. Manage sponsorship policies with per-user spend limits, total caps, allo
  name: Alchemy Gas Manager API
  slug: alchemy-gas-manager-api
- description: The Alchemy Token API provides comprehensive access to ERC-20 token data across EVM-compatible networks. Retrieve token balances by wallet address, token metadata (name, symbol, decimals, logo), and r
  name: Alchemy Token API
  slug: alchemy-token-api
- description: The Alchemy Transfers API provides access to historical on-chain transfer data across EVM-compatible networks. Query asset transfers by address, block range, and transfer category (ETH, ERC-20, ERC-72
  name: Alchemy Transfers API
  slug: alchemy-transfers-api
- description: The Alchemy Bundler API implements the ERC-4337 Account Abstraction bundler standard, allowing UserOperations to be submitted to the blockchain. Developers can send, estimate, and track UserOperations
  name: Alchemy Bundler API
  slug: alchemy-bundler-api
capabilities:
- description: Capability for managing gasless transaction sponsorship using ERC-4337 Account Abstraction. Combines the Gas Manager API for policy creation and management with paymaster sponsorship. Designed for dAp
  name: Alchemy Gasless Transaction Management
  slug: gasless-transaction-management
- description: Unified capability for building Web3 wallet and portfolio applications. Combines the Token API for balance and metadata queries with the Transfers API for transaction history. Designed for wallet deve
  name: Alchemy Web3 Wallet Portfolio
  slug: web3-wallet-portfolio
common:
- title: ''
  type: Pricing
  url: https://www.alchemy.com/pricing
- title: ''
  type: Sandbox
  url: https://www.alchemy.com/sandbox
- title: ''
  type: Webhooks
  url: https://www.alchemy.com/webhooks
- title: ''
  type: SDKs
  url: https://www.alchemy.com/sdk
- title: ''
  type: Blog
  url: https://www.alchemy.com/blog
- title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/alchemyapi/alchemy-platforms/overview
- title: ''
  type: Documentation
  url: https://docs.alchemy.com
- title: ''
  type: Support
  url: https://www.alchemy.com/support
- title: ''
  type: SignUp
  url: https://dashboard.alchemy.com/signup
- title: ''
  type: StatusPage
  url: https://status.alchemy.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/alchemyplatform
- title: ''
  type: SpectralRules
  url: rules/alchemy-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/alchemy-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/web3-wallet-portfolio.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/gasless-transaction-management.yaml
created: '2024-11-07T00:00:00.000Z'
description: Alchemy is a Web3 developer platform providing powerful APIs, SDKs, and infrastructure tools to build and scale blockchain applications. Supporting Ethereum, Polygon, and other EVM-compatible networks, Alchemy powers production dApps with reliable node infrastructure, enhanced APIs for token data, asset transfers, NFTs, and ERC-4337 Account Abstraction tools including gas sponsorship (Gas Manager) and smart account bundling.
features:
- description: Query token data and transfers across Ethereum, Polygon, and other EVM-compatible networks.
  name: Multi-Chain Support
- description: Full support for ERC-4337 with bundler, paymaster (Gas Manager), and smart account APIs.
  name: ERC-4337 Account Abstraction
- description: Sponsor gas fees for end users via Gas Manager policies with spend limits and network rules.
  name: Gasless Transactions
- description: Real-time ERC-20 token balances and metadata including name, symbol, decimals, and logo.
  name: Token Data
- description: Historical on-chain transfer data for ETH, ERC-20, ERC-721, and ERC-1155 assets.
  name: Transfer History
- description: Standard Ethereum JSON-RPC interface with Alchemy-enhanced methods for additional data.
  name: JSON-RPC Compatibility
- description: Real-time blockchain event notifications via webhooks for address activity and mined transactions.
  name: Webhook Notifications
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native support for Ethereum mainnet and testnets.
  name: Ethereum
- description: Full API support for Polygon (MATIC) mainnet and Mumbai testnet.
  name: Polygon
- description: Works with any ERC-4337 compatible bundler for UserOperation submission.
  name: ERC-4337 Bundlers
- description: Integration with MetaMask wallet for Web3 connection management.
  name: MetaMask
- description: Developer toolchain integration for local testing and deployment.
  name: Hardhat and Foundry
jsonld:
- class_count: 7
  name: Alchemy Gas Manager Api Context
  property_count: 15
  slug: alchemy-gas-manager-api-context
- class_count: 6
  name: Alchemy Token Api Context
  property_count: 12
  slug: alchemy-token-api-context
- class_count: 4
  name: Alchemy Transfers Api Context
  property_count: 14
  slug: alchemy-transfers-api-context
layout: provider
modified: '2026-04-19'
name: Alchemy
rules:
- name: Alchemy API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 15
  slug: alchemy-spectral-rules
skills: []
slug: alchemy
solutions: []
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/apis.yml
use_cases:
- description: Build EVM wallets with real-time token balances, transaction history, and NFT support.
  name: Wallet Application Development
- description: Track multi-asset portfolios across EVM networks with accurate token pricing and balances.
  name: DeFi Portfolio Tracking
- description: Abstract gas fees from end users so they can interact with dApps without holding ETH.
  name: Gasless dApp UX
- description: Query ERC-721 and ERC-1155 transfer history for NFT ownership tracking and provenance.
  name: NFT Marketplace Integration
- description: Analyze on-chain transfer patterns, wallet activity, and token flow across EVM networks.
  name: Blockchain Analytics
---
