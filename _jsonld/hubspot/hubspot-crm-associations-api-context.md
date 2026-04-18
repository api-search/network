---
class_count: 19
classes:
- Association
- AssociationType
- AssociationDefinition
- AssociationLabel
- CreateAssociationInput
- ObjectReference
- AssociationTypeInput
- BatchAssociationReadInput
- BatchAssociationCreateInput
- BatchAssociationCreateItem
- BatchAssociationArchiveInput
- BatchAssociationArchiveItem
- CreateLabelInput
- AssociationResult
- BatchAssociationResponse
- PagingNext
- Paging
- AssociationDefinitionCollection
- AssociationLabelCollection
context_file: json-ld/hubspot-crm-associations-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-crm-associations-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Crm Associations Api from HubSpot.
layout: jsonld
name: Hubspot Crm Associations Api Context
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
  name: toObjectId
  type: string
- container: set
  name: associationTypes
  type: reference
- container: ''
  name: associationCategory
  type: string
- container: ''
  name: associationTypeId
  type: integer
- container: ''
  name: label
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: fromObjectTypeId
  type: string
- container: ''
  name: toObjectTypeId
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: inverseLabel
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: typeId
  type: integer
- container: ''
  name: to
  type: reference
- container: set
  name: types
  type: reference
- container: set
  name: inputs
  type: reference
- container: ''
  name: from
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: status
  type: string
- container: set
  name: results
  type: reference
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
  name: numErrors
  type: integer
- container: set
  name: errors
  type: reference
- container: ''
  name: links
  type: reference
- container: ''
  name: after
  type: string
- container: ''
  name: link
  type: string
- container: ''
  name: next
  type: reference
property_count: 28
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-crm-associations-api-context
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
