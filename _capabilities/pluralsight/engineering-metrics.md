---
consumed_apis:
- pluralsight-flow-coding-metrics
- pluralsight-flow-collaboration-metrics
- pluralsight-flow-dora-metrics
- pluralsight-flow-commits
- pluralsight-flow-pull-requests
- pluralsight-flow-tickets
description: Unified workflow for engineering managers to track developer productivity, code quality, collaboration, and delivery performance through Flow metrics. Combines coding metrics, collaboration metrics, DORA metrics, commits, pull requests, and tickets APIs.
layout: capability
name: Pluralsight Engineering Metrics
operations:
- description: Retrieve code-level engineering metrics
  method: GET
  name: get-coding-metrics
  path: /v1/coding-metrics
- description: Retrieve collaboration metrics for engineering teams
  method: GET
  name: get-collaboration-metrics
  path: /v1/collaboration-metrics
- description: Retrieve DORA engineering metrics
  method: GET
  name: get-dora-metrics
  path: /v1/dora-metrics
- description: Retrieve commit data and metrics
  method: GET
  name: get-commits
  path: /v1/commits
- description: Retrieve pull request data and events
  method: GET
  name: get-pull-requests
  path: /v1/pull-requests
- description: Retrieve ticket data and events
  method: GET
  name: get-tickets
  path: /v1/tickets
personas: []
provider_name: Pluralsight
provider_slug: pluralsight
search_terms:
- get dora metrics
- dora engineering metrics including deployment frequency and lead time
- skills assessment
- retrieve commit data and metrics
- technology
- courses
- engineering metrics
- retrieve collaboration metrics for engineering teams
- retrieve pull request data and events
- get tickets
- get pull requests
- retrieve pull request data, comments, and events across repositories.
- retrieve dora engineering metrics
- flow
- get coding metrics
- pull request and collaboration metrics for engineering teams
- video training
- retrieve ticket data including comments, events, and project associations from connected project management tools.
- pluralsight
- retrieve commit data and aggregated commit metrics across repositories.
- collaboration
- get collaboration metrics
- learning
- retrieve dora engineering metrics including deployment frequency, lead time for changes, change failure rate, and time to restore service.
- code-level engineering metrics and developer productivity data
- commit data and aggregated metrics across repositories
- pull request data, comments, and events across repositories
- dora
- retrieve ticket data and events
- retrieve pull request and collaboration metrics for engineering teams with date range filtering.
- education
- ticket data from connected project management tools
- retrieve code-level engineering metrics and developer productivity data with date range filtering.
- developer productivity
- retrieve code-level engineering metrics
- get commits
slug: engineering-metrics
tags:
- Pluralsight
- Flow
- Engineering Metrics
- Developer Productivity
- DORA
- Collaboration
tools:
- description: Retrieve code-level engineering metrics and developer productivity data with date range filtering.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-coding-metrics
- description: Retrieve pull request and collaboration metrics for engineering teams with date range filtering.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-collaboration-metrics
- description: Retrieve DORA engineering metrics including deployment frequency, lead time for changes, change failure rate, and time to restore service.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-dora-metrics
- description: Retrieve commit data and aggregated commit metrics across repositories.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-commits
- description: Retrieve pull request data, comments, and events across repositories.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-pull-requests
- description: Retrieve ticket data including comments, events, and project associations from connected project management tools.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-tickets
---
