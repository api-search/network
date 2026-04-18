---
class_count: 4
classes:
- Domain
- DomainCollectionResponse
- ForwardPaging
- NextPage
context_file: json-ld/hubspot-domains-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-domains-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Domains Api from HubSpot.
layout: jsonld
name: Hubspot Domains Api Context
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
  name: domain
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: isResolving
  type: boolean
- container: ''
  name: isManuallyMarkedAsResolving
  type: boolean
- container: ''
  name: isSslEnabled
  type: boolean
- container: ''
  name: isSslOnly
  type: boolean
- container: ''
  name: isPrimaryBlogPost
  type: boolean
- container: ''
  name: isPrimarySitePage
  type: boolean
- container: ''
  name: isPrimaryLandingPage
  type: boolean
- container: ''
  name: isPrimaryEmail
  type: boolean
- container: ''
  name: isPrimaryKnowledge
  type: boolean
- container: ''
  name: isUsedForBlogPost
  type: boolean
- container: ''
  name: isUsedForSitePage
  type: boolean
- container: ''
  name: isUsedForLandingPage
  type: boolean
- container: ''
  name: isUsedForEmail
  type: boolean
- container: ''
  name: isUsedForKnowledge
  type: boolean
- container: ''
  name: expectedCname
  type: string
- container: ''
  name: redirectTo
  type: string
- container: ''
  name: secondaryToDomain
  type: string
- container: ''
  name: total
  type: string
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: next
  type: reference
- container: ''
  name: after
  type: string
- container: ''
  name: link
  type: string
property_count: 27
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-domains-api-context
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
