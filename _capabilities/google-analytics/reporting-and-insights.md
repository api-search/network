---
consumed_apis:
- ga-data-api
- ga-admin-api
description: Unified reporting workflow combining the Data API for running standard, realtime, and pivot reports with the Admin API for accessing data access audit reports. Used by data analysts, marketing teams, and BI engineers to extract insights from GA4 properties.
layout: capability
name: Google Analytics Reporting and Insights
operations:
- description: Run a customized report of GA4 event data
  method: POST
  name: run-report
  path: /v1/reports
- description: Run a realtime report showing events from the last 30 minutes
  method: POST
  name: run-realtime-report
  path: /v1/reports/realtime
- description: Run a customized pivot report
  method: POST
  name: run-pivot-report
  path: /v1/reports/pivot
- description: Run up to 5 reports in a batch
  method: POST
  name: batch-run-reports
  path: /v1/reports/batch
- description: Run up to 5 pivot reports in a batch
  method: POST
  name: batch-run-pivot-reports
  path: /v1/reports/pivot/batch
- description: Verify dimensions and metrics can be used together
  method: POST
  name: check-compatibility
  path: /v1/compatibility
- description: Report on who accessed GA4 reporting data
  method: POST
  name: run-access-report
  path: /v1/access-reports
personas:
- description: Extracts insights from GA4 data through reports and explorations.
  id: data-analyst
  name: Data Analyst
- description: Measures campaign performance, segments audiences, and tracks conversions.
  id: marketing-team
  name: Marketing Team
- description: Builds automated reporting pipelines and dashboards from GA4 data.
  id: bi-engineer
  name: BI Engineer
provider_name: Google Analytics
provider_slug: google-analytics
search_terms:
- check dimension and metric compatibility
- reporting
- attribution
- insights
- ga4
- setting up and maintaining ga4 account and property structure.
- ingesting events from servers, apps, and offline sources.
- managing data privacy, deletion, and access auditing.
- data
- run a realtime report showing events from the last 30 minutes
- web analytics
- run realtime report
- verify dimensions and metrics can be used together
- server-side event tracking with data stream and secret management.
- integrates ga4 with other platforms and manages infrastructure.
- batch run reports
- check if dimensions and metrics are compatible for a report
- report on who accessed ga4 reporting data
- data analyst
- batch run pivot reports
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- run multiple pivot reports in a single batch
- connects advertising platforms and implements server-side tracking.
- manages data privacy compliance including gdpr deletion requests.
- extracts insights from ga4 data through reports and explorations.
- implements server-side event tracking and offline data collection.
- run pivot report
- run a standard ga4 report with dimensions, metrics, and date ranges
- connecting ga4 with advertising, app, and measurement platforms.
- run multiple reports in a single batch request
- data protection engineer
- compliance team
- querying and analyzing ga4 event data through various report types.
- google
- run up to 5 standard reports in a single batch request
- report on who accessed ga4 reporting data and when
- builds automated reporting pipelines and dashboards from ga4 data.
- privacy officer
- analytics
- audits data access and monitors configuration changes.
- segmenting and exporting user populations for analysis and activation.
- create, export, and query ga4 audience segments.
- run up to 5 reports in a batch
- run an advanced pivot table report for cross-tabulation analysis
- platform engineer
- bi engineer
- google analytics
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- run up to 5 pivot reports in a batch
- run data access audit reports
- user data deletion, access auditing, and data collection acknowledgement.
- run report
- run a customized report of ga4 event data
- run realtime ga4 reports
- run pivot reports for cross-tabulation analysis
- run a customized pivot report
- run up to 5 pivot reports in a single batch request
- marketing team
- backend engineer
- sets up and maintains ga4 accounts, properties, and configurations.
- run standard ga4 reports
- measures campaign performance, segments audiences, and tracks conversions.
- metrics
- analytics administrator
- implements privacy-compliant data handling and deletion workflows.
- machine learning
- check compatibility
- run access report
- marketing ops
- run standard, realtime, pivot, and batch reports with data access auditing.
slug: reporting-and-insights
tags:
- Google Analytics
- Reporting
- Analytics
- Insights
- GA4
tools:
- description: Run a standard GA4 report with dimensions, metrics, and date ranges
  hints:
    idempotent: true
    readOnly: true
  name: run-report
- description: Run a realtime report showing events from the last 30 minutes
  hints:
    idempotent: true
    readOnly: true
  name: run-realtime-report
- description: Run an advanced pivot table report for cross-tabulation analysis
  hints:
    idempotent: true
    readOnly: true
  name: run-pivot-report
- description: Run up to 5 standard reports in a single batch request
  hints:
    idempotent: true
    readOnly: true
  name: batch-run-reports
- description: Run up to 5 pivot reports in a single batch request
  hints:
    idempotent: true
    readOnly: true
  name: batch-run-pivot-reports
- description: Check if dimensions and metrics are compatible for a report
  hints:
    idempotent: true
    readOnly: true
  name: check-compatibility
- description: Report on who accessed GA4 reporting data and when
  hints:
    idempotent: true
    readOnly: true
  name: run-access-report
---
