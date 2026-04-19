---
class_count: 27
classes:
- Campaign
- MessageInput
- JourneyList
- Offer
- PlacementList
- CollectionInput
- ContentTemplateList
- CollectionList
- DecisionRuleList
- OfferInput
- JourneyInput
- DecisionRuleInput
- MessageList
- DecisionRule
- Journey
- ContentTemplateInput
- PlacementInput
- Message
- CampaignInput
- OfferList
- Collection
- CampaignList
- ContentTemplate
- Placement
- name
- description
- version
context_file: json-ld/adobe-experience-cloud-journey-optimizer-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/json-ld/adobe-experience-cloud-journey-optimizer-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Experience Cloud Journey Optimizer Api from Adobe Experience Cloud.
layout: jsonld
name: Adobe Experience Cloud Journey Optimizer Api Context
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
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: schedule
  type: reference
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: endDate
  type: dateTime
- container: ''
  name: content
  type: reference
- container: set
  name: journeys
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: totalCount
  type: integer
- container: set
  name: representations
  type: string
- container: ''
  name: placement
  type: string
- container: ''
  name: priority
  type: integer
- container: set
  name: placements
  type: string
- container: ''
  name: contentType
  type: string
- container: ''
  name: filter
  type: reference
- container: set
  name: templates
  type: string
- container: set
  name: collections
  type: string
- container: set
  name: decisionRules
  type: string
- container: ''
  name: condition
  type: string
- container: ''
  name: eligibilityRule
  type: string
- container: ''
  name: entryCondition
  type: reference
- container: set
  name: activities
  type: string
- container: set
  name: messages
  type: string
- container: ''
  name: audienceId
  type: string
- container: set
  name: offers
  type: string
- container: set
  name: campaigns
  type: string
property_count: 28
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
slug: adobe-experience-cloud-journey-optimizer-api-context
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
