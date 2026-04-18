---
consumed_apis:
- rest-api
description: Alert policy and condition management workflow for platform admins configuring and maintaining New Relic alerting rules, notification channels, and policy structures.
layout: capability
name: New Relic Alerting Configuration
operations:
- description: List alert policies
  method: GET
  name: get-alerts-policies
  path: /v1/policies
- description: Create a new alert policy
  method: POST
  name: create-alerts-policy
  path: /v1/policies
- description: Update an alert policy
  method: PUT
  name: update-alerts-policy
  path: /v1/policies/{policyId}
- description: Delete an alert policy
  method: DELETE
  name: delete-alerts-policy
  path: /v1/policies/{policyId}
- description: List conditions for a policy
  method: GET
  name: get-alerts-conditions
  path: /v1/conditions
- description: List alert incidents
  method: GET
  name: get-alerts-incidents
  path: /v1/incidents
- description: List alert violations
  method: GET
  name: get-alerts-violations
  path: /v1/violations
- description: List alert events
  method: GET
  name: get-alerts-events
  path: /v1/alert-events
personas: []
provider_name: New Relic
provider_slug: new-relic
search_terms:
- list alert violations
- update alerts policy
- list alert events
- list all alert policies
- analysis
- get alerts policies
- create a new alert policy
- apm
- list alert conditions
- alerting
- get alerts violations
- delete an alert policy
- list alert incidents
- update an alert policy
- list alert events filtered by product or entity type
- infrastructure
- monitoring
- create alerts policy
- get alerts incidents
- list conditions for a policy
- list alert policies
- platform
- analytics
- update or delete an alert policy
- observability
- manage alert policies
- performance
- configuration
- platform administration
- devops
- policies
- list alert conditions for a specific policy
- get alerts conditions
- new relic
- delete alerts policy
- get alerts events
slug: full-stack-observability
tags:
- New Relic
- Alerting
- Configuration
- Platform Administration
- Policies
tools:
- description: List all alert policies
  hints:
    openWorld: true
    readOnly: true
  name: get-alerts-policies
- description: Create a new alert policy
  hints:
    openWorld: true
    readOnly: false
  name: create-alerts-policy
- description: Update an alert policy
  hints:
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-alerts-policy
- description: Delete an alert policy
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-alerts-policy
- description: List alert conditions for a specific policy
  hints:
    openWorld: true
    readOnly: true
  name: get-alerts-conditions
- description: List alert incidents
  hints:
    openWorld: true
    readOnly: true
  name: get-alerts-incidents
- description: List alert violations
  hints:
    openWorld: true
    readOnly: true
  name: get-alerts-violations
- description: List alert events filtered by product or entity type
  hints:
    openWorld: true
    readOnly: true
  name: get-alerts-events
---
