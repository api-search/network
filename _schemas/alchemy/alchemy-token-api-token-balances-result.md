---
description: Result payload for token balance queries.
layout: schema
name: Token Balances Result
properties_list:
- description: Wallet address queried.
  name: address
  type: string
- description: List of token balances for the wallet.
  name: tokenBalances
  type: array
- description: Pagination key for fetching the next page.
  name: pageKey
  type: string
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-token-api-token-balances-result-schema.json
slug: alchemy-token-api-token-balances-result
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Token Balances Result
---
