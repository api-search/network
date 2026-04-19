---
class_count: 13
classes:
- ActivationRequest
- BatchActivationItem
- BatchActivationRequest
- Campaign
- CampaignRequest
- CampaignResponseFull
- CampaignResponseNormal
- CampaignResponseSimple
- CampaignVariation
- Flag
- FlagMetadata
- FlagsResponse
- SingleCampaignRequest
context_file: json-ld/ab-tasty-decision-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-ld/ab-tasty-decision-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Ab Tasty Decision Api from AB Tasty.
layout: jsonld
name: Ab Tasty Decision Api Context
namespaces:
- prefix: abt
  uri: https://abtasty.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: visitorId
  type: string
- container: ''
  name: anonymousId
  type: string
- container: ''
  name: context
  type: ''
- container: ''
  name: visitorConsent
  type: boolean
- container: ''
  name: triggerHit
  type: boolean
- container: ''
  name: decisionGroup
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: variationGroupId
  type: string
- container: ''
  name: variation
  type: ''
- container: ''
  name: campaignId
  type: string
- container: ''
  name: variationId
  type: string
- container: set
  name: campaigns
  type: ''
- container: ''
  name: value
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: vid
  type: string
- container: ''
  name: aid
  type: string
- container: ''
  name: cid
  type: string
- container: ''
  name: caid
  type: string
- container: ''
  name: vaid
  type: string
- container: set
  name: batch
  type: ''
- container: set
  name: campaignsVariation
  type: ''
- container: ''
  name: mergedModifications
  type: ''
- container: ''
  name: qt
  type: integer
- container: ''
  name: campaignName
  type: string
- container: ''
  name: slug
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: variationGroupName
  type: string
- container: ''
  name: variationName
  type: string
- container: ''
  name: reference
  type: boolean
property_count: 29
provider_name: AB Tasty
provider_slug: ab-tasty
slug: ab-tasty-decision-api-context
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
- JSON-LD
- Linked Data
- Semantic Web
---
