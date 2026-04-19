---
class_count: 7
classes:
- Sponsor User Operation Response
- Sponsor User Operation Result
- Policy List Response
- Sponsor User Operation Request
- Gas Manager Policy
- Create Policy Request
- name
context_file: json-ld/alchemy-gas-manager-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/json-ld/alchemy-gas-manager-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Alchemy Gas Manager Api from Alchemy.
layout: jsonld
name: Alchemy Gas Manager Api Context
namespaces:
- prefix: alchemy
  uri: https://alchemy.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: callGasLimit
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: jsonrpc
  type: string
- container: ''
  name: maxSpendPerUser
  type: decimal
- container: ''
  name: maxSpendTotal
  type: decimal
- container: ''
  name: method
  type: string
- container: ''
  name: network
  type: string
- container: set
  name: params
  type: string
- container: ''
  name: paymasterAndData
  type: string
- container: set
  name: policies
  type: reference
- container: ''
  name: policyId
  type: string
- container: ''
  name: preVerificationGas
  type: string
- container: ''
  name: result
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: verificationGasLimit
  type: string
property_count: 15
provider_name: Alchemy
provider_slug: alchemy
slug: alchemy-gas-manager-api-context
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
- JSON-LD
- Linked Data
- Semantic Web
---
