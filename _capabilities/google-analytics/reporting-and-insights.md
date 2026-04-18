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
- manage accounts, properties, data streams, custom dimensions/metrics, and conversion events.
- extracts insights from ga4 data through reports and explorations.
- marketing ops
- create, export, and query ga4 audience segments.
- integrates ga4 with other platforms and manages infrastructure.
- ga4
- run up to 5 reports in a batch
- analytics
- google analytics
- check compatibility
- run access report
- platform engineer
- managing data privacy, deletion, and access auditing.
- run pivot report
- check if dimensions and metrics are compatible for a report
- backend engineer
- run realtime report
- measures campaign performance, segments audiences, and tracks conversions.
- run multiple reports in a single batch request
- marketing team
- manages data privacy compliance including gdpr deletion requests.
- run standard ga4 reports
- run a customized pivot report
- run up to 5 pivot reports in a batch
- run up to 5 pivot reports in a single batch request
- user data deletion, access auditing, and data collection acknowledgement.
- run a realtime report showing events from the last 30 minutes
- data protection engineer
- sets up and maintains ga4 accounts, properties, and configurations.
- ingesting events from servers, apps, and offline sources.
- report on who accessed ga4 reporting data
- querying and analyzing ga4 event data through various report types.
- setting up and maintaining ga4 account and property structure.
- metrics
- run standard, realtime, pivot, and batch reports with data access auditing.
- privacy officer
- check dimension and metric compatibility
- bi engineer
- connect ga4 with firebase, google ads, and manage measurement protocol secrets.
- builds automated reporting pipelines and dashboards from ga4 data.
- run a customized report of ga4 event data
- run up to 5 standard reports in a single batch request
- implements privacy-compliant data handling and deletion workflows.
- implements server-side event tracking and offline data collection.
- batch run reports
- run realtime ga4 reports
- run pivot reports for cross-tabulation analysis
- verify dimensions and metrics can be used together
- attribution
- report on who accessed ga4 reporting data and when
- data
- reporting
- connects advertising platforms and implements server-side tracking.
- machine learning
- data analyst
- segmenting and exporting user populations for analysis and activation.
- server-side event tracking with data stream and secret management.
- run data access audit reports
- connecting ga4 with advertising, app, and measurement platforms.
- audits data access and monitors configuration changes.
- run an advanced pivot table report for cross-tabulation analysis
- google
- insights
- run a standard ga4 report with dimensions, metrics, and date ranges
- run report
- batch run pivot reports
- web analytics
- run multiple pivot reports in a single batch
- analytics administrator
- compliance team
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
