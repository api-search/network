---
class_count: 4
classes:
- Asset Transfer
- Asset Transfers Response
- Asset Transfers Result
- Transfer Metadata
context_file: json-ld/alchemy-transfers-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/json-ld/alchemy-transfers-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Alchemy Transfers Api from Alchemy.
layout: jsonld
name: Alchemy Transfers Api Context
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
  name: asset
  type: string
- container: ''
  name: blockNum
  type: string
- container: ''
  name: blockTimestamp
  type: dateTime
- container: ''
  name: category
  type: string
- container: ''
  name: from
  type: string
- container: ''
  name: hash
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: jsonrpc
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: pageKey
  type: string
- container: ''
  name: result
  type: reference
- container: ''
  name: to
  type: string
- container: set
  name: transfers
  type: reference
- container: ''
  name: value
  type: decimal
property_count: 14
provider_name: Alchemy
provider_slug: alchemy
slug: alchemy-transfers-api-context
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
