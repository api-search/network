---
class_count: 13
classes:
- AuditEventResponse
- AuditEvent
- EventClient
- EventLocation
- EventRequest
- EventUser
- ItemUsageResponse
- ItemUsage
- SignInAttemptResponse
- SignInAttempt
- TokenIntrospection
- email
- name
context_file: json-ld/1password-events-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/json-ld/1password-events-context.jsonld
description: JSON-LD context defining the semantic vocabulary for 1Password Events from 1Password.
layout: jsonld
name: 1Password Events Context
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
  name: action
  type: string
- container: ''
  name: actorDetails
  type: string
- container: ''
  name: actorUuid
  type: string
- container: ''
  name: appName
  type: string
- container: ''
  name: appVersion
  type: string
- container: ''
  name: auxDetails
  type: reference
- container: ''
  name: auxId
  type: integer
- container: ''
  name: auxInfo
  type: string
- container: ''
  name: auxUuid
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: client
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: cursor
  type: string
- container: ''
  name: deviceUuid
  type: string
- container: set
  name: features
  type: string
- container: ''
  name: hasMore
  type: boolean
- container: ''
  name: ip
  type: string
- container: ''
  name: itemUuid
  type: string
- container: set
  name: items
  type: string
- container: ''
  name: latitude
  type: decimal
- container: ''
  name: limit
  type: integer
- container: ''
  name: location
  type: string
- container: ''
  name: loginTime
  type: dateTime
- container: ''
  name: longitude
  type: decimal
- container: ''
  name: objectDetails
  type: reference
- container: ''
  name: objectType
  type: string
- container: ''
  name: objectUuid
  type: string
- container: ''
  name: osName
  type: string
- container: ''
  name: osVersion
  type: string
- container: ''
  name: platformName
  type: string
- container: ''
  name: platformVersion
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: session
  type: reference
- container: ''
  name: sessionUuid
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: targetUser
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: type
  type: string
- container: ''
  name: usedVersion
  type: integer
- container: ''
  name: user
  type: string
- container: ''
  name: uuid
  type: string
- container: ''
  name: vaultUuid
  type: string
property_count: 43
provider_name: 1Password
provider_slug: 1password
slug: 1password-events-context
tags:
- Password Manager
- Passwords
- Security
- Secrets
- JSON-LD
- Linked Data
- Semantic Web
---
