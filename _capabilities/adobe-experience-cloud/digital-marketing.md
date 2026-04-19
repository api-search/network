---
consumed_apis:
- analytics-api
- target-api
- journey-optimizer
description: Unified workflow capability combining Adobe Analytics, Adobe Target, and Adobe Journey Optimizer for data-driven marketing campaigns, A/B testing, and personalized journey orchestration. Designed for digital marketers and marketing technologists.
layout: capability
name: Adobe Experience Cloud Digital Marketing
operations:
- description: Run an Adobe Analytics report.
  method: POST
  name: run-report
  path: /v1/reports
- description: List analytics segments.
  method: GET
  name: list-segments
  path: /v1/segments
- description: List Target activities.
  method: GET
  name: list-activities
  path: /v1/activities
- description: List Target audiences.
  method: GET
  name: list-audiences
  path: /v1/audiences
- description: List Journey Optimizer journeys.
  method: GET
  name: list-journeys
  path: /v1/journeys
- description: List Journey Optimizer offers.
  method: GET
  name: list-offers
  path: /v1/offers
personas: []
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
search_terms:
- list targeting audiences in adobe target.
- create a new personalized offer in adobe journey optimizer.
- run report
- customer journeys.
- run an adobe analytics report with dimensions, metrics, and segments.
- technical marketer integrating experience cloud apis into marketing stack.
- adobe experience cloud
- ajo list offers
- unified customer profiles and data management.
- journey orchestration
- list journeys
- digital analytics reporting and audience insights.
- list content offers in adobe target.
- analytics list segments
- run analytics report
- customer experience
- campaign management
- list a/b test and personalization activities in adobe target.
- ajo create offer
- multi-channel customer journey management.
- list target activities.
- ajo list messages
- list analytics segments.
- run an adobe analytics report.
- list segments
- target list activities
- personalization
- list personalized offers in adobe journey optimizer.
- CDP Administrator
- Marketing Technologist
- list offers
- digital marketing
- list audience segments in adobe analytics.
- audience segment management.
- target audiences.
- administrator managing customer profiles, segments, and identity resolution.
- list journey optimizer journeys.
- list activities
- list target audiences.
- analytics
- list customer journeys in adobe journey optimizer.
- list campaign messages in adobe journey optimizer.
- target list offers
- Digital Marketer
- profile management, audience segmentation, and data ingestion.
- a/b testing and content personalization.
- analytics list metrics
- Data Engineer
- marketing professional using analytics, personalization, and journey tools.
- engineer managing data pipelines, schemas, and datasets in experience platform.
- a/b test and personalization activities.
- list journey optimizer offers.
- list available metrics for an adobe analytics report suite.
- ajo list journeys
- analytics, a/b testing, and journey orchestration for digital marketers.
- list audiences
- target list audiences
- analytics report execution.
- personalized offers.
slug: digital-marketing
tags:
- Adobe Experience Cloud
- Digital Marketing
- Analytics
- Personalization
- Journey Orchestration
tools:
- description: Run an Adobe Analytics report with dimensions, metrics, and segments.
  hints:
    openWorld: true
    readOnly: true
  name: run-analytics-report
- description: List audience segments in Adobe Analytics.
  hints:
    openWorld: true
    readOnly: true
  name: analytics-list-segments
- description: List available metrics for an Adobe Analytics report suite.
  hints:
    openWorld: true
    readOnly: true
  name: analytics-list-metrics
- description: List A/B test and personalization activities in Adobe Target.
  hints:
    openWorld: true
    readOnly: true
  name: target-list-activities
- description: List targeting audiences in Adobe Target.
  hints:
    openWorld: true
    readOnly: true
  name: target-list-audiences
- description: List content offers in Adobe Target.
  hints:
    openWorld: true
    readOnly: true
  name: target-list-offers
- description: List customer journeys in Adobe Journey Optimizer.
  hints:
    openWorld: true
    readOnly: true
  name: ajo-list-journeys
- description: List personalized offers in Adobe Journey Optimizer.
  hints:
    openWorld: true
    readOnly: true
  name: ajo-list-offers
- description: Create a new personalized offer in Adobe Journey Optimizer.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: ajo-create-offer
- description: List campaign messages in Adobe Journey Optimizer.
  hints:
    openWorld: true
    readOnly: true
  name: ajo-list-messages
---
