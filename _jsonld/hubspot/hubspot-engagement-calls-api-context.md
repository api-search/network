---
class_count: 23
classes:
- Call
- PropertyHistory
- CallCollectionResponse
- CallSearchResponse
- BatchCallsResponse
- BatchError
- CallCreateRequest
- CallUpdateRequest
- BatchCreateCallsRequest
- BatchReadCallsRequest
- BatchReadInput
- BatchUpdateCallsRequest
- BatchUpdateInput
- BatchArchiveCallsRequest
- CallSearchRequest
- FilterGroup
- Filter
- SortOption
- AssociationInput
- AssociationType
- GdprDeleteRequest
- Paging
- NextPage
context_file: json-ld/hubspot-engagement-calls-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-engagement-calls-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Engagement Calls Api from HubSpot.
layout: jsonld
name: Hubspot Engagement Calls Api Context
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
  name: propertiesWithHistory
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
  name: archivedAt
  type: dateTime
- container: ''
  name: value
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: sourceType
  type: string
- container: ''
  name: sourceId
  type: string
- container: ''
  name: sourceLabel
  type: string
- container: ''
  name: updatedByUserId
  type: integer
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: total
  type: integer
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
- container: set
  name: errors
  type: reference
- container: ''
  name: links
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: context
  type: reference
- container: set
  name: associations
  type: reference
- container: set
  name: inputs
  type: reference
- container: ''
  name: idProperty
  type: string
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
- container: set
  name: values
  type: string
- container: ''
  name: highValue
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: to
  type: reference
- container: set
  name: types
  type: reference
- container: ''
  name: associationCategory
  type: string
- container: ''
  name: associationTypeId
  type: integer
- container: ''
  name: objectId
  type: string
- container: ''
  name: next
  type: reference
- container: ''
  name: link
  type: string
property_count: 46
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-engagement-calls-api-context
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
