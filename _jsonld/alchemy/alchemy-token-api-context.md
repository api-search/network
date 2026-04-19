---
class_count: 6
classes:
- Token Balance
- Token Balances Result
- Token Metadata Response
- Token Balances Response
- Token Metadata
- name
context_file: json-ld/alchemy-token-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/json-ld/alchemy-token-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Alchemy Token Api from Alchemy.
layout: jsonld
name: Alchemy Token Api Context
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
  name: address
  type: string
- container: ''
  name: contractAddress
  type: string
- container: ''
  name: decimals
  type: integer
- container: ''
  name: error
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: jsonrpc
  type: string
- container: ''
  name: logo
  type: reference
- container: ''
  name: pageKey
  type: string
- container: ''
  name: result
  type: reference
- container: ''
  name: symbol
  type: string
- container: ''
  name: tokenBalance
  type: string
- container: set
  name: tokenBalances
  type: reference
property_count: 12
provider_name: Alchemy
provider_slug: alchemy
slug: alchemy-token-api-context
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
