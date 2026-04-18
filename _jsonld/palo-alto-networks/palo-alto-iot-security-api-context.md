---
class_count: 6
classes:
- Alert
- AssetReport
- Device
- DeviceTag
- PolicyRecommendation
- Vulnerability
context_file: json-ld/palo-alto-iot-security-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-iot-security-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Iot Security Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Iot Security Api Context
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
  name: affectedDeviceCount
  type: integer
- container: set
  name: applications
  type: string
- container: ''
  name: byCategory
  type: reference
- container: ''
  name: byRiskLevel
  type: reference
- container: set
  name: bySite
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: confidence
  type: float
- container: ''
  name: confidenceScore
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: critical
  type: integer
- container: ''
  name: cve
  type: string
- container: ''
  name: cvssScore
  type: float
- container: ''
  name: description
  type: string
- container: ''
  name: destinationZone
  type: string
- container: ''
  name: details
  type: reference
- container: ''
  name: deviceCount
  type: integer
- container: ''
  name: deviceIp
  type: string
- container: ''
  name: deviceProfile
  type: string
- container: ''
  name: deviceid
  type: string
- container: ''
  name: firstDetected
  type: dateTime
- container: ''
  name: firstSeen
  type: dateTime
- container: ''
  name: high
  type: integer
- container: ''
  name: hostname
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: ip
  type: string
- container: ''
  name: lastSeen
  type: dateTime
- container: ''
  name: low
  type: integer
- container: ''
  name: mac
  type: string
- container: ''
  name: medium
  type: integer
- container: ''
  name: model
  type: string
- container: ''
  name: monitored
  type: string
- container: ''
  name: monitoredDevices
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: os
  type: string
- container: ''
  name: osVersion
  type: string
- container: ''
  name: profile
  type: string
- container: ''
  name: remediation
  type: string
- container: ''
  name: reportTime
  type: dateTime
- container: ''
  name: resolved
  type: string
- container: ''
  name: resolvedReason
  type: string
- container: ''
  name: riskScore
  type: integer
- container: set
  name: services
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: site
  type: string
- container: ''
  name: sourceZone
  type: string
- container: ''
  name: subnet
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: set
  name: topProfiles
  type: reference
- container: ''
  name: totalDevices
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: vendor
  type: string
- container: ''
  name: vulnerabilityName
  type: string
property_count: 54
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-iot-security-api-context
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
