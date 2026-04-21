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
- events
- get event
- list monitored entities matching a selector
- add an investigation comment to a problem
- application performance monitoring
- get details of a specific monitored entity
- analytics
- get details of a specific event
- close a problem with an optional message
- intelligence
- get a specific event
- digital experience management
- get full details of a specific problem including root cause analysis
- list problems detected by davis ai in the dynatrace environment
- close problem
- get entity
- update an investigation comment
- update a comment
- list events
- ingest custom events
- ai operations
- problems
- query events related to incidents
- automation
- ingest a custom event to annotate the timeline
- observability
- get a comment
- get entity details for root cause investigation
- get problem details including root cause
- query affected entities
- add an investigation comment
- get a specific comment on a problem
- application security
- apm
- list entities matching a selector
- incident response
- close an open problem with an optional closing message
- list comments on a problem
- delete a comment from a problem
- sre
- delete problem comment
- get event details
- list problems detected by davis ai
- close a problem
- list problem comments
- cloud monitoring
- get full problem details with root cause analysis
- ingest event
- get problem
- manage investigation comments
- list events in the dynatrace environment
- list problems
- get entity details
- update problem comment
- query and manage ai-detected problems
- get problem comment
- delete a comment
- manage a specific comment
- list investigation comments on a problem
- list entities
- create problem comment
- list events matching filters
- dynatrace
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
