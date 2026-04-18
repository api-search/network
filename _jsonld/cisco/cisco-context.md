---
class_count: 4
classes:
- Organization
- Network
- Device
- Client
context_file: json-ld/cisco-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/cisco/refs/heads/main/json-ld/cisco-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Cisco from Cisco.
layout: jsonld
name: Cisco Context
namespaces:
- prefix: cisco
  uri: https://cisco.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: serial
  type: string
- container: ''
  name: mac
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: networkId
  type: string
- container: ''
  name: lanIp
  type: string
- container: ''
  name: firmware
  type: string
- container: set
  name: productTypes
  type: ''
- container: set
  name: tags
  type: ''
- container: ''
  name: timeZone
  type: string
- container: ''
  name: ip
  type: string
- container: ''
  name: os
  type: string
- container: ''
  name: status
  type: string
property_count: 14
provider_name: Cisco
provider_slug: cisco
slug: cisco-context
tags:
- Collaboration
- Enterprise
- Networking
- Security
- SD-WAN
- JSON-LD
- Linked Data
- Semantic Web
---
