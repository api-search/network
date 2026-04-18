---
class_count: 2
classes:
- UserDeletionId
- UserDeletionRequest
context_file: json-ld/google-analytics-user-deletion-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/json-ld/google-analytics-user-deletion-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Google Analytics User Deletion Api from Google Analytics.
layout: jsonld
name: Google Analytics User Deletion Api Context
namespaces:
- prefix: ga
  uri: https://developers.google.com/analytics/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: deletionRequestTime
  type: dateTime
- container: ''
  name: firebaseProjectId
  type: string
- container: ''
  name: id
  type: reference
- container: ''
  name: kind
  type: string
- container: ''
  name: propertyId
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: webPropertyId
  type: string
property_count: 8
provider_name: Google Analytics
provider_slug: google-analytics
slug: google-analytics-user-deletion-api-context
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
- JSON-LD
- Linked Data
- Semantic Web
---
