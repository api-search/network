---
consumed_apis:
- ga-measurement-protocol
- ga-admin-api
description: Unified workflow for server-side event tracking combining the Measurement Protocol for sending events with the Admin API for managing measurement protocol secrets and data streams. Used by backend engineers and marketing ops teams to implement server-side tracking and offline event collection.
layout: capability
name: Google Analytics Event Collection
operations:
- description: Send events via Measurement Protocol
  method: POST
  name: send-events
  path: /v1/events
- description: Validate event payloads
  method: POST
  name: validate-events
  path: /v1/events/validate
- description: List data streams
  method: GET
  name: list-data-streams
  path: /v1/data-streams
- description: Create a data stream
  method: POST
  name: create-data-stream
  path: /v1/data-streams
- description: List measurement protocol secrets
  method: GET
  name: list-measurement-protocol-secrets
  path: /v1/secrets
- description: Create a measurement protocol secret
  method: POST
  name: create-measurement-protocol-secret
  path: /v1/secrets
personas:
- description: Implements server-side event tracking and offline data collection.
  id: backend-engineer
  name: Backend Engineer
- description: Connects advertising platforms and implements server-side tracking.
  id: marketing-ops
  name: Marketing Operations
provider_name: Google Analytics
provider_slug: google-analytics
search_terms:
- data protection engineer
- measurement protocol
- sets up and maintains ga4 accounts, properties, and configurations.
- server side
- setting up and maintaining ga4 account and property structure.
- google
- builds automated reporting pipelines and dashboards from ga4 data.
- analytics
- list data streams
- compliance team
- web analytics
- backend engineer
- google analytics
- send events via measurement protocol
- analytics administrator
- implements server-side event tracking and offline data collection.
- run standard, realtime, pivot, and batch reports with data access auditing.
- create, export, and query ga4 audience segments.
- create an api secret for measurement protocol authentication
- validate event payloads
- manage api secrets for measurement protocol
- data
- data analyst
- machine learning
- manages data privacy compliance including gdpr deletion requests.
- send events to google analytics
- querying and analyzing ga4 event data through various report types.
- create measurement protocol secret
- managing data privacy, deletion, and access auditing.
- attribution
- tracking
- connecting ga4 with advertising, app, and measurement platforms.
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- send events to google analytics via measurement protocol
- bi engineer
- implements privacy-compliant data handling and deletion workflows.
- acknowledge user data collection
- connects advertising platforms and implements server-side tracking.
- extracts insights from ga4 data through reports and explorations.
- create data stream
- privacy officer
- create a new data stream for event collection
- acknowledge user data collection terms (required before creating secrets)
- marketing ops
- reporting
- validate events
- create a measurement protocol secret
- marketing team
- create a data stream
- list api secrets for measurement protocol authentication
- integrates ga4 with other platforms and manages infrastructure.
- list measurement protocol secrets
- user data deletion, access auditing, and data collection acknowledgement.
- list data streams for configuring event collection
- measures campaign performance, segments audiences, and tracks conversions.
- ingesting events from servers, apps, and offline sources.
- segmenting and exporting user populations for analysis and activation.
- platform engineer
- manage data streams for event collection
- events
- server-side event tracking with data stream and secret management.
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- validate event payloads without sending to google analytics
- metrics
- send events
- validate events without sending
- audits data access and monitors configuration changes.
slug: event-collection
tags:
- Google Analytics
- Measurement Protocol
- Events
- Server Side
- Tracking
tools:
- description: Send events to Google Analytics via Measurement Protocol
  hints:
    idempotent: false
    readOnly: false
  name: send-events
- description: Validate event payloads without sending to Google Analytics
  hints:
    idempotent: true
    readOnly: true
  name: validate-events
- description: List data streams for configuring event collection
  hints:
    idempotent: true
    readOnly: true
  name: list-data-streams
- description: Create a new data stream for event collection
  hints:
    idempotent: false
    readOnly: false
  name: create-data-stream
- description: List API secrets for Measurement Protocol authentication
  hints:
    idempotent: true
    readOnly: true
  name: list-measurement-protocol-secrets
- description: Create an API secret for Measurement Protocol authentication
  hints:
    idempotent: false
    readOnly: false
  name: create-measurement-protocol-secret
- description: Acknowledge user data collection terms (required before creating secrets)
  hints:
    idempotent: true
    readOnly: false
  name: acknowledge-user-data-collection
---
