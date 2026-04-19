---
consumed_apis:
- ga-admin-api
description: Unified workflow for managing GA4 integration links with Firebase, Google Ads, and measurement protocol secrets. Used by platform engineers and marketing ops teams to connect GA4 with advertising and app platforms.
layout: capability
name: Google Analytics Integrations and Linking
operations:
- description: List Firebase links on a property
  method: GET
  name: list-firebase-links
  path: /v1/firebase-links
- description: Create a Firebase link
  method: POST
  name: create-firebase-link
  path: /v1/firebase-links
- description: List Google Ads links on a property
  method: GET
  name: list-google-ads-links
  path: /v1/google-ads-links
- description: Create a Google Ads link
  method: POST
  name: create-google-ads-link
  path: /v1/google-ads-links
- description: Update a Google Ads link
  method: PATCH
  name: update-google-ads-link
  path: /v1/google-ads-links/{id}
- description: Delete a Google Ads link
  method: DELETE
  name: delete-google-ads-link
  path: /v1/google-ads-links/{id}
- description: List measurement protocol secrets
  method: GET
  name: list-measurement-protocol-secrets
  path: /v1/measurement-protocol-secrets
- description: Create a measurement protocol secret
  method: POST
  name: create-measurement-protocol-secret
  path: /v1/measurement-protocol-secrets
- description: Get a measurement protocol secret
  method: GET
  name: get-measurement-protocol-secret
  path: /v1/measurement-protocol-secrets/{id}
personas:
- description: Integrates GA4 with other platforms and manages infrastructure.
  id: platform-engineer
  name: Platform Engineer
- description: Connects advertising platforms and implements server-side tracking.
  id: marketing-ops
  name: Marketing Operations
provider_name: Google Analytics
provider_slug: google-analytics
search_terms:
- reporting
- delete google ads link
- attribution
- manage a specific google ads link
- list google ads links on a ga4 property
- manage measurement protocol secrets
- setting up and maintaining ga4 account and property structure.
- ingesting events from servers, apps, and offline sources.
- managing data privacy, deletion, and access auditing.
- data
- web analytics
- update a google ads link
- manage google ads integration links
- list firebase links on a property
- create a google ads integration link on a ga4 property
- list measurement protocol secrets for a data stream
- create a google ads link
- data analyst
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- update google ads link
- server-side event tracking with data stream and secret management.
- integrates ga4 with other platforms and manages infrastructure.
- connects advertising platforms and implements server-side tracking.
- manages data privacy compliance including gdpr deletion requests.
- firebase
- list firebase links
- create a measurement protocol secret for server-side tracking
- extracts insights from ga4 data through reports and explorations.
- implements server-side event tracking and offline data collection.
- connecting ga4 with advertising, app, and measurement platforms.
- delete a google ads link
- list measurement protocol secrets
- list google ads links
- data protection engineer
- compliance team
- list google ads links on a property
- linking
- querying and analyzing ga4 event data through various report types.
- create a firebase link
- google
- builds automated reporting pipelines and dashboards from ga4 data.
- audits data access and monitors configuration changes.
- privacy officer
- analytics
- create measurement protocol secret
- segmenting and exporting user populations for analysis and activation.
- create, export, and query ga4 audience segments.
- google ads
- update a google ads link configuration
- get a specific measurement protocol secret
- get details of a specific measurement protocol secret
- create google ads link
- platform engineer
- bi engineer
- google analytics
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- user data deletion, access auditing, and data collection acknowledgement.
- integrations
- create firebase link
- create a measurement protocol secret
- get a measurement protocol secret
- marketing team
- backend engineer
- sets up and maintains ga4 accounts, properties, and configurations.
- manage firebase integration links
- get measurement protocol secret
- measures campaign performance, segments audiences, and tracks conversions.
- metrics
- create a firebase integration link on a ga4 property
- analytics administrator
- implements privacy-compliant data handling and deletion workflows.
- delete a google ads integration link
- machine learning
- list firebase links on a ga4 property
- marketing ops
- run standard, realtime, pivot, and batch reports with data access auditing.
slug: integrations-and-linking
tags:
- Google Analytics
- Integrations
- Firebase
- Google Ads
- Linking
tools:
- description: List Firebase links on a GA4 property
  hints:
    idempotent: true
    readOnly: true
  name: list-firebase-links
- description: Create a Firebase integration link on a GA4 property
  hints:
    idempotent: false
    readOnly: false
  name: create-firebase-link
- description: List Google Ads links on a GA4 property
  hints:
    idempotent: true
    readOnly: true
  name: list-google-ads-links
- description: Create a Google Ads integration link on a GA4 property
  hints:
    idempotent: false
    readOnly: false
  name: create-google-ads-link
- description: Update a Google Ads link configuration
  hints:
    idempotent: true
    readOnly: false
  name: update-google-ads-link
- description: Delete a Google Ads integration link
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-google-ads-link
- description: List measurement protocol secrets for a data stream
  hints:
    idempotent: true
    readOnly: true
  name: list-measurement-protocol-secrets
- description: Create a measurement protocol secret for server-side tracking
  hints:
    idempotent: false
    readOnly: false
  name: create-measurement-protocol-secret
- description: Get details of a specific measurement protocol secret
  hints:
    idempotent: true
    readOnly: true
  name: get-measurement-protocol-secret
---
