---
class_count: 0
classes: []
context_file: json-ld/palo-alto-networks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-networks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Networks from Palo Alto Networks.
layout: jsonld
name: Palo Alto Networks Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: sec
  uri: https://w3id.org/security#
- prefix: owl
  uri: http://www.w3.org/2002/07/owl#
- prefix: skos
  uri: http://www.w3.org/2004/02/skos/core#
properties:
- container: ''
  name: SecurityIncident
  type: reference
- container: ''
  name: FirewallPolicy
  type: reference
- container: ''
  name: ThreatSignature
  type: reference
- container: ''
  name: NetworkDevice
  type: reference
- container: ''
  name: VulnerabilityAssessment
  type: reference
- container: ''
  name: CloudAccount
  type: reference
- container: ''
  name: SecurityAlert
  type: reference
- container: ''
  name: DataLossEvent
  type: reference
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: identifier
  type: string
- container: ''
  name: url
  type: reference
- container: ''
  name: datePublished
  type: dateTime
- container: ''
  name: dateModified
  type: dateTime
- container: ''
  name: dateCreated
  type: dateTime
- container: ''
  name: creator
  type: reference
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: incidentId
  type: string
- container: ''
  name: alertId
  type: string
- container: ''
  name: alertCount
  type: integer
- container: ''
  name: alertSources
  type: string
- container: ''
  name: assignedTo
  type: string
- container: ''
  name: detectionSource
  type: string
- container: ''
  name: resolutionComment
  type: string
- container: ''
  name: policyId
  type: string
- container: ''
  name: policyName
  type: string
- container: ''
  name: policyType
  type: string
- container: ''
  name: sourceZone
  type: string
- container: ''
  name: destinationZone
  type: string
- container: ''
  name: sourceAddress
  type: string
- container: ''
  name: destinationAddress
  type: string
- container: ''
  name: application
  type: string
- container: ''
  name: ruleAction
  type: string
- container: ''
  name: signatureId
  type: string
- container: ''
  name: signatureType
  type: string
- container: ''
  name: threatName
  type: string
- container: ''
  name: threatId
  type: string
- container: ''
  name: verdict
  type: string
- container: ''
  name: sha256
  type: string
- container: ''
  name: malwareFamily
  type: string
- container: ''
  name: serialNumber
  type: string
- container: ''
  name: deviceName
  type: string
- container: ''
  name: deviceModel
  type: string
- container: ''
  name: deviceIp
  type: string
- container: ''
  name: softwareVersion
  type: string
- container: ''
  name: cveId
  type: string
- container: ''
  name: cvssScore
  type: decimal
- container: ''
  name: cvssVector
  type: string
- container: ''
  name: affectedProduct
  type: reference
- container: ''
  name: fixedVersion
  type: string
- container: ''
  name: exploitStatus
  type: string
- container: ''
  name: cloudType
  type: string
- container: ''
  name: accountId
  type: string
- container: ''
  name: accountName
  type: string
- container: ''
  name: resourceId
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: complianceStandard
  type: string
- container: ''
  name: dataClassification
  type: string
- container: ''
  name: exposureType
  type: string
- container: ''
  name: dataStore
  type: string
- container: ''
  name: relatedIncident
  type: reference
- container: ''
  name: relatedAlert
  type: reference
- container: ''
  name: relatedPolicy
  type: reference
- container: ''
  name: affectsResource
  type: reference
- container: ''
  name: detectedBy
  type: reference
- container: ''
  name: mitigatedBy
  type: reference
- container: ''
  name: partOf
  type: reference
- container: ''
  name: enforcedBy
  type: reference
property_count: 72
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-networks-context
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
