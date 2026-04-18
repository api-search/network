---
class_count: 7
classes:
- CRMAccount
- CRMContact
- Lead
- Opportunity
- Engagement
- Note
- Stage
context_file: json-ld/merge-crm-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/json-ld/merge-crm-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Merge Crm Api from Merge.
layout: jsonld
name: Merge Crm Api Context
namespaces:
- prefix: merge
  uri: https://api.merge.dev/schema/
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
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: industry
  type: string
- container: ''
  name: website
  type: reference
- container: ''
  name: numberOfEmployees
  type: integer
- container: ''
  name: owner
  type: reference
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: account
  type: reference
- container: ''
  name: leadSource
  type: string
- container: ''
  name: amount
  type: integer
- container: ''
  name: stage
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: closeDate
  type: dateTime
- container: ''
  name: content
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: lastActivityAt
  type: dateTime
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: remoteWasDeleted
  type: boolean
property_count: 22
provider_name: Merge
provider_slug: merge
slug: merge-crm-api-context
tags:
- Integrations
- Platform
- Unified API
- JSON-LD
- Linked Data
- Semantic Web
---
