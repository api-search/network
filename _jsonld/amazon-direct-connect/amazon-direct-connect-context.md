---
class_count: 19
classes:
- AssociatedGateway
- BGPPeer
- Connection
- CustomerAgreement
- DirectConnectGateway
- DirectConnectGatewayAssociation
- DirectConnectGatewayAttachment
- Interconnect
- Lag
- Location
- NewPrivateVirtualInterface
- NewPublicVirtualInterface
- NewTransitVirtualInterface
- ResourceTag
- RouteFilterPrefix
- Tag
- VirtualGateway
- VirtualInterface
- VirtualInterfaceTestHistory
context_file: json-ld/amazon-direct-connect-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-direct-connect/refs/heads/main/json-ld/amazon-direct-connect-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Direct Connect from Amazon Direct Connect.
layout: jsonld
name: Amazon Direct Connect Context
namespaces:
- prefix: amz
  uri: https://amazonaws.com/direct-connect/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: addressFamily
  type: string
- container: ''
  name: agreementName
  type: string
- container: ''
  name: allowedPrefixesToDirectConnectGateway
  type: string
- container: ''
  name: allowsHostedConnections
  type: string
- container: ''
  name: amazonAddress
  type: string
- container: ''
  name: amazonSideAsn
  type: string
- container: ''
  name: asn
  type: string
- container: ''
  name: associatedGateway
  type: string
- container: ''
  name: associationId
  type: string
- container: ''
  name: associationState
  type: string
- container: ''
  name: attachmentState
  type: string
- container: ''
  name: attachmentType
  type: string
- container: ''
  name: authKey
  type: string
- container: ''
  name: availableMacSecPortSpeeds
  type: string
- container: ''
  name: availablePortSpeeds
  type: string
- container: ''
  name: availableProviders
  type: string
- container: ''
  name: awsDevice
  type: string
- container: ''
  name: awsDeviceV2
  type: string
- container: ''
  name: awsLogicalDeviceId
  type: string
- container: ''
  name: bandwidth
  type: string
- container: ''
  name: bgpPeerId
  type: string
- container: ''
  name: bgpPeerState
  type: string
- container: ''
  name: bgpPeers
  type: string
- container: ''
  name: bgpStatus
  type: string
- container: ''
  name: cidr
  type: string
- container: ''
  name: connectionId
  type: string
- container: ''
  name: connectionName
  type: string
- container: ''
  name: connectionState
  type: string
- container: ''
  name: connections
  type: string
- container: ''
  name: connectionsBandwidth
  type: string
- container: ''
  name: customerAddress
  type: string
- container: ''
  name: customerRouterConfig
  type: string
- container: ''
  name: directConnectGatewayId
  type: string
- container: ''
  name: directConnectGatewayName
  type: string
- container: ''
  name: directConnectGatewayOwnerAccount
  type: string
- container: ''
  name: directConnectGatewayState
  type: string
- container: ''
  name: enableSiteLink
  type: string
- container: ''
  name: encryptionMode
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: hasLogicalRedundancy
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: interconnectId
  type: string
- container: ''
  name: interconnectName
  type: string
- container: ''
  name: interconnectState
  type: string
- container: ''
  name: jumboFrameCapable
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: lagId
  type: string
- container: ''
  name: lagName
  type: string
- container: ''
  name: lagState
  type: string
- container: ''
  name: loaIssueTime
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: locationCode
  type: string
- container: ''
  name: locationName
  type: string
- container: ''
  name: macSecCapable
  type: string
- container: ''
  name: macSecKeys
  type: string
- container: ''
  name: minimumLinks
  type: string
- container: ''
  name: mtu
  type: string
- container: ''
  name: numberOfConnections
  type: string
- container: ''
  name: ownerAccount
  type: string
- container: ''
  name: partnerName
  type: string
- container: ''
  name: portEncryptionStatus
  type: string
- container: ''
  name: providerName
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: resourceArn
  type: string
- container: ''
  name: routeFilterPrefixes
  type: string
- container: ''
  name: siteLinkEnabled
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: stateChangeError
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: testDurationInMinutes
  type: string
- container: ''
  name: testId
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: virtualGatewayId
  type: string
- container: ''
  name: virtualGatewayOwnerAccount
  type: string
- container: ''
  name: virtualGatewayRegion
  type: string
- container: ''
  name: virtualGatewayState
  type: string
- container: ''
  name: virtualInterfaceId
  type: string
- container: ''
  name: virtualInterfaceName
  type: string
- container: ''
  name: virtualInterfaceOwnerAccount
  type: string
- container: ''
  name: virtualInterfaceRegion
  type: string
- container: ''
  name: virtualInterfaceState
  type: string
- container: ''
  name: virtualInterfaceType
  type: string
- container: ''
  name: vlan
  type: string
property_count: 85
provider_name: Amazon Direct Connect
provider_slug: amazon-direct-connect
slug: amazon-direct-connect-context
tags:
- AWS
- Dedicated Connection
- Direct Connect
- Hybrid Cloud
- Networking
- JSON-LD
- Linked Data
- Semantic Web
---
