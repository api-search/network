---
class_count: 7
classes:
- CoreNetwork
- description
- ListCoreNetworksResponse
- CreateCoreNetworkRequest
- CreateCoreNetworkResponse
- GetCoreNetworkResponse
- DeleteCoreNetworkResponse
context_file: json-ld/amazon-cloud-wan-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloud-wan/refs/heads/main/json-ld/amazon-cloud-wan-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Cloud Wan from Amazon Cloud WAN.
layout: jsonld
name: Amazon Cloud Wan Context
namespaces:
- prefix: cloudwan
  uri: https://aws.amazon.com/cloud-wan/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: coreNetworkId
  type: string
- container: ''
  name: coreNetworkArn
  type: string
- container: ''
  name: globalNetworkId
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: set
  name: coreNetworks
  type: ''
- container: ''
  name: nextToken
  type: string
- container: set
  name: tags
  type: ''
- container: ''
  name: coreNetwork
  type: string
property_count: 9
provider_name: Amazon Cloud WAN
provider_slug: amazon-cloud-wan
slug: amazon-cloud-wan-context
tags:
- AWS
- Cloud WAN
- Networking
- Wide Area Network
- SD-WAN
- JSON-LD
- Linked Data
- Semantic Web
---
