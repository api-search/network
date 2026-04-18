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
- submit a user data deletion request
- backend engineer
- implements server-side event tracking and offline data collection.
- privacy officer
- upsert user deletion request
- manages data privacy compliance including gdpr deletion requests.
- create, export, and query ga4 audience segments.
- extracts insights from ga4 data through reports and explorations.
- search change history events
- querying and analyzing ga4 event data through various report types.
- user data deletion, access auditing, and data collection acknowledgement.
- analytics
- metrics
- privacy
- audit all configuration changes to an account for compliance tracking
- google
- gdpr
- compliance
- ingesting events from servers, apps, and offline sources.
- web analytics
- marketing team
- run access report
- setting up and maintaining ga4 account and property structure.
- marketing ops
- audit data access
- bi engineer
- audit who accessed google analytics reporting data and when
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- server-side event tracking with data stream and secret management.
- data analyst
- integrates ga4 with other platforms and manages infrastructure.
- connects advertising platforms and implements server-side tracking.
- audits data access and monitors configuration changes.
- compliance team
- acknowledge user data collection terms
- implements privacy-compliant data handling and deletion workflows.
- acknowledge user data collection
- attribution
- run standard, realtime, pivot, and batch reports with data access auditing.
- acknowledge terms of user data collection for a ga4 property
- manage user data collection acknowledgement
- segmenting and exporting user populations for analysis and activation.
- audit configuration changes
- builds automated reporting pipelines and dashboards from ga4 data.
- connecting ga4 with advertising, app, and measurement platforms.
- data protection engineer
- analytics administrator
- data protection
- manage user data deletion requests
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- search through account configuration changes
- measures campaign performance, segments audiences, and tracks conversions.
- submit a user data deletion request for gdpr/privacy compliance
- sets up and maintains ga4 accounts, properties, and configurations.
- platform engineer
- managing data privacy, deletion, and access auditing.
- data
- google analytics
- reporting
- machine learning
- report on who accessed ga4 reporting data
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
