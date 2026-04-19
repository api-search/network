---
api_count: 1
apis:
- description: The Amazon Managed Blockchain API provides a fully managed service for creating and managing scalable blockchain networks using open-source frameworks such as Hyperledger Fabric and Ethereum. Covers 2
  name: Amazon Managed Blockchain API
  slug: amazon-managed-blockchain-api
capabilities:
- description: Workflow capability for blockchain architects and developers to create and manage Hyperledger Fabric and Ethereum networks, members, peer nodes, and proposals on Amazon Managed Blockchain.
  name: Amazon Managed Blockchain - Network Operations
  slug: blockchain-network-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/managed-blockchain/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/managed-blockchain/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/managedblockchain/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-managed-blockchain-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-managed-blockchain-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/blockchain-network-operations.yaml
created: '2024-01-15'
description: Amazon Managed Blockchain is a fully managed service that allows you to create and manage scalable blockchain networks using popular open-source frameworks such as Hyperledger Fabric and Ethereum. It eliminates the overhead required to create the network or join a public network, and automatically scales to meet the demands of thousands of applications running millions of transactions.
features:
- description: Create permissioned blockchain networks using Hyperledger Fabric framework.
  name: Hyperledger Fabric Support
- description: Create and participate in public Ethereum networks.
  name: Ethereum Support
- description: Invite AWS accounts to join your network as members and manage their access.
  name: Network Member Management
- description: Create and manage peer nodes to participate in blockchain network transactions.
  name: Peer Node Management
- description: Create and vote on proposals to manage network configuration changes.
  name: Proposal and Voting
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Store blockchain application code and configuration in S3 buckets.
  name: Amazon S3
- description: Encrypt blockchain network data using AWS Key Management Service.
  name: AWS KMS
- description: Monitor blockchain node and network metrics in CloudWatch.
  name: Amazon CloudWatch
jsonld:
- class_count: 93
  name: Amazon Managed Blockchain Context
  property_count: 68
  slug: amazon-managed-blockchain-context
layout: provider
modified: '2026-04-19'
name: Amazon Managed Blockchain
rules:
- name: Amazon Managed Blockchain API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 7
  slug: amazon-managed-blockchain-spectral-rules
skills: []
slug: amazon-managed-blockchain
solutions: []
tags:
- AWS
- Blockchain
- Distributed Ledger
- Hyperledger Fabric
- Ethereum
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-blockchain/refs/heads/main/apis.yml
use_cases:
- description: Track products through supply chains with immutable blockchain records shared across organizations.
  name: Supply Chain Transparency
- description: Automate financial settlement processes with smart contracts on Hyperledger Fabric.
  name: Financial Settlement
- description: Share patient data securely across healthcare providers using blockchain consent records.
  name: Healthcare Data Sharing
- description: Manage digital assets and NFTs on Ethereum through a fully managed blockchain service.
  name: Digital Asset Management
---
