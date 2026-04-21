---
consumed_apis:
- decision-api
description: Unified workflow for server-side feature experimentation, A/B testing, and feature flag management. Enables developers and product teams to evaluate campaigns, retrieve flag values, and track activations for controlled rollouts and experiments.
layout: capability
name: AB Tasty Feature Experimentation
operations:
- description: Evaluate visitor context and retrieve all matching campaign assignments
  method: POST
  name: get-campaigns
  path: /v1/campaigns
- description: Get assignment for a specific campaign by ID
  method: POST
  name: get-campaign
  path: /v1/campaigns/{campaignId}
- description: Retrieve feature flag values and metadata for a visitor
  method: POST
  name: get-flags
  path: /v1/flags
- description: Manually activate a campaign variation for a visitor
  method: POST
  name: activate-campaign
  path: /v1/activate
personas: []
provider_name: AB Tasty
provider_slug: ab-tasty
search_terms:
- product manager monitoring experiment assignments and flag rollouts
- activate experiment
- retrieve feature flag values and metadata for a visitor, used to implement feature toggles and progressive rollouts
- backend or frontend developer implementing server-side experiments and feature flags
- feature flag evaluation operations
- get visitor campaign
- get visitor campaigns
- retrieve a specific campaign assignment for a visitor, useful for targeted experiment evaluation
- get campaigns
- server side
- aggregation
- feature flags
- unified workflow for server-side feature experimentation, a/b testing, and feature flag management
- get flags
- retrieve a specific campaign assignment for a visitor
- conversion tracking and experiment measurement
- experimentation
- progressive feature releases and feature toggles
- Product Manager
- manually activate a campaign variation for a visitor
- ab tasty
- get visitor flags
- retrieve feature flag values and metadata for a visitor
- Developer
- a/b testing
- evaluate visitor context and retrieve all matching campaign assignments
- get campaign
- get assignment for a specific campaign by id
- manual campaign activation
- retrieve campaign assignments for a visitor based on context
- quality assurance engineer using remote control api to test experiments
- evaluate a visitor's context and retrieve all active campaign and variation assignments for server-side rendering
- a/b testing, multivariate testing, and experiment management
- personalization
- manually activate a campaign variation assignment, used when auto-activation is disabled via trigger_hit=false
- activate campaign
slug: feature-experimentation
tags:
- AB Tasty
- Experimentation
- Feature Flags
- A/B Testing
- Server Side
tools:
- description: Evaluate a visitor's context and retrieve all active campaign and variation assignments for server-side rendering
  hints:
    openWorld: false
    readOnly: true
  name: get-visitor-campaigns
- description: Retrieve a specific campaign assignment for a visitor, useful for targeted experiment evaluation
  hints:
    openWorld: false
    readOnly: true
  name: get-visitor-campaign
- description: Retrieve feature flag values and metadata for a visitor, used to implement feature toggles and progressive rollouts
  hints:
    openWorld: false
    readOnly: true
  name: get-visitor-flags
- description: Manually activate a campaign variation assignment, used when auto-activation is disabled via trigger_hit=false
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: activate-experiment
---
