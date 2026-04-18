---
consumed_apis:
- problems-v2
- events-v2
- entities-v2
description: Unified incident response workflow combining problems, events, and entity data for SREs investigating service degradations detected by Davis AI.
layout: capability
name: Dynatrace Incident Response
operations:
- description: List problems detected by Davis AI
  method: GET
  name: list-problems
  path: /v1/problems
- description: Get full problem details with root cause analysis
  method: GET
  name: get-problem
  path: /v1/problems/{problemId}
- description: Close a problem with an optional message
  method: POST
  name: close-problem
  path: /v1/problems/{problemId}/close
- description: List comments on a problem
  method: GET
  name: list-problem-comments
  path: /v1/problems/{problemId}/comments
- description: Add an investigation comment
  method: POST
  name: create-problem-comment
  path: /v1/problems/{problemId}/comments
- description: Get a comment
  method: GET
  name: get-problem-comment
  path: /v1/problems/{problemId}/comments/{commentId}
- description: Update a comment
  method: PUT
  name: update-problem-comment
  path: /v1/problems/{problemId}/comments/{commentId}
- description: Delete a comment
  method: DELETE
  name: delete-problem-comment
  path: /v1/problems/{problemId}/comments/{commentId}
- description: List events matching filters
  method: GET
  name: list-events
  path: /v1/events
- description: Get a specific event
  method: GET
  name: get-event
  path: /v1/events/{eventId}
- description: Ingest a custom event to annotate the timeline
  method: POST
  name: ingest-event
  path: /v1/events/ingest
- description: List entities matching a selector
  method: GET
  name: list-entities
  path: /v1/entities
- description: Get entity details for root cause investigation
  method: GET
  name: get-entity
  path: /v1/entities/{entityId}
personas: []
provider_name: Dynatrace
provider_slug: dynatrace
search_terms:
- list events in the dynatrace environment
- create problem comment
- add an investigation comment to a problem
- delete problem comment
- analytics
- get a specific event
- close a problem with an optional message
- manage investigation comments
- get a comment
- get entity details for root cause investigation
- list problem comments
- observability
- update an investigation comment
- list entities matching a selector
- list investigation comments on a problem
- problems
- list comments on a problem
- cloud monitoring
- close an open problem with an optional closing message
- close a problem
- get details of a specific monitored entity
- get entity
- ingest event
- digital experience management
- list problems detected by davis ai in the dynatrace environment
- list entities
- delete a comment
- dynatrace
- list problems
- get details of a specific event
- sre
- get problem
- ingest custom events
- list monitored entities matching a selector
- list problems detected by davis ai
- update a comment
- events
- ai operations
- incident response
- delete a comment from a problem
- close problem
- get event
- query events related to incidents
- list events matching filters
- query affected entities
- intelligence
- get problem details including root cause
- application performance monitoring
- add an investigation comment
- apm
- ingest a custom event to annotate the timeline
- manage a specific comment
- get problem comment
- update problem comment
- list events
- get entity details
- get full details of a specific problem including root cause analysis
- get a specific comment on a problem
- get event details
- query and manage ai-detected problems
- application security
- automation
- get full problem details with root cause analysis
slug: incident-response
tags:
- Dynatrace
- Incident Response
- SRE
- Problems
- Events
tools:
- description: List problems detected by Davis AI in the Dynatrace environment
  hints:
    openWorld: true
    readOnly: true
  name: list-problems
- description: Get full details of a specific problem including root cause analysis
  hints:
    openWorld: true
    readOnly: true
  name: get-problem
- description: Close an open problem with an optional closing message
  hints:
    destructive: true
    openWorld: true
    readOnly: false
  name: close-problem
- description: List investigation comments on a problem
  hints:
    openWorld: true
    readOnly: true
  name: list-problem-comments
- description: Add an investigation comment to a problem
  hints:
    openWorld: true
    readOnly: false
  name: create-problem-comment
- description: Get a specific comment on a problem
  hints:
    openWorld: true
    readOnly: true
  name: get-problem-comment
- description: Update an investigation comment
  hints:
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-problem-comment
- description: Delete a comment from a problem
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-problem-comment
- description: List events in the Dynatrace environment
  hints:
    openWorld: true
    readOnly: true
  name: list-events
- description: Get details of a specific event
  hints:
    openWorld: true
    readOnly: true
  name: get-event
- description: Ingest a custom event to annotate the timeline
  hints:
    openWorld: true
    readOnly: false
  name: ingest-event
- description: List monitored entities matching a selector
  hints:
    openWorld: true
    readOnly: true
  name: list-entities
- description: Get details of a specific monitored entity
  hints:
    openWorld: true
    readOnly: true
  name: get-entity
---
