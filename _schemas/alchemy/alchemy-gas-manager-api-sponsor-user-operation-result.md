---
description: Paymaster response data for a sponsored user operation.
layout: schema
name: Sponsor User Operation Result
properties_list:
- description: Encoded paymaster address and data for the user operation.
  name: paymasterAndData
  type: string
- description: Pre-verification gas estimate in hexadecimal.
  name: preVerificationGas
  type: string
- description: Verification gas limit in hexadecimal.
  name: verificationGasLimit
  type: string
- description: Call gas limit in hexadecimal.
  name: callGasLimit
  type: string
provider_name: Alchemy
provider_slug: alchemy
schema_file: json-schema/alchemy-gas-manager-api-sponsor-user-operation-result-schema.json
slug: alchemy-gas-manager-api-sponsor-user-operation-result
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
title: Sponsor User Operation Result
---
