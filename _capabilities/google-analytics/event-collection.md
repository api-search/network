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
- platform engineer
- privacy officer
- data protection engineer
- data
- tracking
- validate event payloads
- integrates ga4 with other platforms and manages infrastructure.
- list data streams
- audits data access and monitors configuration changes.
- attribution
- server side
- web analytics
- metrics
- setting up and maintaining ga4 account and property structure.
- analytics administrator
- measures campaign performance, segments audiences, and tracks conversions.
- manage api secrets for measurement protocol
- implements server-side event tracking and offline data collection.
- list api secrets for measurement protocol authentication
- list measurement protocol secrets
- list data streams for configuring event collection
- acknowledge user data collection terms (required before creating secrets)
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- connecting ga4 with advertising, app, and measurement platforms.
- machine learning
- acknowledge user data collection
- create a new data stream for event collection
- send events to google analytics via measurement protocol
- analytics
- managing data privacy, deletion, and access auditing.
- create a measurement protocol secret
- create measurement protocol secret
- run standard, realtime, pivot, and batch reports with data access auditing.
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- create, export, and query ga4 audience segments.
- create a data stream
- extracts insights from ga4 data through reports and explorations.
- segmenting and exporting user populations for analysis and activation.
- data analyst
- marketing team
- user data deletion, access auditing, and data collection acknowledgement.
- ingesting events from servers, apps, and offline sources.
- measurement protocol
- manages data privacy compliance including gdpr deletion requests.
- google
- validate events
- compliance team
- validate event payloads without sending to google analytics
- create data stream
- marketing ops
- builds automated reporting pipelines and dashboards from ga4 data.
- manage data streams for event collection
- send events via measurement protocol
- create an api secret for measurement protocol authentication
- implements privacy-compliant data handling and deletion workflows.
- reporting
- google analytics
- send events to google analytics
- backend engineer
- sets up and maintains ga4 accounts, properties, and configurations.
- server-side event tracking with data stream and secret management.
- querying and analyzing ga4 event data through various report types.
- validate events without sending
- events
- bi engineer
- send events
- connects advertising platforms and implements server-side tracking.
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
