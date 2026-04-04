---
aid: ab-tasty:decision-api
name: AB Tasty Decision API
tags:
  - Decision
  - Experiments
  - Personaliztions
humanURL: https://docs.abtasty.com/server-side/decision-api/decision-api
properties:
  - url: openapi/decision-api-openapi.yml
    type: OpenAPI
description: >-
  The AB Tasty Decision API is a server-side service that evaluates a visitors
  context against your active experiments, personalizations, and feature flags,
  then returns a deterministic decision which campaigns the user qualifies for,
  the selected variation, and any variables or content to render. It centralizes
  targeting, traffic allocation, and bucketing so you can power A/B tests,
  gradual rollouts, and personalized experiences from backends, mobile apps, or
  edge workers while keeping user exposure consistent. You pass identifiers and
  attributes at request time, use the response to render the experience, and
  pair it with event tracking for measurement...

---