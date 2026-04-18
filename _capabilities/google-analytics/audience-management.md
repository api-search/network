---
consumed_apis:
- ga-data-api
- ga-admin-api
description: Unified workflow for creating, exporting, and analyzing GA4 audiences. Combines the Data API audience export capabilities with Admin API property configuration. Used by marketing teams and data analysts for audience segmentation, export, and activation.
layout: capability
name: Google Analytics Audience Management
operations:
- description: Create an audience export
  method: POST
  name: create-audience-export
  path: /v1/audience-exports
- description: List audience exports
  method: GET
  name: list-audience-exports
  path: /v1/audience-exports
- description: Get audience export details
  method: GET
  name: get-audience-export
  path: /v1/audience-exports/{id}
- description: Query users from an audience export
  method: POST
  name: query-audience-export
  path: /v1/audience-exports/{id}/users
- description: List GA4 properties
  method: GET
  name: list-properties
  path: /v1/properties
personas:
- description: Measures campaign performance, segments audiences, and tracks conversions.
  id: marketing-team
  name: Marketing Team
- description: Extracts insights from GA4 data through reports and explorations.
  id: data-analyst
  name: Data Analyst
provider_name: Google Analytics
provider_slug: google-analytics
search_terms:
- backend engineer
- implements server-side event tracking and offline data collection.
- privacy officer
- querying and analyzing ga4 event data through various report types.
- create, export, and query ga4 audience segments.
- list ga4 properties
- extracts insights from ga4 data through reports and explorations.
- analytics
- user data deletion, access auditing, and data collection acknowledgement.
- metrics
- google
- get audience export
- web analytics
- ingesting events from servers, apps, and offline sources.
- list properties
- marketing team
- retrieve users from an audience export
- create and list audience exports
- list properties for audience context
- get a specific audience export
- query audience export
- setting up and maintaining ga4 account and property structure.
- retrieve users from a completed audience export
- marketing ops
- bi engineer
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- server-side event tracking with data stream and secret management.
- integrates ga4 with other platforms and manages infrastructure.
- marketing
- data analyst
- connects advertising platforms and implements server-side tracking.
- audits data access and monitors configuration changes.
- implements privacy-compliant data handling and deletion workflows.
- compliance team
- list audience exports
- attribution
- query users from an audience export
- run standard, realtime, pivot, and batch reports with data access auditing.
- segmenting and exporting user populations for analysis and activation.
- builds automated reporting pipelines and dashboards from ga4 data.
- connecting ga4 with advertising, app, and measurement platforms.
- data protection engineer
- create an audience export for a ga4 property
- create audience export
- analytics administrator
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- export
- audiences
- segmentation
- list all audience exports for a property
- measures campaign performance, segments audiences, and tracks conversions.
- sets up and maintains ga4 accounts, properties, and configurations.
- get audience export details
- platform engineer
- get metadata about a specific audience export
- managing data privacy, deletion, and access auditing.
- google analytics
- data
- create an audience export
- reporting
- machine learning
- list ga4 properties to identify available audiences
- manages data privacy compliance including gdpr deletion requests.
slug: audience-management
tags:
- Google Analytics
- Audiences
- Segmentation
- Export
- Marketing
tools:
- description: Create an audience export for a GA4 property
  hints:
    idempotent: false
    readOnly: false
  name: create-audience-export
- description: Get metadata about a specific audience export
  hints:
    idempotent: true
    readOnly: true
  name: get-audience-export
- description: List all audience exports for a property
  hints:
    idempotent: true
    readOnly: true
  name: list-audience-exports
- description: Retrieve users from a completed audience export
  hints:
    idempotent: true
    readOnly: true
  name: query-audience-export
- description: List GA4 properties to identify available audiences
  hints:
    idempotent: true
    readOnly: true
  name: list-properties
---
