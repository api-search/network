---
consumed_apis:
- attribution-api
- http-v2-api
- identify-api
description: Unified workflow for sending events and identifying users. For data engineers.
layout: capability
name: Amplitude Analytics Ingestion
operations:
- description: Amplitude Send Attribution Data
  method: POST
  name: sendAttribution
  path: /v1/attribution
- description: Amplitude Upload Events
  method: POST
  name: uploadEvents
  path: /v1/events
- description: Amplitude Identify a User
  method: POST
  name: identifyUser
  path: /v1/identify
personas: []
provider_name: Amplitude
provider_slug: amplitude
search_terms:
- scim provisioning and privacy compliance. for it admins and compliance teams.
- manage and evaluate a/b experiments and feature flags. for product managers.
- identity management
- event ingestion
- manages privacy and compliance
- identify api identifyUser
- analytics
- amplitude send attribution data
- amplitude upload events
- analyzes data and manages cohorts
- export raw event data and manage behavioral cohorts. for data analysts.
- feature flags
- privacy compliance
- experimentation
- data governance
- product analytics
- ingests and exports event data
- identifyUser
- manage event schemas and chart annotations. for data governance teams.
- a/b testing
- runs experiments and feature flags
- amplitude
- attribution api sendAttribution
- amplitude identify a user
- http v2 api uploadEvents
- sendAttribution
- unified workflow for sending events and identifying users. for data engineers.
- user behavior
- uploadEvents
slug: amplitude-analytics-ingestion
tags:
- Amplitude
- Analytics
- Event Ingestion
tools:
- description: Amplitude Send Attribution Data
  hints:
    readOnly: false
  name: attribution-api-sendAttribution
- description: Amplitude Upload Events
  hints:
    readOnly: false
  name: http-v2-api-uploadEvents
- description: Amplitude Identify a User
  hints:
    readOnly: false
  name: identify-api-identifyUser
---
