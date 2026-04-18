---
class_count: 14
classes:
- FeatureFlag
- FeatureFlagInput
- PortalFlagState
- PortalFlagStateInput
- PortalFlagStateCollection
- BatchPortalFlagStateInput
- BatchPortalFlagStateInputItem
- BatchDeleteInput
- BatchDeleteInputItem
- BatchPortalFlagStateResponse
- BatchPortalFlagStateResponseWithErrors
- BatchError
- Paging
- PagingNext
context_file: json-ld/hubspot-crm-feature-flags-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-crm-feature-flags-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Crm Feature Flags Api from HubSpot.
layout: jsonld
name: Hubspot Crm Feature Flags Api Context
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
  name: appId
  type: string
- container: ''
  name: flagName
  type: string
- container: ''
  name: defaultState
  type: string
- container: ''
  name: overrideState
  type: string
- container: ''
  name: portalId
  type: string
- container: ''
  name: flagState
  type: string
- container: set
  name: portalFlagStates
  type: reference
- container: ''
  name: paging
  type: reference
- container: set
  name: inputs
  type: reference
- container: ''
  name: status
  type: string
- container: set
  name: results
  type: reference
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: completedAt
  type: dateTime
- container: set
  name: errors
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: context
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
property_count: 20
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-crm-feature-flags-api-context
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
