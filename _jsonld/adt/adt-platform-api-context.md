---
class_count: 19
classes:
- ArmRequest
- System
- DeviceList
- AccessCode
- VideoClipList
- AutomationList
- Event
- EventList
- VideoClip
- AccessCodeList
- Device
- Automation
- SystemList
- DisarmRequest
- SystemStatusResponse
- AccessCodeInput
- name
- address
- description
context_file: json-ld/adt-platform-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adt/refs/heads/main/json-ld/adt-platform-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adt Platform Api from ADT.
layout: jsonld
name: Adt Platform Api Context
namespaces:
- prefix: adt
  uri: https://api.adt.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: mode
  type: string
- container: ''
  name: accessCode
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: lastModified
  type: dateTime
- container: set
  name: devices
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: set
  name: permissions
  type: string
- container: set
  name: clips
  type: string
- container: set
  name: automations
  type: string
- container: ''
  name: deviceId
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: userId
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: total
  type: integer
- container: ''
  name: cameraId
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: trigger
  type: string
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: thumbnailUrl
  type: reference
- container: set
  name: accessCodes
  type: string
- container: ''
  name: zone
  type: string
- container: ''
  name: batteryLevel
  type: integer
- container: ''
  name: lastActivity
  type: dateTime
- container: ''
  name: enabled
  type: boolean
- container: set
  name: actions
  type: string
- container: set
  name: systems
  type: string
- container: ''
  name: systemId
  type: string
- container: ''
  name: code
  type: string
property_count: 31
provider_name: ADT
provider_slug: adt
slug: adt-platform-api-context
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
- JSON-LD
- Linked Data
- Semantic Web
---
