---
class_count: 4
classes:
- ContentSnippet
- DLPIncident
- DataPattern
- IncidentSummary
context_file: json-ld/palo-alto-dlp-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-dlp-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Dlp Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Dlp Api Context
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
  name: actionTaken
  type: string
- container: ''
  name: application
  type: string
- container: ''
  name: byChannel
  type: reference
- container: ''
  name: bySeverity
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: confidence
  type: string
- container: ''
  name: critical
  type: integer
- container: ''
  name: dataPatternId
  type: string
- container: ''
  name: dataPatternName
  type: string
- container: ''
  name: description
  type: string
- container: set
  name: detectionRules
  type: reference
- container: ''
  name: direction
  type: string
- container: ''
  name: email
  type: integer
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: endpoint
  type: integer
- container: ''
  name: fileName
  type: string
- container: ''
  name: fileSize
  type: integer
- container: ''
  name: fileType
  type: string
- container: ''
  name: high
  type: integer
- container: ''
  name: id
  type: string
- container: ''
  name: incidentCount
  type: integer
- container: ''
  name: incidentId
  type: string
- container: ''
  name: informational
  type: integer
- container: ''
  name: low
  type: integer
- container: ''
  name: masked
  type: boolean
- container: ''
  name: matchCount
  type: integer
- container: ''
  name: medium
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: openIncidents
  type: integer
- container: ''
  name: patternId
  type: string
- container: ''
  name: patternName
  type: string
- container: ''
  name: position
  type: integer
- container: ''
  name: proximity
  type: integer
- container: ''
  name: reportingPeriod
  type: reference
- container: ''
  name: resolvedIncidents
  type: integer
- container: ''
  name: reviewedAt
  type: dateTime
- container: ''
  name: reviewedBy
  type: string
- container: ''
  name: reviewerComments
  type: string
- container: ''
  name: ruleType
  type: string
- container: ''
  name: saas
  type: integer
- container: ''
  name: severity
  type: string
- container: ''
  name: snippet
  type: string
- container: ''
  name: ssl
  type: integer
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: set
  name: topDataPatterns
  type: reference
- container: set
  name: topUsers
  type: reference
- container: ''
  name: totalIncidents
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: user
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: web
  type: integer
property_count: 55
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-dlp-api-context
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
