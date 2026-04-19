---
consumed_apis:
- ga-user-deletion-api
- ga-admin-api
description: Unified workflow for managing data privacy and compliance across Google Analytics. Combines the User Deletion API for GDPR/privacy compliance with the Admin API for data access auditing and user data collection acknowledgement. Used by privacy officers, compliance teams, and data protection engineers.
layout: capability
name: Google Analytics Compliance and Privacy
operations:
- description: Submit a user data deletion request
  method: POST
  name: upsert-user-deletion-request
  path: /v1/user-deletion-requests
- description: Report on who accessed GA4 reporting data
  method: POST
  name: run-access-report
  path: /v1/access-reports
- description: Search through account configuration changes
  method: POST
  name: search-change-history-events
  path: /v1/change-history
- description: Acknowledge user data collection terms
  method: POST
  name: acknowledge-user-data-collection
  path: /v1/data-collection-acknowledgement
personas:
- description: Manages data privacy compliance including GDPR deletion requests.
  id: privacy-officer
  name: Privacy Officer
- description: Audits data access and monitors configuration changes.
  id: compliance-team
  name: Compliance Team
- description: Implements privacy-compliant data handling and deletion workflows.
  id: data-protection-engineer
  name: Data Protection Engineer
provider_name: Google Analytics
provider_slug: google-analytics
search_terms:
- privacy officer
- audits data access and monitors configuration changes.
- sets up and maintains ga4 accounts, properties, and configurations.
- privacy
- extracts insights from ga4 data through reports and explorations.
- connecting ga4 with advertising, app, and measurement platforms.
- attribution
- acknowledge terms of user data collection for a ga4 property
- machine learning
- audit all configuration changes to an account for compliance tracking
- audit data access
- marketing ops
- run standard, realtime, pivot, and batch reports with data access auditing.
- setting up and maintaining ga4 account and property structure.
- data analyst
- integrates ga4 with other platforms and manages infrastructure.
- search change history events
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- marketing team
- compliance team
- implements server-side event tracking and offline data collection.
- reporting
- gdpr
- upsert user deletion request
- audit configuration changes
- manage user data collection acknowledgement
- acknowledge user data collection
- submit a user data deletion request for gdpr/privacy compliance
- manage user data deletion requests
- data protection engineer
- acknowledge user data collection terms
- compliance
- connects advertising platforms and implements server-side tracking.
- manages data privacy compliance including gdpr deletion requests.
- run access report
- builds automated reporting pipelines and dashboards from ga4 data.
- user data deletion, access auditing, and data collection acknowledgement.
- report on who accessed ga4 reporting data
- measures campaign performance, segments audiences, and tracks conversions.
- querying and analyzing ga4 event data through various report types.
- bi engineer
- analytics
- backend engineer
- segmenting and exporting user populations for analysis and activation.
- google analytics
- data protection
- data
- google
- platform engineer
- analytics administrator
- implements privacy-compliant data handling and deletion workflows.
- managing data privacy, deletion, and access auditing.
- search through account configuration changes
- audit who accessed google analytics reporting data and when
- server-side event tracking with data stream and secret management.
- web analytics
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- create, export, and query ga4 audience segments.
- ingesting events from servers, apps, and offline sources.
- metrics
- submit a user data deletion request
slug: compliance
tags:
- Google Analytics
- Compliance
- Privacy
- GDPR
- Data Protection
tools:
- description: Submit a user data deletion request for GDPR/privacy compliance
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: upsert-user-deletion-request
- description: Audit who accessed Google Analytics reporting data and when
  hints:
    idempotent: true
    readOnly: true
  name: run-access-report
- description: Audit all configuration changes to an account for compliance tracking
  hints:
    idempotent: true
    readOnly: true
  name: search-change-history-events
- description: Acknowledge terms of user data collection for a GA4 property
  hints:
    idempotent: true
    readOnly: false
  name: acknowledge-user-data-collection
---
