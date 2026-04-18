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
- backend engineer
- create an api secret for measurement protocol authentication
- send events via measurement protocol
- privacy officer
- list data streams
- implements server-side event tracking and offline data collection.
- querying and analyzing ga4 event data through various report types.
- create, export, and query ga4 audience segments.
- extracts insights from ga4 data through reports and explorations.
- analytics
- user data deletion, access auditing, and data collection acknowledgement.
- metrics
- create data stream
- list api secrets for measurement protocol authentication
- create a data stream
- google
- web analytics
- tracking
- send events to google analytics via measurement protocol
- marketing team
- ingesting events from servers, apps, and offline sources.
- create measurement protocol secret
- validate event payloads without sending to google analytics
- setting up and maintaining ga4 account and property structure.
- validate events
- marketing ops
- bi engineer
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- server-side event tracking with data stream and secret management.
- integrates ga4 with other platforms and manages infrastructure.
- connects advertising platforms and implements server-side tracking.
- data analyst
- audits data access and monitors configuration changes.
- implements privacy-compliant data handling and deletion workflows.
- validate events without sending
- create a measurement protocol secret
- measurement protocol
- acknowledge user data collection
- compliance team
- send events
- acknowledge user data collection terms (required before creating secrets)
- events
- attribution
- run standard, realtime, pivot, and batch reports with data access auditing.
- segmenting and exporting user populations for analysis and activation.
- builds automated reporting pipelines and dashboards from ga4 data.
- connecting ga4 with advertising, app, and measurement platforms.
- data protection engineer
- analytics administrator
- list data streams for configuring event collection
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- validate event payloads
- create a new data stream for event collection
- send events to google analytics
- manage data streams for event collection
- measures campaign performance, segments audiences, and tracks conversions.
- sets up and maintains ga4 accounts, properties, and configurations.
- platform engineer
- managing data privacy, deletion, and access auditing.
- list measurement protocol secrets
- google analytics
- data
- reporting
- machine learning
- manages data privacy compliance including gdpr deletion requests.
- server side
- manage api secrets for measurement protocol
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
