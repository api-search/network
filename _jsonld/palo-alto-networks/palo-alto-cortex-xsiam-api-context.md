---
class_count: 8
classes:
- Alert
- Asset
- AuditLog
- Endpoint
- Filter
- Incident
- SortOrder
- value
context_file: json-ld/palo-alto-cortex-xsiam-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xsiam-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cortex Xsiam Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cortex Xsiam Api Context
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
- container: ''
  name: actorEmail
  type: string
- container: ''
  name: actorPrimaryUsername
  type: string
- container: ''
  name: actorType
  type: string
- container: ''
  name: alertCount
  type: integer
- container: ''
  name: alertId
  type: string
- container: ''
  name: alertType
  type: string
- container: ''
  name: assetId
  type: string
- container: ''
  name: assetName
  type: string
- container: ''
  name: assetType
  type: string
- container: ''
  name: assignedUserMail
  type: string
- container: ''
  name: assignedUserPrettyName
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: contentVersion
  type: string
- container: ''
  name: creationTime
  type: integer
- container: ''
  name: description
  type: string
- container: ''
  name: detectionTime
  type: integer
- container: ''
  name: detectionTimestamp
  type: integer
- container: ''
  name: domain
  type: string
- container: ''
  name: endpointId
  type: string
- container: ''
  name: endpointName
  type: string
- container: ''
  name: endpointStatus
  type: string
- container: ''
  name: endpointType
  type: string
- container: ''
  name: endpointVersion
  type: string
- container: ''
  name: field
  type: string
- container: ''
  name: firstSeen
  type: integer
- container: ''
  name: hostName
  type: string
- container: ''
  name: incidentId
  type: string
- container: ''
  name: incidentName
  type: string
- container: ''
  name: ip
  type: string
- container: set
  name: ipAddresses
  type: string
- container: ''
  name: isIsolated
  type: string
- container: ''
  name: keyword
  type: string
- container: ''
  name: lastSeen
  type: integer
- container: set
  name: mitreTacticsIdsAndNames
  type: string
- container: set
  name: mitreTechniquesIdsAndNames
  type: string
- container: ''
  name: modificationTime
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: operatingSystem
  type: string
- container: ''
  name: operator
  type: string
- container: ''
  name: osType
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: resolutionStatus
  type: string
- container: ''
  name: result
  type: string
- container: ''
  name: riskScore
  type: decimal
- container: ''
  name: scanStatus
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: source
  type: string
- container: set
  name: sources
  type: string
- container: ''
  name: starred
  type: boolean
- container: ''
  name: status
  type: string
- container: ''
  name: subType
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: timestamp
  type: integer
- container: ''
  name: userName
  type: string
- container: set
  name: users
  type: string
- container: ''
  name: xdrUrl
  type: string
property_count: 57
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cortex-xsiam-api-context
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
