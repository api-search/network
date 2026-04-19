---
class_count: 0
classes: []
context_file: json-ld/analytics-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/analytics/refs/heads/main/json-ld/analytics-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Analytics from Analytics.
layout: jsonld
name: Analytics Context
namespaces:
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
- prefix: analytics
  uri: https://raw.githubusercontent.com/api-evangelist/analytics/refs/heads/main/vocabulary/
properties:
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: slug
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: deployment
  type: string
- container: ''
  name: license
  type: string
- container: ''
  name: website
  type: reference
- container: ''
  name: apiReference
  type: reference
- container: set
  name: sdks
  type: ''
- container: ''
  name: dataCollection
  type: reference
- container: ''
  name: privacy
  type: reference
- container: set
  name: integrations
  type: ''
- container: ''
  name: pricing
  type: reference
- container: set
  name: tags
  type: ''
- container: ''
  name: events
  type: boolean
- container: ''
  name: pageviews
  type: boolean
- container: ''
  name: sessions
  type: boolean
- container: ''
  name: userIdentification
  type: boolean
- container: ''
  name: customProperties
  type: boolean
- container: ''
  name: gdprCompliant
  type: boolean
- container: ''
  name: ccpaCompliant
  type: boolean
- container: ''
  name: cookieless
  type: boolean
- container: set
  name: dataResidency
  type: ''
- container: ''
  name: model
  type: string
- container: ''
  name: freeEvents
  type: integer
property_count: 25
provider_name: Analytics
provider_slug: analytics
slug: analytics-context
tags:
- Analytics
- Business Intelligence
- Customer Data Platform
- Data Pipeline
- Event Tracking
- Mobile Analytics
- Observability
- Product Analytics
- Real-Time Analytics
- Web Analytics
- JSON-LD
- Linked Data
- Semantic Web
---
