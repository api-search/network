---
class_count: 8
classes:
- Alarm
- ApplicationUsage
- LANNetwork
- PathRule
- QoSRule
- Site
- SiteMetric
- WANInterface
context_file: json-ld/palo-alto-prisma-sd-wan-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-sd-wan-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Sd Wan Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Sd Wan Api Context
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
  name: acknowledged
  type: boolean
- container: ''
  name: acknowledgedAt
  type: dateTime
- container: ''
  name: acknowledgedBy
  type: string
- container: ''
  name: address
  type: reference
- container: ''
  name: adminState
  type: string
- container: set
  name: appFilters
  type: string
- container: ''
  name: application
  type: string
- container: ''
  name: avgLatencyMs
  type: decimal
- container: ''
  name: bandwidthLimitDown
  type: decimal
- container: ''
  name: bandwidthLimitUp
  type: decimal
- container: ''
  name: bytesDown
  type: integer
- container: ''
  name: bytesUp
  type: integer
- container: ''
  name: city
  type: string
- container: ''
  name: clearedAt
  type: dateTime
- container: ''
  name: cost
  type: integer
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
  name: dhcpEnabled
  type: boolean
- container: ''
  name: direction
  type: string
- container: ''
  name: dscpClass
  type: string
- container: ''
  name: elementClusterRole
  type: string
- container: ''
  name: elementId
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: interfaceName
  type: string
- container: ''
  name: jitterMs
  type: integer
- container: ''
  name: label
  type: string
- container: ''
  name: labelId
  type: string
- container: ''
  name: latencyMs
  type: integer
- container: ''
  name: latitude
  type: double
- container: ''
  name: linkBwDown
  type: decimal
- container: ''
  name: linkBwUp
  type: decimal
- container: ''
  name: location
  type: reference
- container: ''
  name: longitude
  type: double
- container: ''
  name: lqmEnabled
  type: boolean
- container: ''
  name: message
  type: string
- container: ''
  name: metricType
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: network
  type: string
- container: ''
  name: packetLossPct
  type: decimal
- container: ''
  name: postCode
  type: string
- container: set
  name: preferredPaths
  type: reference
- container: ''
  name: priority
  type: integer
- container: ''
  name: raisedAt
  type: dateTime
- container: ''
  name: sessions
  type: integer
- container: ''
  name: severity
  type: string
- container: ''
  name: siteId
  type: string
- container: ''
  name: siteName
  type: string
- container: ''
  name: slaThreshold
  type: reference
- container: ''
  name: state
  type: string
- container: ''
  name: street
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: value
  type: decimal
- container: ''
  name: vlanId
  type: integer
property_count: 59
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-sd-wan-api-context
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
