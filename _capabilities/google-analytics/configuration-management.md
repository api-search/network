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
- list all accessible accounts
- attribution
- managing data privacy, deletion, and access auditing.
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- connects advertising platforms and implements server-side tracking.
- extracts insights from ga4 data through reports and explorations.
- list summaries of all accessible accounts
- connecting ga4 with advertising, app, and measurement platforms.
- list custom dimensions
- create data stream
- google
- analytics
- create property
- manage data streams
- create a new ga4 property
- platform engineer
- google analytics
- search through all changes to an account or its children
- list data streams
- manage ga4 properties
- list conversion events on a property
- run standard, realtime, pivot, and batch reports with data access auditing.
- manage conversion events
- list custom metrics on a property
- list custom dimensions on a property
- integrates ga4 with other platforms and manages infrastructure.
- data analyst
- archive custom metric
- data protection engineer
- list properties
- view account summaries
- create a custom metric
- privacy officer
- list ga4 properties
- create, export, and query ga4 audience segments.
- create a custom dimension on a property
- search change history events
- sets up and maintains ga4 accounts, properties, and configurations.
- create a conversion event on a property
- search change history
- bi engineer
- create a new data stream on a property
- data
- list custom metrics
- configuration
- implements server-side event tracking and offline data collection.
- list data streams on a property
- list accounts
- create a custom dimension
- manage ga4 accounts
- querying and analyzing ga4 event data through various report types.
- management
- builds automated reporting pipelines and dashboards from ga4 data.
- search through account changes
- request a ticket for creating a new account
- list conversion events
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- list ga4 properties for an account
- marketing team
- backend engineer
- measures campaign performance, segments audiences, and tracks conversions.
- provision account ticket
- acknowledge terms of user data collection for a property
- create custom dimension
- implements privacy-compliant data handling and deletion workflows.
- reporting
- ga4
- setting up and maintaining ga4 account and property structure.
- ingesting events from servers, apps, and offline sources.
- web analytics
- server-side event tracking with data stream and secret management.
- acknowledge user data collection
- create a custom metric on a property
- manages data privacy compliance including gdpr deletion requests.
- manage custom dimensions
- list all accessible google analytics accounts
- compliance team
- manage custom metrics
- audits data access and monitors configuration changes.
- create custom metric
- segmenting and exporting user populations for analysis and activation.
- create conversion event
- create a ga4 property
- admin
- user data deletion, access auditing, and data collection acknowledgement.
- create a data stream
- archive a custom metric on a property
- analytics administrator
- metrics
- list summaries of all accessible accounts with their properties
- machine learning
- list account summaries
- marketing ops
- create a conversion event
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
