---
description: Result payload containing the list of asset transfers.
layout: schema
name: Asset Transfers Result
properties_list:
- description: List of asset transfer events matching the query.
  name: transfers
  type: array
- description: Pagination key for retrieving the next page of results.
  name: pageKey
  type: string
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-transfers-api-asset-transfers-result-schema.json
slug: alchemy-transfers-api-asset-transfers-result
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Asset Transfers Result
---
