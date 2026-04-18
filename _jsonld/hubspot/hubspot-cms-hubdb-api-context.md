---
class_count: 8
classes:
- HubDBTable
- HubDBColumn
- HubDBTableCreateRequest
- HubDBRow
- HubDBRowCreateRequest
- CollectionResponseHubDBTable
- CollectionResponseHubDBRow
- Paging
context_file: json-ld/hubspot-cms-hubdb-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-cms-hubdb-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Cms Hubdb Api from HubSpot.
layout: jsonld
name: Hubspot Cms Hubdb Api Context
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
  name: label
  type: string
- container: set
  name: columns
  type: reference
- container: ''
  name: published
  type: boolean
- container: ''
  name: rowCount
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: publishedAt
  type: dateTime
- container: ''
  name: type
  type: string
- container: set
  name: options
  type: reference
- container: ''
  name: values
  type: reference
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: next
  type: reference
property_count: 15
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-cms-hubdb-api-context
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
