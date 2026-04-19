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
- privacy officer
- audits data access and monitors configuration changes.
- get metadata about a specific audience export
- sets up and maintains ga4 accounts, properties, and configurations.
- extracts insights from ga4 data through reports and explorations.
- connecting ga4 with advertising, app, and measurement platforms.
- list all audience exports for a property
- attribution
- machine learning
- create and list audience exports
- marketing ops
- list ga4 properties
- run standard, realtime, pivot, and batch reports with data access auditing.
- setting up and maintaining ga4 account and property structure.
- create an audience export
- data analyst
- audiences
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- integrates ga4 with other platforms and manages infrastructure.
- marketing team
- get audience export details
- compliance team
- implements server-side event tracking and offline data collection.
- retrieve users from a completed audience export
- reporting
- get a specific audience export
- create audience export
- segmentation
- ingesting events from servers, apps, and offline sources.
- query audience export
- marketing
- data protection engineer
- connects advertising platforms and implements server-side tracking.
- manages data privacy compliance including gdpr deletion requests.
- list properties
- builds automated reporting pipelines and dashboards from ga4 data.
- query users from an audience export
- user data deletion, access auditing, and data collection acknowledgement.
- list properties for audience context
- measures campaign performance, segments audiences, and tracks conversions.
- querying and analyzing ga4 event data through various report types.
- bi engineer
- analytics
- backend engineer
- export
- segmenting and exporting user populations for analysis and activation.
- google analytics
- get audience export
- data
- google
- list audience exports
- platform engineer
- analytics administrator
- retrieve users from an audience export
- implements privacy-compliant data handling and deletion workflows.
- managing data privacy, deletion, and access auditing.
- web analytics
- server-side event tracking with data stream and secret management.
- list ga4 properties to identify available audiences
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- create, export, and query ga4 audience segments.
- create an audience export for a ga4 property
- metrics
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
