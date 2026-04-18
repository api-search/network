---
class_count: 8
classes:
- DedicatedVlanAttachmentDetailsEntry
- IPBlockEntry
- IPPoolRequest
- InterconnectRequest
- PhysicalConnectionEntry
- SettingsEntry
- VlanAttachmentCustomIpAddress
- VlanAttachmentRequest
context_file: json-ld/palo-alto-sase-multitenant-interconnect-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-multitenant-interconnect-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase Multitenant Interconnect Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase Multitenant Interconnect Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: bandwidth
  type: string
- container: ''
  name: bgpPeerAsn
  type: integer
- container: ''
  name: bgpPeerBfdMinReceiveInterval
  type: integer
- container: ''
  name: bgpPeerBfdMinTransmitInterval
  type: integer
- container: ''
  name: bgpPeerBfdMultiplier
  type: integer
- container: ''
  name: bgpPeerBfdSessionInitMode
  type: string
- container: ''
  name: bgpPeerMd5AuthEnabled
  type: boolean
- container: ''
  name: candidateCloudRouterIpAddress
  type: string
- container: ''
  name: candidateCustomerRouterIpAddress
  type: string
- container: set
  name: cidr
  type: string
- container: ''
  name: cloudProvider
  type: string
- container: set
  name: coloFacilities
  type: string
- container: set
  name: dedicatedConnectionDetails
  type: reference
- container: ''
  name: edgeAvailability
  type: string
- container: ''
  name: edgeLocation
  type: string
- container: ''
  name: egressType
  type: string
- container: set
  name: ipBlocks
  type: reference
- container: ''
  name: ipPool
  type: reference
- container: ''
  name: ipProvider
  type: string
- container: ''
  name: linkType
  type: string
- container: ''
  name: macSecEnabled
  type: boolean
- container: ''
  name: name
  type: string
- container: ''
  name: partnerEmail
  type: string
- container: ''
  name: partnerName
  type: string
- container: ''
  name: physicalConnection
  type: reference
- container: ''
  name: physicalConnectionName
  type: string
- container: ''
  name: primaryAttachmentCustomIpAddress
  type: reference
- container: ''
  name: redundantAttachmentCustomIpAddress
  type: reference
- container: ''
  name: region
  type: string
- container: ''
  name: requestedLinkCount
  type: integer
- container: ''
  name: stackType
  type: string
- container: ''
  name: tsgId
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: usage
  type: string
- container: ''
  name: vlanAttachment
  type: reference
property_count: 35
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-multitenant-interconnect-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---
