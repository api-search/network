---
class_count: 15
classes:
- BlogAuthor
- BlogAuthorInput
- BlogAuthorCollection
- BatchInputItem
- BatchInput
- BatchReadInput
- BatchCreateInput
- BatchArchiveInput
- BatchResponse
- DetachFromLanguageGroupRequest
- SetLanguagePrimaryRequest
- AttachToLanguageGroupRequest
- CreateLanguageVariationRequest
- Paging
- PagingNext
context_file: json-ld/hubspot-authors-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-authors-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Authors Api from HubSpot.
layout: jsonld
name: Hubspot Authors Api Context
namespaces:
- prefix: hubspot
  uri: https://developers.hubspot.com/schema/
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
  type: ''
- container: ''
  name: slug
  type: string
- container: ''
  name: email
  type: ''
- container: ''
  name: bio
  type: string
- container: ''
  name: website
  type: reference
- container: ''
  name: twitter
  type: string
- container: ''
  name: facebook
  type: string
- container: ''
  name: linkedin
  type: string
- container: ''
  name: avatar
  type: reference
- container: ''
  name: language
  type: string
- container: ''
  name: translatedFromId
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: updated
  type: dateTime
- container: ''
  name: deletedAt
  type: dateTime
- container: ''
  name: total
  type: integer
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: properties
  type: reference
- container: set
  name: inputs
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: requestedAt
  type: dateTime
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: links
  type: reference
- container: ''
  name: primaryId
  type: string
- container: ''
  name: primaryLanguage
  type: string
- container: ''
  name: next
  type: reference
- container: ''
  name: after
  type: string
- container: ''
  name: link
  type: string
property_count: 30
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-authors-api-context
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
- JSON-LD
- Linked Data
- Semantic Web
---
