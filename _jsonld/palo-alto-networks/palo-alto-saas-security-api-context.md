---
class_count: 6
classes:
- Application
- Asset
- Incident
- LogForwardingSettings
- User
- UserActivity
context_file: json-ld/palo-alto-saas-security-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-saas-security-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Saas Security Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Saas Security Api Context
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
  name: accountType
  type: string
- container: ''
  name: action
  type: string
- container: set
  name: affectedAssets
  type: string
- container: set
  name: affectedUsers
  type: string
- container: ''
  name: appId
  type: string
- container: ''
  name: appName
  type: string
- container: ''
  name: assetCount
  type: integer
- container: ''
  name: assetId
  type: string
- container: ''
  name: assigneeId
  type: string
- container: ''
  name: connectedAt
  type: dateTime
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: description
  type: string
- container: set
  name: destinations
  type: reference
- container: ''
  name: displayName
  type: string
- container: set
  name: dlpViolations
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: exposure
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: incidentCount
  type: integer
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: lastActivity
  type: dateTime
- container: ''
  name: lastScannedAt
  type: dateTime
- container: set
  name: logTypes
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: policyName
  type: string
- container: ''
  name: riskLevel
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: sizeBytes
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: title
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: userId
  type: string
property_count: 36
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-saas-security-api-context
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
