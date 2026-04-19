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
- manage and evaluate a/b experiments and feature flags. for product managers.
- event ingestion
- data governance
- user behavior
- amplitude
- amplitude identify a user
- attribution api sendAttribution
- uploadEvents
- identity management
- sendAttribution
- ingests and exports event data
- unified workflow for sending events and identifying users. for data engineers.
- product analytics
- privacy compliance
- runs experiments and feature flags
- identifyUser
- analyzes data and manages cohorts
- identify api identifyUser
- export raw event data and manage behavioral cohorts. for data analysts.
- analytics
- http v2 api uploadEvents
- manage event schemas and chart annotations. for data governance teams.
- manages privacy and compliance
- experimentation
- amplitude upload events
- amplitude send attribution data
- feature flags
- a/b testing
- scim provisioning and privacy compliance. for it admins and compliance teams.
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
