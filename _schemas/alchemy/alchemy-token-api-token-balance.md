---
description: ERC-20 token balance entry for a wallet address.
layout: schema
name: Token Balance
properties_list:
- description: Token contract address.
  name: contractAddress
  type: string
- description: Token balance in hexadecimal (raw units, divide by 10^decimals).
  name: tokenBalance
  type: string
- description: Error message if the balance could not be retrieved.
  name: error
  type: string
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-token-api-token-balance-schema.json
slug: alchemy-token-api-token-balance
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Token Balance
---
