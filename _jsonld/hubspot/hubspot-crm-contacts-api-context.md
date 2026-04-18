---
class_count: 14
classes:
- Contact
- CollectionResponseContact
- BatchResponseContact
- SimplePublicObjectInput
- BatchReadInput
- BatchCreateInput
- BatchUpdateInput
- BatchArchiveInput
- SearchRequest
- FilterGroup
- Filter
- Association
- CollectionResponseAssociation
- Paging
context_file: json-ld/hubspot-crm-contacts-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-crm-contacts-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Crm Contacts Api from HubSpot.
layout: jsonld
name: Hubspot Crm Contacts Api Context
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
  name: properties
  type: reference
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: archived
  type: boolean
- container: ''
  name: associations
  type: reference
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: completedAt
  type: dateTime
- container: set
  name: inputs
  type: reference
- container: set
  name: filterGroups
  type: reference
- container: set
  name: sorts
  type: reference
- container: ''
  name: query
  type: string
- container: ''
  name: limit
  type: integer
- container: ''
  name: after
  type: string
- container: set
  name: filters
  type: reference
- container: ''
  name: propertyName
  type: string
- container: ''
  name: operator
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: next
  type: reference
property_count: 22
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-crm-contacts-api-context
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
