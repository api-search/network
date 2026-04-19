---
class_count: 3
classes:
- ietf
- ietf-if
- ieee802
context_file: json-ld/cisco-nexus-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/cisco-nexus/refs/heads/main/json-ld/cisco-nexus-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Cisco Nexus from Cisco Nexus Dashboard.
layout: jsonld
name: Cisco Nexus Context
namespaces:
- prefix: cisco
  uri: https://developer.cisco.com/docs/nexus-model/latest/#
- prefix: nxos
  uri: https://developer.cisco.com/docs/nx-os/
- prefix: nxapi
  uri: https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference/latest/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: rdfs
  uri: http://www.w3.org/2000/01/rdf-schema#
properties:
- container: ''
  name: NexusSwitch
  type: ''
- container: ''
  name: PhysicalInterface
  type: ''
- container: ''
  name: SviInterface
  type: ''
- container: ''
  name: VlanBridgeDomain
  type: ''
- container: ''
  name: Ipv4StaticRoute
  type: ''
- container: ''
  name: Ipv4Nexthop
  type: ''
- container: ''
  name: BgpInstance
  type: ''
- container: ''
  name: BgpDomain
  type: ''
- container: ''
  name: BgpPeer
  type: ''
- container: ''
  name: EthernetStatistics
  type: ''
- container: ''
  name: VlanStatistics
  type: ''
- container: set
  name: interfaces
  type: reference
- container: set
  name: vlans
  type: reference
- container: set
  name: routes
  type: reference
- container: ''
  name: bgp
  type: reference
property_count: 15
provider_name: Cisco Nexus Dashboard
provider_slug: cisco-nexus
slug: cisco-nexus-context
tags:
- Data Center
- Infrastructure
- Network Automation
- Networking
- SDN
- Switches
- JSON-LD
- Linked Data
- Semantic Web
---
