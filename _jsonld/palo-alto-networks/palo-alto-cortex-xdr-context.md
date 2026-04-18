---
class_count: 1
classes:
- Cortex XDR Incident
context_file: json-ld/palo-alto-cortex-xdr-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xdr-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cortex Xdr from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cortex Xdr Context
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
  name: alertCount
  type: integer
- container: set
  name: alertSources
  type: string
- container: ''
  name: assignedUserMail
  type: string
- container: ''
  name: assignedUserPrettyName
  type: string
- container: ''
  name: creationTime
  type: integer
- container: ''
  name: description
  type: string
- container: set
  name: fileArtifacts
  type: ''
- container: ''
  name: fileName
  type: string
- container: ''
  name: filePath
  type: string
- container: ''
  name: fileSha256
  type: string
- container: ''
  name: fileSignatureStatus
  type: string
- container: ''
  name: highSeverityAlertCount
  type: integer
- container: ''
  name: hostCount
  type: integer
- container: ''
  name: incidentId
  type: string
- container: ''
  name: incidentName
  type: string
- container: ''
  name: isManual
  type: boolean
- container: ''
  name: lowSeverityAlertCount
  type: integer
- container: ''
  name: medSeverityAlertCount
  type: integer
- container: ''
  name: modificationTime
  type: integer
- container: set
  name: networkArtifacts
  type: ''
- container: ''
  name: networkCountry
  type: string
- container: ''
  name: networkDomain
  type: string
- container: ''
  name: networkRemoteIp
  type: string
- container: ''
  name: networkRemotePort
  type: integer
- container: ''
  name: notes
  type: string
- container: ''
  name: resolveComment
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: userCount
  type: integer
- container: ''
  name: wildfireVerdict
  type: string
- container: ''
  name: xdrUrl
  type: reference
property_count: 32
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cortex-xdr-context
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
