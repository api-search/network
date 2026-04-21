---
consumed_apis:
- ga-admin-api
description: Unified workflow for managing GA4 property configuration including accounts, properties, data streams, custom dimensions and metrics, conversion events, and integration links. Used by analytics administrators and platform engineers to set up and maintain GA4 properties.
layout: capability
name: Google Analytics Configuration Management
operations:
- description: List all accessible accounts
  method: GET
  name: list-accounts
  path: /v1/accounts
- description: List summaries of all accessible accounts
  method: GET
  name: list-account-summaries
  path: /v1/account-summaries
- description: List GA4 properties
  method: GET
  name: list-properties
  path: /v1/properties
- description: Create a GA4 property
  method: POST
  name: create-property
  path: /v1/properties
- description: List data streams on a property
  method: GET
  name: list-data-streams
  path: /v1/data-streams
- description: Create a data stream
  method: POST
  name: create-data-stream
  path: /v1/data-streams
- description: List custom dimensions
  method: GET
  name: list-custom-dimensions
  path: /v1/custom-dimensions
- description: Create a custom dimension
  method: POST
  name: create-custom-dimension
  path: /v1/custom-dimensions
- description: List custom metrics
  method: GET
  name: list-custom-metrics
  path: /v1/custom-metrics
- description: Create a custom metric
  method: POST
  name: create-custom-metric
  path: /v1/custom-metrics
- description: List conversion events
  method: GET
  name: list-conversion-events
  path: /v1/conversion-events
- description: Create a conversion event
  method: POST
  name: create-conversion-event
  path: /v1/conversion-events
- description: Search through account changes
  method: POST
  name: search-change-history-events
  path: /v1/change-history
personas:
- description: Sets up and maintains GA4 accounts, properties, and configurations.
  id: analytics-administrator
  name: Analytics Administrator
- description: Integrates GA4 with other platforms and manages infrastructure.
  id: platform-engineer
  name: Platform Engineer
provider_name: Google Analytics
provider_slug: google-analytics
search_terms:
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- platform engineer
- archive a custom metric on a property
- reporting
- implements privacy-compliant data handling and deletion workflows.
- implements server-side event tracking and offline data collection.
- list conversion events on a property
- compliance team
- create a custom metric
- create property
- list all accessible accounts
- list summaries of all accessible accounts
- management
- acknowledge user data collection
- list custom dimensions on a property
- create a ga4 property
- analytics administrator
- manage custom metrics
- list account summaries
- manage conversion events
- search change history events
- server-side event tracking with data stream and secret management.
- search change history
- acknowledge terms of user data collection for a property
- builds automated reporting pipelines and dashboards from ga4 data.
- create data stream
- admin
- create a conversion event on a property
- create custom metric
- managing data privacy, deletion, and access auditing.
- list data streams on a property
- list summaries of all accessible accounts with their properties
- google
- list all accessible google analytics accounts
- request a ticket for creating a new account
- list custom metrics on a property
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- querying and analyzing ga4 event data through various report types.
- list data streams
- manage ga4 accounts
- attribution
- list properties
- setting up and maintaining ga4 account and property structure.
- create a custom dimension on a property
- web analytics
- archive custom metric
- create a data stream
- bi engineer
- manage data streams
- list ga4 properties
- user data deletion, access auditing, and data collection acknowledgement.
- ingesting events from servers, apps, and offline sources.
- list accounts
- machine learning
- marketing ops
- segmenting and exporting user populations for analysis and activation.
- privacy officer
- extracts insights from ga4 data through reports and explorations.
- view account summaries
- list ga4 properties for an account
- create, export, and query ga4 audience segments.
- connects advertising platforms and implements server-side tracking.
- data protection engineer
- google analytics
- marketing team
- create a conversion event
- audits data access and monitors configuration changes.
- sets up and maintains ga4 accounts, properties, and configurations.
- data analyst
- search through all changes to an account or its children
- ga4
- search through account changes
- provision account ticket
- analytics
- manages data privacy compliance including gdpr deletion requests.
- create custom dimension
- list conversion events
- create a new ga4 property
- configuration
- list custom metrics
- manage custom dimensions
- manage ga4 properties
- run standard, realtime, pivot, and batch reports with data access auditing.
- create conversion event
- metrics
- list custom dimensions
- connecting ga4 with advertising, app, and measurement platforms.
- backend engineer
- create a new data stream on a property
- create a custom dimension
- integrates ga4 with other platforms and manages infrastructure.
- data
- measures campaign performance, segments audiences, and tracks conversions.
- create a custom metric on a property
slug: configuration-management
tags:
- Google Analytics
- Configuration
- Admin
- Management
- GA4
tools:
- description: List all accessible Google Analytics accounts
  hints:
    idempotent: true
    readOnly: true
  name: list-accounts
- description: List summaries of all accessible accounts with their properties
  hints:
    idempotent: true
    readOnly: true
  name: list-account-summaries
- description: Request a ticket for creating a new account
  hints:
    idempotent: false
    readOnly: false
  name: provision-account-ticket
- description: List GA4 properties for an account
  hints:
    idempotent: true
    readOnly: true
  name: list-properties
- description: Create a new GA4 property
  hints:
    idempotent: false
    readOnly: false
  name: create-property
- description: List data streams on a property
  hints:
    idempotent: true
    readOnly: true
  name: list-data-streams
- description: Create a new data stream on a property
  hints:
    idempotent: false
    readOnly: false
  name: create-data-stream
- description: List custom dimensions on a property
  hints:
    idempotent: true
    readOnly: true
  name: list-custom-dimensions
- description: Create a custom dimension on a property
  hints:
    idempotent: false
    readOnly: false
  name: create-custom-dimension
- description: List custom metrics on a property
  hints:
    idempotent: true
    readOnly: true
  name: list-custom-metrics
- description: Create a custom metric on a property
  hints:
    idempotent: false
    readOnly: false
  name: create-custom-metric
- description: Archive a custom metric on a property
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: archive-custom-metric
- description: List conversion events on a property
  hints:
    idempotent: true
    readOnly: true
  name: list-conversion-events
- description: Create a conversion event on a property
  hints:
    idempotent: false
    readOnly: false
  name: create-conversion-event
- description: Search through all changes to an account or its children
  hints:
    idempotent: true
    readOnly: true
  name: search-change-history-events
- description: Acknowledge terms of user data collection for a property
  hints:
    idempotent: true
    readOnly: false
  name: acknowledge-user-data-collection
---
