---
description: A gas sponsorship policy defining rules for covering user operation gas fees.
layout: schema
name: Gas Manager Policy
properties_list:
- description: Unique identifier for the policy.
  name: policyId
  type: string
- description: Display name for the policy.
  name: name
  type: string
- description: Current status of the policy.
  name: status
  type: string
- description: Blockchain network the policy applies to.
  name: network
  type: string
- description: Maximum ETH spend per user address covered by this policy.
  name: maxSpendPerUser
  type: number
- description: Maximum total ETH spend across all users for this policy.
  name: maxSpendTotal
  type: number
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-gas-manager-api-policy-schema.json
slug: alchemy-gas-manager-api-policy
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Gas Manager Policy
---
