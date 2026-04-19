---
consumed_apis:
- adobe-bulk-data-insertion
- adobe-analytics
description: Unified workflow for server-side data collection and ingestion combining Bulk Data Insertion for high-volume event uploads with the Analytics API for report suite discovery and validation. Used by data engineers and implementation teams.
layout: capability
name: Adobe Analytics Data Collection
operations:
- description: Upload a batch events file.
  method: POST
  name: upload-events
  path: /v1/events
- description: Validate a batch events file without ingesting.
  method: POST
  name: validate-events
  path: /v1/events/validate
- description: List report suites to identify collection targets.
  method: GET
  name: list-report-suites
  path: /v1/report-suites
- description: Get report suite details.
  method: GET
  name: get-report-suite
  path: /v1/report-suites/{rsid}
- description: List metrics to validate event data mapping.
  method: GET
  name: list-metrics
  path: /v1/metrics
- description: List dimensions to validate event data mapping.
  method: GET
  name: list-dimensions
  path: /v1/dimensions
personas: []
provider_name: Adobe Analytics
provider_slug: adobe-analytics
search_terms:
- upload events
- validate a batch events file without ingesting data.
- server side
- adobe
- list metrics
- list report suites to identify data collection targets.
- analytics
- web analytics
- batch event upload.
- list dimensions to validate event data mapping.
- business intelligence
- list report suites
- report suite discovery for data collection targeting.
- list metrics to validate event data mapping.
- customer intelligence
- metric discovery for event mapping.
- upload a gzip-compressed csv file of batched analytics event data.
- digital marketing
- data collection
- list dimensions
- validate a batch events file without ingesting.
- list available metrics to validate event data mapping.
- upload a batch events file.
- report suite details.
- get report suite details.
- marketing
- validate events
- validate event files.
- list available dimensions to validate event data mapping.
- adobe analytics
- bulk data insertion
- list report suites to identify collection targets.
- get details for a report suite to verify collection configuration.
- events
- get report suite
- dimension discovery for event mapping.
slug: data-collection
tags:
- Adobe Analytics
- Data Collection
- Bulk Data Insertion
- Events
- Server Side
tools:
- description: Upload a gzip-compressed CSV file of batched Analytics event data.
  hints:
    idempotent: false
    readOnly: false
  name: upload-events
- description: Validate a batch events file without ingesting data.
  hints:
    idempotent: true
    readOnly: true
  name: validate-events
- description: List report suites to identify data collection targets.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-report-suites
- description: Get details for a report suite to verify collection configuration.
  hints:
    idempotent: true
    readOnly: true
  name: get-report-suite
- description: List available metrics to validate event data mapping.
  hints:
    idempotent: true
    readOnly: true
  name: list-metrics
- description: List available dimensions to validate event data mapping.
  hints:
    idempotent: true
    readOnly: true
  name: list-dimensions
---
