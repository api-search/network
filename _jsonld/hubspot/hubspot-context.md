---
class_count: 1
classes:
- id
context_file: json-ld/hubspot-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot from HubSpot.
layout: jsonld
name: Hubspot Context
namespaces:
- prefix: hubspot
  uri: https://developers.hubspot.com/docs/api/schemas/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: rdfs
  uri: http://www.w3.org/2000/01/rdf-schema#
properties:
- container: ''
  name: Contact
  type: rdfs:Class
- container: ''
  name: Company
  type: rdfs:Class
- container: ''
  name: Deal
  type: rdfs:Class
- container: ''
  name: Ticket
  type: rdfs:Class
- container: ''
  name: Engagement
  type: rdfs:Class
- container: ''
  name: WebhookEvent
  type: rdfs:Class
- container: ''
  name: email
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastname
  type: string
- container: ''
  name: phone
  type: string
- container: ''
  name: mobilephone
  type: string
- container: ''
  name: company
  type: string
- container: ''
  name: website
  type: anyURI
- container: ''
  name: jobtitle
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: zip
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: domain
  type: anyURI
- container: ''
  name: description
  type: string
- container: ''
  name: numberofemployees
  type: integer
- container: ''
  name: annualrevenue
  type: decimal
- container: ''
  name: dealname
  type: string
- container: ''
  name: amount
  type: decimal
- container: ''
  name: dealstage
  type: string
- container: ''
  name: closedate
  type: date
- container: ''
  name: pipeline
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: hs_ticket_priority
  type: string
- container: ''
  name: hs_pipeline_stage
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: associations
  type: ''
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
  name: eventId
  type: ''
- container: ''
  name: objectId
  type: integer
- container: ''
  name: portalId
  type: integer
- container: ''
  name: occurredAt
  type: long
- container: ''
  name: subscriptionType
  type: string
- container: ''
  name: changeSource
  type: string
- container: ''
  name: changeFlag
  type: string
- container: ''
  name: propertyName
  type: string
- container: ''
  name: propertyValue
  type: string
- container: ''
  name: subscriptionId
  type: integer
- container: ''
  name: appId
  type: integer
property_count: 49
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-context
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
