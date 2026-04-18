---
class_count: 7
classes:
- AccessPolicy
- AccessPolicyRequest
- Role
- ServiceAccount
- ServiceAccountCredentials
- ServiceAccountRequest
- ServiceAccountUpdate
context_file: json-ld/palo-alto-sase-iam-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-iam-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase Iam Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase Iam Api Context
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
  name: clientId
  type: string
- container: ''
  name: clientSecret
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: description
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: id
  type: string
- container: ''
  name: keyCount
  type: integer
- container: ''
  name: keyId
  type: string
- container: ''
  name: name
  type: string
- container: set
  name: permissions
  type: string
- container: ''
  name: principalId
  type: string
- container: ''
  name: principalType
  type: string
- container: ''
  name: roleId
  type: string
- container: ''
  name: roleName
  type: string
- container: ''
  name: tsgId
  type: string
- container: ''
  name: updatedAt
  type: dateTime
property_count: 17
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-iam-api-context
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
