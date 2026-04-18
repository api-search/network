---
class_count: 63
classes:
- Organization
- SecurityAdvisory
- ThreatSignature
- SecurityPolicy
- SecurityAlert
- SecurityIncident
- MalwareAnalysis
- CloudResource
- NetworkDevice
- IoTDevice
- Vulnerability
- ComplianceViolation
- AttackSurfaceAsset
- AISecurityScan
- name
- description
- datePublished
- dateModified
- severity
- status
- category
- cvssScore
- affectedProduct
- fixedVersion
- signatureId
- signatureType
- threatName
- action
- verdict
- sha256
- md5
- filetype
- malwareFamily
- alertId
- incidentId
- assignedTo
- alertCount
- detectionSource
- sourceAddress
- destinationAddress
- sourceZone
- destinationZone
- application
- ruleAction
- cloudType
- resourceId
- resourceType
- region
- accountId
- complianceStandard
- deviceIp
- deviceMac
- deviceProfile
- riskScore
- assetType
- ipRanges
- domain
- certificate
- exposureLevel
- prompt
- modelResponse
- aiThreatType
- confidence
context_file: json-ld/palo-alto-networks-security-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-networks-security-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Networks Security from Palo Alto Networks.
layout: jsonld
name: Palo Alto Networks Security Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: stix
  uri: https://docs.oasis-open.org/cti/stix/v2.1/
- prefix: cve
  uri: https://cve.mitre.org/cgi-bin/cvename.cgi?name=
properties:
- container: ''
  name: url
  type: reference
- container: ''
  name: cveId
  type: reference
- container: ''
  name: relatedThreat
  type: reference
- container: ''
  name: mitigatedBy
  type: reference
- container: ''
  name: detectedBy
  type: reference
- container: ''
  name: affectsResource
  type: reference
property_count: 6
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-networks-security-context
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
