---
class_count: 6
classes:
- AkriDiscoveryResponseResult
- AkriInstanceCount
- AkriBrokerPodCount
- AkriInstance
- AkriConfiguration
- AkriDiscoveryResponseTime
context_file: json-ld/akri-akri-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-ld/akri-akri-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Akri Akri from Akri.
layout: jsonld
name: Akri Akri Context
namespaces:
- prefix: akri
  uri: https://akri.sh/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: apiVersion
  type: string
- container: ''
  name: capacity
  type: integer
- container: ''
  name: configuration
  type: string
- container: ''
  name: configurationName
  type: string
- container: ''
  name: deviceUsage
  type: reference
- container: ''
  name: discoveryDetails
  type: string
- container: ''
  name: discoveryHandler
  type: reference
- container: set
  name: discoveryProperties
  type: string
- container: ''
  name: kind
  type: string
- container: ''
  name: le
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: name
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: node
  type: string
- container: set
  name: nodes
  type: string
- container: ''
  name: result
  type: string
- container: ''
  name: shared
  type: string
- container: ''
  name: spec
  type: reference
- container: ''
  name: value
  type: decimal
property_count: 19
provider_name: Akri
provider_slug: akri
slug: akri-akri-context
tags:
- Device Management
- Edge Computing
- IoT
- Kubernetes
- CNCF
- Open Source
- OPC UA
- ONVIF
- udev
- JSON-LD
- Linked Data
- Semantic Web
---
