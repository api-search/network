---
class_count: 8
classes:
- BandwidthAllocation
- IKEGateway
- IKEGatewayConfig
- IPsecTunnel
- OnboardingStatus
- PrismaAccessLocation
- RemoteNetwork
- RemoteNetworkRequest
context_file: json-ld/palo-alto-sase-config-orchestration-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-config-orchestration-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase Config Orchestration Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase Config Orchestration Api Context
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
  name: allocatedBandwidthMbps
  type: integer
- container: ''
  name: authenticationType
  type: string
- container: ''
  name: availableBandwidthMbps
  type: integer
- container: ''
  name: bandwidthMbps
  type: integer
- container: ''
  name: city
  type: string
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: country
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: description
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: ikeGateway
  type: reference
- container: ''
  name: ikeVersion
  type: string
- container: ''
  name: ipsecTunnel
  type: reference
- container: ''
  name: licensedBandwidthMbps
  type: integer
- container: ''
  name: localAddress
  type: string
- container: ''
  name: localIp
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: peerId
  type: string
- container: ''
  name: peerIp
  type: string
- container: ''
  name: preSharedKey
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: remoteAddress
  type: string
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: step
  type: string
- container: set
  name: steps
  type: reference
- container: set
  name: subnets
  type: string
- container: ''
  name: tunnelInterface
  type: string
- container: ''
  name: tunnelStatus
  type: string
- container: ''
  name: updatedAt
  type: dateTime
property_count: 34
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-config-orchestration-api-context
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
