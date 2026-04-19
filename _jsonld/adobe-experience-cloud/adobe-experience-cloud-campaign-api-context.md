---
class_count: 14
classes:
- EmailList
- Service
- Email
- TransactionalMessageRequest
- TransactionalMessageResponse
- ServiceList
- ProfileList
- Profile
- WorkflowList
- ServiceInput
- ProfileInput
- Workflow
- name
- email
context_file: json-ld/adobe-experience-cloud-campaign-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/json-ld/adobe-experience-cloud-campaign-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Experience Cloud Campaign Api from Adobe Experience Cloud.
layout: jsonld
name: Adobe Experience Cloud Campaign Api Context
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
- container: set
  name: content
  type: string
- container: ''
  name: PKey
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: htmlContent
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: sender
  type: reference
- container: ''
  name: created
  type: dateTime
- container: ''
  name: label
  type: string
- container: ''
  name: mode
  type: string
- container: ''
  name: ctx
  type: reference
- container: ''
  name: eventId
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: birthDate
  type: date
- container: ''
  name: phone
  type: string
- container: ''
  name: lastModified
  type: dateTime
- container: ''
  name: count
  type: reference
- container: ''
  name: value
  type: integer
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: messageType
  type: string
property_count: 20
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
slug: adobe-experience-cloud-campaign-api-context
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
