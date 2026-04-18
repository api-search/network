---
class_count: 8
classes:
- BatchNotesResponse
- BatchError
- BatchCreateNotesRequest
- BatchReadNotesRequest
- BatchReadInput
- BatchUpdateNotesRequest
- BatchUpdateInput
- BatchArchiveNotesRequest
context_file: json-ld/hubspot-engagement-notes-batch-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-engagement-notes-batch-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Engagement Notes Batch from HubSpot.
layout: jsonld
name: Hubspot Engagement Notes Batch Context
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
  name: inputs
  type: reference
- container: set
  name: properties
  type: string
- container: set
  name: propertiesWithHistory
  type: string
- container: ''
  name: idProperty
  type: string
- container: ''
  name: id
  type: string
property_count: 15
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-engagement-notes-batch-context
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
