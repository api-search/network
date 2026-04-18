---
class_count: 8
classes:
- List
- CollectionResponseList
- ListCreateRequest
- Membership
- CollectionResponseMembership
- MembershipChangeRequest
- MembershipChangeResponse
- Paging
context_file: json-ld/hubspot-crm-lists-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-crm-lists-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Crm Lists Api from HubSpot.
layout: jsonld
name: Hubspot Crm Lists Api Context
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
  name: listId
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: listType
  type: string
- container: ''
  name: objectTypeId
  type: string
- container: ''
  name: processingStatus
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: filterBranch
  type: reference
- container: ''
  name: memberCount
  type: integer
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: processingType
  type: string
- container: ''
  name: recordId
  type: string
- container: ''
  name: addedAt
  type: dateTime
- container: set
  name: recordIdsToAdd
  type: string
- container: set
  name: recordIdsToRemove
  type: string
- container: set
  name: recordIdsAdded
  type: string
- container: set
  name: recordIdsAlreadyMember
  type: string
- container: set
  name: recordIdsRemoved
  type: string
- container: set
  name: recordIdsMissing
  type: string
- container: ''
  name: next
  type: reference
property_count: 21
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-crm-lists-api-context
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
