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
- list data streams for configuring event collection
- acknowledge user data collection
- events
- create a new data stream for event collection
- send events to google analytics
- audits data access and monitors configuration changes.
- tracking
- reporting
- privacy officer
- metrics
- setting up and maintaining ga4 account and property structure.
- platform engineer
- extracts insights from ga4 data through reports and explorations.
- marketing ops
- connects advertising platforms and implements server-side tracking.
- marketing team
- compliance team
- ingesting events from servers, apps, and offline sources.
- send events via measurement protocol
- google
- manages data privacy compliance including gdpr deletion requests.
- measures campaign performance, segments audiences, and tracks conversions.
- validate events without sending
- validate events
- list api secrets for measurement protocol authentication
- create data stream
- google analytics
- send events
- integrates ga4 with other platforms and manages infrastructure.
- create measurement protocol secret
- implements privacy-compliant data handling and deletion workflows.
- managing data privacy, deletion, and access auditing.
- analytics
- validate event payloads without sending to google analytics
- implements server-side event tracking and offline data collection.
- builds automated reporting pipelines and dashboards from ga4 data.
- user data deletion, access auditing, and data collection acknowledgement.
- data protection engineer
- segmenting and exporting user populations for analysis and activation.
- web analytics
- create a measurement protocol secret
- validate event payloads
- acknowledge user data collection terms (required before creating secrets)
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- create, export, and query ga4 audience segments.
- data
- create a data stream
- querying and analyzing ga4 event data through various report types.
- server side
- analytics administrator
- create an api secret for measurement protocol authentication
- sets up and maintains ga4 accounts, properties, and configurations.
- backend engineer
- attribution
- manage data streams for event collection
- server-side event tracking with data stream and secret management.
- run standard, realtime, pivot, and batch reports with data access auditing.
- measurement protocol
- connecting ga4 with advertising, app, and measurement platforms.
- data analyst
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- list data streams
- send events to google analytics via measurement protocol
- manage api secrets for measurement protocol
- bi engineer
- list measurement protocol secrets
- machine learning
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
