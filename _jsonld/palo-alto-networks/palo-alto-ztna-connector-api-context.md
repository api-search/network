---
class_count: 11
classes:
- Connector
- ConnectorGroup
- ConnectorGroupRequest
- ConnectorRequest
- FQDNRule
- FQDNRuleRequest
- LicenseInfo
- SubnetRule
- SubnetRuleRequest
- ZTNAApplication
- ZTNAApplicationRequest
context_file: json-ld/palo-alto-ztna-connector-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-ztna-connector-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Ztna Connector Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Ztna Connector Api Context
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
  name: activeUsers
  type: integer
- container: ''
  name: appId
  type: string
- container: ''
  name: connectorCount
  type: integer
- container: ''
  name: connectorId
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: description
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: expiresAt
  type: dateTime
- container: set
  name: features
  type: string
- container: ''
  name: fqdn
  type: string
- container: ''
  name: fqdnPattern
  type: string
- container: ''
  name: groupId
  type: string
- container: ''
  name: hostname
  type: string
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: lastSeenAt
  type: dateTime
- container: ''
  name: licensedUsers
  type: integer
- container: ''
  name: name
  type: string
- container: set
  name: ports
  type: integer
- container: set
  name: protocols
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: ruleId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: subnet
  type: string
- container: ''
  name: subscriptionId
  type: string
- container: ''
  name: version
  type: string
property_count: 25
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-ztna-connector-api-context
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
