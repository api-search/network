---
class_count: 5
classes:
- Page
- CollectionResponsePage
- PageCreateRequest
- PageUpdateRequest
- Paging
context_file: json-ld/hubspot-cms-pages-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-cms-pages-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Cms Pages Api from HubSpot.
layout: jsonld
name: Hubspot Cms Pages Api Context
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
  name: htmlTitle
  type: string
- container: ''
  name: slug
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: currentState
  type: string
- container: ''
  name: contentTypeCategory
  type: integer
- container: ''
  name: publishDate
  type: dateTime
- container: ''
  name: metaDescription
  type: string
- container: ''
  name: url
  type: ''
- container: ''
  name: domain
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: templatePath
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: archived
  type: boolean
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: layoutSections
  type: reference
- container: ''
  name: next
  type: reference
property_count: 20
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-cms-pages-api-context
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
