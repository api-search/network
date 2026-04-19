---
description: Represents a single asset transfer event on the blockchain.
layout: schema
name: Asset Transfer
properties_list:
- description: Block number of the transfer in hexadecimal.
  name: blockNum
  type: string
- description: Transaction hash of the transfer.
  name: hash
  type: string
- description: Sender wallet address.
  name: from
  type: string
- description: Recipient wallet address.
  name: to
  type: string
- description: Transfer value in native units.
  name: value
  type: number
- description: Asset symbol (e.g., ETH, USDC, or NFT collection name).
  name: asset
  type: string
- description: Transfer category (external, internal, erc20, erc721, erc1155).
  name: category
  type: string
- description: Additional metadata for an asset transfer.
  name: metadata
  type: object
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-transfers-api-asset-transfer-schema.json
slug: alchemy-transfers-api-asset-transfer
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Asset Transfer
---
