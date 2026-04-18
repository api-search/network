---
class_count: 9
classes:
- ApiStats
- AtpReport
- AtpReportList
- ReleaseNote
- ReleaseNotesList
- ThreatHistoryEntry
- ThreatHistoryList
- ThreatList
- ThreatSignature
context_file: json-ld/palo-alto-threat-vault-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-threat-vault-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Threat Vault Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Threat Vault Api Context
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
  name: apiKey
  type: string
- container: set
  name: behaviors
  type: reference
- container: set
  name: connections
  type: reference
- container: ''
  name: count
  type: integer
- container: ''
  name: createTime
  type: dateTime
- container: set
  name: cve
  type: string
- container: ''
  name: data
  type: reference
- container: ''
  name: defaultAction
  type: string
- container: ''
  name: deprecatedSignatures
  type: integer
- container: ''
  name: description
  type: string
- container: set
  name: dnsQueries
  type: string
- container: ''
  name: dstIp
  type: string
- container: ''
  name: dstPort
  type: integer
- container: ''
  name: endpointUsage
  type: reference
- container: ''
  name: fileType
  type: string
- container: ''
  name: firstReleaseTime
  type: dateTime
- container: set
  name: httpRequests
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: latestReleaseTime
  type: dateTime
- container: ''
  name: latestReleaseVersion
  type: string
- container: ''
  name: limit
  type: integer
- container: ''
  name: maxVersion
  type: string
- container: ''
  name: minVersion
  type: string
- container: ''
  name: modifiedSignatures
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: network
  type: reference
- container: ''
  name: newSignatures
  type: integer
- container: ''
  name: notes
  type: string
- container: ''
  name: offset
  type: integer
- container: ''
  name: oriReleaseVersion
  type: string
- container: ''
  name: protocol
  type: string
- container: ''
  name: quota
  type: integer
- container: ''
  name: releaseDate
  type: date
- container: ''
  name: releaseTime
  type: dateTime
- container: ''
  name: remaining
  type: integer
- container: ''
  name: report
  type: reference
- container: ''
  name: resetTime
  type: dateTime
- container: ''
  name: severity
  type: string
- container: ''
  name: sha256
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: subtype
  type: string
- container: ''
  name: success
  type: boolean
- container: ''
  name: total
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: used
  type: integer
- container: ''
  name: verdict
  type: string
- container: ''
  name: version
  type: string
- container: set
  name: zingbox
  type: reference
property_count: 50
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-threat-vault-api-context
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
