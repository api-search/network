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
- list ga4 properties
- query audience export
- integrates ga4 with other platforms and manages infrastructure.
- segmentation
- data analyst
- export
- extracts insights from ga4 data through reports and explorations.
- list all audience exports for a property
- connects advertising platforms and implements server-side tracking.
- segmenting and exporting user populations for analysis and activation.
- web analytics
- analytics administrator
- list audience exports
- backend engineer
- metrics
- platform engineer
- setting up and maintaining ga4 account and property structure.
- attribution
- bi engineer
- google analytics
- user data deletion, access auditing, and data collection acknowledgement.
- manages data privacy compliance including gdpr deletion requests.
- list properties for audience context
- reporting
- run standard, realtime, pivot, and batch reports with data access auditing.
- marketing
- retrieve users from an audience export
- create, export, and query ga4 audience segments.
- query users from an audience export
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- privacy officer
- ingesting events from servers, apps, and offline sources.
- retrieve users from a completed audience export
- list ga4 properties to identify available audiences
- analytics
- get audience export
- marketing ops
- sets up and maintains ga4 accounts, properties, and configurations.
- querying and analyzing ga4 event data through various report types.
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- server-side event tracking with data stream and secret management.
- create and list audience exports
- data protection engineer
- audits data access and monitors configuration changes.
- google
- list properties
- implements server-side event tracking and offline data collection.
- marketing team
- compliance team
- get a specific audience export
- implements privacy-compliant data handling and deletion workflows.
- connecting ga4 with advertising, app, and measurement platforms.
- builds automated reporting pipelines and dashboards from ga4 data.
- audiences
- get audience export details
- data
- create an audience export
- get metadata about a specific audience export
- create an audience export for a ga4 property
- measures campaign performance, segments audiences, and tracks conversions.
- managing data privacy, deletion, and access auditing.
- machine learning
- create audience export
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
