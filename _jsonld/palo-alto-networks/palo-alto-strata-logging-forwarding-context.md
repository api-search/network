---
class_count: 5
classes:
- AuthLogPayload
- ThreatLogPayload
- TrafficLogPayload
- UrlLogPayload
- WildfireLogPayload
context_file: json-ld/palo-alto-strata-logging-forwarding-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-strata-logging-forwarding-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Strata Logging Forwarding from Palo Alto Networks.
layout: jsonld
name: Palo Alto Strata Logging Forwarding Context
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
  name: app
  type: string
- container: ''
  name: authMethod
  type: string
- container: ''
  name: authProfile
  type: string
- container: ''
  name: authResult
  type: string
- container: ''
  name: authSource
  type: string
- container: ''
  name: bytesReceived
  type: integer
- container: ''
  name: bytesSent
  type: integer
- container: ''
  name: contentType
  type: string
- container: ''
  name: deviceName
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: dport
  type: integer
- container: ''
  name: dst
  type: string
- container: ''
  name: dstUser
  type: string
- container: ''
  name: dstZone
  type: string
- container: ''
  name: fileHash
  type: string
- container: ''
  name: fileSize
  type: integer
- container: ''
  name: filename
  type: string
- container: ''
  name: filetype
  type: string
- container: ''
  name: httpMethod
  type: string
- container: ''
  name: logForwardingProfile
  type: string
- container: ''
  name: mfaResult
  type: string
- container: ''
  name: mfaVendor
  type: string
- container: ''
  name: natDport
  type: integer
- container: ''
  name: natDst
  type: string
- container: ''
  name: natSport
  type: integer
- container: ''
  name: natSrc
  type: string
- container: ''
  name: outputFormat
  type: string
- container: ''
  name: packetsReceived
  type: integer
- container: ''
  name: packetsSent
  type: integer
- container: ''
  name: proto
  type: string
- container: ''
  name: receiveTime
  type: dateTime
- container: ''
  name: reportUrl
  type: reference
- container: ''
  name: ruleName
  type: string
- container: ''
  name: serial
  type: string
- container: ''
  name: sessionDuration
  type: integer
- container: ''
  name: sessionId
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: sport
  type: integer
- container: ''
  name: src
  type: string
- container: ''
  name: srcUser
  type: string
- container: ''
  name: srcZone
  type: string
- container: ''
  name: subtype
  type: string
- container: ''
  name: threatId
  type: string
- container: ''
  name: threatName
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: url
  type: string
- container: ''
  name: urlCategory
  type: string
- container: ''
  name: urlOrFilename
  type: string
- container: ''
  name: verdict
  type: string
- container: ''
  name: vsys
  type: string
property_count: 51
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-strata-logging-forwarding-context
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
