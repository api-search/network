---
class_count: 3
classes:
- EmailAttachment
- EmailDLPIncident
- EmailRecipient
context_file: json-ld/palo-alto-email-dlp-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-email-dlp-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Email Dlp Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Email Dlp Api Context
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
  name: attachmentCount
  type: integer
- container: ''
  name: category
  type: string
- container: ''
  name: comment
  type: string
- container: ''
  name: contentType
  type: string
- container: set
  name: dataPatterns
  type: reference
- container: ''
  name: deliveryStatus
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: filename
  type: string
- container: ''
  name: hasAttachments
  type: boolean
- container: ''
  name: hasMatches
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: matchCount
  type: integer
- container: ''
  name: name
  type: string
- container: set
  name: patternsMatched
  type: string
- container: ''
  name: reviewedAt
  type: dateTime
- container: ''
  name: reviewedBy
  type: string
- container: ''
  name: sender
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: type
  type: string
property_count: 25
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-email-dlp-api-context
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
