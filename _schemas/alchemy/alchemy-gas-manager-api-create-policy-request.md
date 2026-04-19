---
description: Request body for creating a new gas manager policy.
layout: schema
name: Create Policy Request
properties_list:
- description: Display name for the new policy.
  name: name
  type: string
- description: Blockchain network for the policy.
  name: network
  type: string
- description: Maximum ETH spend per user (optional).
  name: maxSpendPerUser
  type: number
- description: Maximum total ETH spend across all users (optional).
  name: maxSpendTotal
  type: number
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-gas-manager-api-create-policy-request-schema.json
slug: alchemy-gas-manager-api-create-policy-request
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Create Policy Request
---
