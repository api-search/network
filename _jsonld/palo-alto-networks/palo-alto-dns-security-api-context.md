---
class_count: 2
classes:
- DomainDetail
- NetworkStats
context_file: json-ld/palo-alto-dns-security-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-dns-security-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Dns Security Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Dns Security Api Context
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
  name: allowedQueries
  type: integer
- container: ''
  name: blockedQueries
  type: integer
- container: ''
  name: category
  type: string
- container: set
  name: categoryBreakdown
  type: reference
- container: ''
  name: count
  type: integer
- container: ''
  name: customerid
  type: string
- container: ''
  name: dnsSecurityCategory
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: end
  type: string
- container: ''
  name: firstSeen
  type: dateTime
- container: set
  name: ipAddresses
  type: string
- container: ''
  name: lastSeen
  type: dateTime
- container: ''
  name: percentage
  type: float
- container: ''
  name: period
  type: reference
- container: ''
  name: queryCount
  type: integer
- container: ''
  name: registrar
  type: string
- container: ''
  name: registrationDate
  type: date
- container: ''
  name: riskLevel
  type: string
- container: ''
  name: riskScore
  type: float
- container: ''
  name: sinkholedQueries
  type: integer
- container: ''
  name: start
  type: string
- container: set
  name: topQueriedDomains
  type: reference
- container: ''
  name: totalQueries
  type: integer
property_count: 23
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-dns-security-api-context
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
