---
class_count: 6
classes:
- AgentScore
- ApplicationScore
- MonitoredAgent
- MonitoredApplication
- PerformanceMetric
- TestResult
context_file: json-ld/palo-alto-autonomous-dem-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-autonomous-dem-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Autonomous Dem Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Autonomous Dem Api Context
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
  name: agentId
  type: string
- container: ''
  name: agentVersion
  type: string
- container: ''
  name: appId
  type: string
- container: ''
  name: application
  type: string
- container: ''
  name: applicationScore
  type: integer
- container: ''
  name: category
  type: string
- container: ''
  name: cpuUsagePct
  type: decimal
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: deviceName
  type: string
- container: ''
  name: dnsTimeMs
  type: decimal
- container: ''
  name: endpointScore
  type: integer
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: httpStatusCode
  type: integer
- container: ''
  name: jitterMs
  type: decimal
- container: ''
  name: lastSeen
  type: dateTime
- container: ''
  name: latencyMs
  type: decimal
- container: ''
  name: memoryUsagePct
  type: decimal
- container: ''
  name: metricType
  type: string
- container: ''
  name: monitoredUsers
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: networkScore
  type: integer
- container: ''
  name: os
  type: string
- container: ''
  name: osVersion
  type: string
- container: ''
  name: overallScore
  type: integer
- container: ''
  name: packetLossPct
  type: decimal
- container: ''
  name: sampleCount
  type: integer
- container: ''
  name: segment
  type: string
- container: ''
  name: siteName
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: tcpConnectMs
  type: decimal
- container: ''
  name: testCount
  type: integer
- container: ''
  name: testId
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: ttfbMs
  type: decimal
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: url
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: value
  type: decimal
property_count: 39
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-autonomous-dem-api-context
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
