---
description: JSON-RPC request to sponsor a user operation via the Gas Manager paymaster.
layout: schema
name: Sponsor User Operation Request
properties_list:
- description: Request ID.
  name: id
  type: integer
- description: JSON-RPC version.
  name: jsonrpc
  type: string
- description: Alchemy paymaster method.
  name: method
  type: string
- description: Sponsorship parameters array.
  name: params
  type: array
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-gas-manager-api-sponsor-user-operation-request-schema.json
slug: alchemy-gas-manager-api-sponsor-user-operation-request
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Sponsor User Operation Request
---
