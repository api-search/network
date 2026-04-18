---
class_count: 7
classes:
- IKEGateway
- IPSecTunnel
- JobStatus
- MobileAgentInfrastructureSettings
- RemoteNetwork
- SecurityRule
- ServiceConnection
context_file: json-ld/palo-alto-prisma-access-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-access-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Access Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Access Api Context
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
  name: action
  type: string
- container: set
  name: addresses
  type: string
- container: ''
  name: antiReplay
  type: boolean
- container: set
  name: application
  type: string
- container: ''
  name: authentication
  type: reference
- container: ''
  name: autoKey
  type: reference
- container: set
  name: category
  type: string
- container: ''
  name: certificate
  type: reference
- container: ''
  name: description
  type: string
- container: set
  name: destination
  type: string
- container: ''
  name: destinationIp
  type: string
- container: set
  name: details
  type: string
- container: ''
  name: disabled
  type: boolean
- container: set
  name: dnsServers
  type: string
- container: set
  name: dnsSuffix
  type: string
- container: ''
  name: dynamic
  type: boolean
- container: ''
  name: ecmpLoadBalancing
  type: string
- container: ''
  name: enable
  type: boolean
- container: ''
  name: endTs
  type: dateTime
- container: ''
  name: folder
  type: string
- container: set
  name: from
  type: string
- container: set
  name: group
  type: string
- container: ''
  name: id
  type: string
- container: set
  name: ikeGateway
  type: reference
- container: ''
  name: ip
  type: string
- container: set
  name: ipPool
  type: string
- container: ''
  name: ipsecCryptoProfile
  type: string
- container: ''
  name: ipsecTunnel
  type: string
- container: ''
  name: licenseType
  type: string
- container: ''
  name: localCertificate
  type: string
- container: ''
  name: localId
  type: reference
- container: ''
  name: logSetting
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: natPool
  type: string
- container: ''
  name: peerAddress
  type: reference
- container: ''
  name: peerId
  type: reference
- container: ''
  name: position
  type: string
- container: ''
  name: preSharedKey
  type: string
- container: ''
  name: profileSetting
  type: reference
- container: ''
  name: proxyId
  type: string
- container: ''
  name: qosEnabled
  type: boolean
- container: ''
  name: region
  type: string
- container: set
  name: regions
  type: reference
- container: ''
  name: result
  type: string
- container: set
  name: service
  type: string
- container: set
  name: source
  type: string
- container: set
  name: sourceUser
  type: string
- container: ''
  name: spnName
  type: string
- container: ''
  name: startTs
  type: dateTime
- container: ''
  name: status
  type: string
- container: set
  name: subnets
  type: string
- container: set
  name: tag
  type: string
- container: set
  name: to
  type: string
- container: ''
  name: tunnelMonitor
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: version
  type: string
property_count: 56
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-access-api-context
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
