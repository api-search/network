---
class_count: 8
classes:
- BrowserDeployment
- BrowserDeploymentRequest
- BrowserPolicy
- BrowserPolicyRequest
- BrowserSession
- BrowserUser
- ManagedDevice
- UsageReport
context_file: json-ld/palo-alto-prisma-access-browser-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-access-browser-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Access Browser Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Access Browser Api Context
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
  name: activeSessions
  type: integer
- container: ''
  name: activeUsers
  type: integer
- container: set
  name: blockedCategories
  type: string
- container: ''
  name: browserVersion
  type: string
- container: ''
  name: complianceStatus
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: set
  name: dataPoints
  type: reference
- container: ''
  name: dataTransferredGb
  type: float
- container: ''
  name: deploymentId
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: deviceCount
  type: integer
- container: ''
  name: deviceId
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: dlpEnabled
  type: boolean
- container: ''
  name: dlpEvents
  type: integer
- container: ''
  name: downloadControl
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: end
  type: date
- container: ''
  name: endedAt
  type: dateTime
- container: ''
  name: extensionPolicy
  type: string
- container: ''
  name: hostname
  type: string
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: lastActiveAt
  type: dateTime
- container: ''
  name: lastSeenAt
  type: dateTime
- container: ''
  name: name
  type: string
- container: ''
  name: period
  type: reference
- container: ''
  name: platform
  type: string
- container: ''
  name: policyId
  type: string
- container: ''
  name: sessionId
  type: string
- container: ''
  name: sessions
  type: integer
- container: ''
  name: start
  type: date
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: threatsBlocked
  type: integer
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: totalSessions
  type: integer
- container: ''
  name: updateChannel
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: userId
  type: string
- container: ''
  name: webFiltering
  type: reference
property_count: 41
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-access-browser-api-context
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
