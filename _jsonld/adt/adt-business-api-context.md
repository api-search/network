---
class_count: 11
classes:
- User
- UserList
- CredentialList
- Credential
- EventReport
- SiteList
- Site
- CredentialInput
- name
- email
- address
context_file: json-ld/adt-business-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adt/refs/heads/main/json-ld/adt-business-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adt Business Api from ADT.
layout: jsonld
name: Adt Business Api Context
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
  name: id
  type: string
- container: ''
  name: role
  type: string
- container: set
  name: users
  type: string
- container: set
  name: credentials
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: validFrom
  type: dateTime
- container: ''
  name: validTo
  type: dateTime
- container: ''
  name: siteId
  type: string
- container: ''
  name: period
  type: reference
- container: ''
  name: summary
  type: reference
- container: set
  name: events
  type: string
- container: set
  name: sites
  type: string
- container: ''
  name: total
  type: integer
- container: ''
  name: systemCount
  type: integer
- container: ''
  name: cardNumber
  type: string
property_count: 17
provider_name: ADT
provider_slug: adt
slug: adt-business-api-context
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
