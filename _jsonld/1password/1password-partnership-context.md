---
class_count: 4
classes:
- Account
- CreateAccountRequest
- UpdateAccountRequest
- createdAt
context_file: json-ld/1password-partnership-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/json-ld/1password-partnership-context.jsonld
description: JSON-LD context defining the semantic vocabulary for 1Password Partnership from 1Password.
layout: jsonld
name: 1Password Partnership Context
namespaces:
- prefix: onepassword
  uri: https://1password.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: accountType
  type: string
- container: ''
  name: accountUid
  type: string
- container: ''
  name: activationToken
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: endsAt
  type: dateTime
- container: ''
  name: status
  type: string
property_count: 6
provider_name: 1Password
provider_slug: 1password
slug: 1password-partnership-context
tags:
- Password Manager
- Passwords
- Security
- Secrets
- JSON-LD
- Linked Data
- Semantic Web
---
