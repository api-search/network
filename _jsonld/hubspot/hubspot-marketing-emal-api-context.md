---
class_count: 9
classes:
- SmtpToken
- SmtpTokenWithPassword
- SmtpTokenCollectionResponse
- SmtpTokenCreateRequest
- TransactionalEmailRequest
- EmailMessage
- TransactionalEmailResponse
- Paging
- NextPage
context_file: json-ld/hubspot-marketing-emal-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-marketing-emal-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Marketing Emal Api from HubSpot.
layout: jsonld
name: Hubspot Marketing Emal Api Context
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
  name: campaignName
  type: string
- container: ''
  name: emailCampaignId
  type: string
- container: ''
  name: createContact
  type: boolean
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: createdBy
  type: string
- container: ''
  name: password
  type: string
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: emailId
  type: integer
- container: ''
  name: message
  type: reference
- container: ''
  name: contactProperties
  type: reference
- container: ''
  name: customProperties
  type: reference
- container: ''
  name: to
  type: string
- container: ''
  name: from
  type: string
- container: ''
  name: sendId
  type: string
- container: set
  name: replyTo
  type: string
- container: set
  name: cc
  type: string
- container: set
  name: bcc
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusId
  type: string
- container: ''
  name: sendResult
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
- container: ''
  name: next
  type: reference
- container: ''
  name: after
  type: string
- container: ''
  name: link
  type: string
property_count: 28
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-marketing-emal-api-context
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
