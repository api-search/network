---
class_count: 15
classes:
- Activity
- ActivityList
- OfferList
- DeliveryRequest
- Offer
- OfferInput
- PropertyList
- AudienceList
- Audience
- AudienceInput
- EnvironmentList
- DeliveryResponse
- ActivityInput
- name
- description
context_file: json-ld/adobe-experience-cloud-target-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/json-ld/adobe-experience-cloud-target-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Experience Cloud Target Api from Adobe Experience Cloud.
layout: jsonld
name: Adobe Experience Cloud Target Api Context
namespaces:
- prefix: aec
  uri: https://developer.adobe.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: priority
  type: integer
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: startsAt
  type: dateTime
- container: ''
  name: endsAt
  type: dateTime
- container: ''
  name: total
  type: integer
- container: ''
  name: offset
  type: integer
- container: ''
  name: limit
  type: integer
- container: set
  name: activities
  type: string
- container: set
  name: offers
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: context
  type: reference
- container: ''
  name: channel
  type: string
- container: ''
  name: userAgent
  type: string
- container: ''
  name: execute
  type: reference
- container: set
  name: mboxes
  type: string
- container: ''
  name: index
  type: integer
- container: ''
  name: prefetch
  type: reference
- container: set
  name: views
  type: string
- container: set
  name: properties
  type: string
- container: ''
  name: token
  type: string
- container: set
  name: audiences
  type: string
- container: ''
  name: targetRule
  type: reference
- container: set
  name: environments
  type: string
- container: ''
  name: requestId
  type: string
- container: set
  name: options
  type: string
property_count: 28
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
slug: adobe-experience-cloud-target-api-context
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
- JSON-LD
- Linked Data
- Semantic Web
---
