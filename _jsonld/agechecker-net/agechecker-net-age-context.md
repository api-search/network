---
class_count: 8
classes:
- VerificationResponse
- Session
- createdAt
- VerificationRequest
- email
- SessionList
- WebhookConfig
- url
context_file: json-ld/agechecker-net-age-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-ld/agechecker-net-age-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agechecker Net Age from AgeChecker.Net.
layout: jsonld
name: Agechecker Net Age Context
namespaces:
- prefix: agechecker-net
  uri: https://agechecker-net.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: result
  type: string
- container: ''
  name: sessionId
  type: string
- container: ''
  name: requiresPhotoId
  type: boolean
- container: ''
  name: ageVerified
  type: boolean
- container: ''
  name: minimumAge
  type: integer
- container: ''
  name: redirectUrl
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: birthDate
  type: date
- container: ''
  name: address
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: zip
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: phone
  type: string
- container: ''
  name: ipAddress
  type: string
- container: set
  name: sessions
  type: string
- container: ''
  name: total
  type: integer
- container: ''
  name: limit
  type: integer
- container: ''
  name: offset
  type: integer
- container: ''
  name: id
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: secret
  type: string
property_count: 25
provider_name: AgeChecker.Net
provider_slug: agechecker-net
slug: agechecker-net-age-context
tags:
- Age Verification
- Identity
- Compliance
- Regulatory
- E-Commerce
- JSON-LD
- Linked Data
- Semantic Web
---
