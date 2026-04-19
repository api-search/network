---
class_count: 8
classes:
- ScimGroup
- ScimUser
- ScimGroupRequest
- ScimUserRequest
- ScimGroupListResponse
- ScimPatchRequest
- ScimUserListResponse
- name
context_file: json-ld/amplitude-scim-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-scim-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Scim Api from Amplitude.
layout: jsonld
name: Amplitude Scim Api Context
namespaces:
- prefix: amplitude
  uri: https://amplitude.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: schemas
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: displayName
  type: string
- container: set
  name: members
  type: reference
- container: ''
  name: value
  type: string
- container: ''
  name: display
  type: string
- container: ''
  name: meta
  type: reference
- container: ''
  name: resourceType
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: lastModified
  type: dateTime
- container: ''
  name: userName
  type: string
- container: ''
  name: givenName
  type: string
- container: ''
  name: familyName
  type: string
- container: set
  name: emails
  type: reference
- container: ''
  name: primary
  type: boolean
- container: ''
  name: type
  type: string
- container: ''
  name: active
  type: boolean
- container: set
  name: groups
  type: reference
- container: ''
  name: totalResults
  type: integer
- container: set
  name: Resources
  type: reference
- container: set
  name: Operations
  type: reference
- container: ''
  name: op
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: startIndex
  type: integer
- container: ''
  name: itemsPerPage
  type: integer
property_count: 25
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-scim-api-context
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
- JSON-LD
- Linked Data
- Semantic Web
---
