---
class_count: 2
classes:
- FilterGroup
- Filter
context_file: json-ld/hubspot-engagement-notes-filter-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-engagement-notes-filter-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Engagement Notes Filter from HubSpot.
layout: jsonld
name: Hubspot Engagement Notes Filter Context
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
- container: set
  name: values
  type: string
- container: ''
  name: highValue
  type: string
property_count: 6
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-engagement-notes-filter-context
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
