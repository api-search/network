---
consumed_apis:
- behavioral-cohorts-api
- dashboard-rest-api
- export-api
description: Export raw event data and manage behavioral cohorts. For data analysts.
layout: capability
name: Amplitude Data Export and Cohorts
operations:
- description: Amplitude List All Cohorts
  method: GET
  name: listCohorts
  path: /v1/cohorts
- description: Amplitude Request a Cohort Export
  method: GET
  name: requestCohortExport
  path: /v1/cohorts
- description: Amplitude Get Cohort Export Status
  method: GET
  name: getCohortExportStatus
  path: /v1/cohorts
- description: Amplitude Download Cohort Export File
  method: GET
  name: downloadCohortExport
  path: /v1/cohorts
- description: Amplitude Upload a Cohort
  method: POST
  name: uploadCohort
  path: /v1/cohorts
- description: Amplitude Get Event Segmentation
  method: GET
  name: getEventSegmentation
  path: /v1/event-segmentation
- description: Amplitude Get Funnel Analysis
  method: GET
  name: getFunnelAnalysis
  path: /v1/funnel-analysis
- description: Amplitude Get Retention Analysis
  method: GET
  name: getRetentionAnalysis
  path: /v1/retention-analysis
- description: Amplitude Get User Activity
  method: GET
  name: getUserActivity
  path: /v1/user-activity
- description: Amplitude Search Users
  method: GET
  name: searchUsers
  path: /v1/user-activity
- description: Amplitude Get Revenue LTV Data
  method: GET
  name: getRevenueLTV
  path: /v1/revenue-analysis
- description: Amplitude List Event Types
  method: GET
  name: listEventTypes
  path: /v1/event-list
- description: Amplitude Export Raw Event Data
  method: GET
  name: exportEvents
  path: /v1/export
personas: []
provider_name: Amplitude
provider_slug: amplitude
search_terms:
- data export
- uploadCohort
- manage and evaluate a/b experiments and feature flags. for product managers.
- dashboard rest api getUserActivity
- data governance
- listCohorts
- downloadCohortExport
- user behavior
- amplitude request a cohort export
- amplitude
- amplitude get funnel analysis
- listEventTypes
- getCohortExportStatus
- exportEvents
- identity management
- ingests and exports event data
- getFunnelAnalysis
- unified workflow for sending events and identifying users. for data engineers.
- product analytics
- privacy compliance
- runs experiments and feature flags
- dashboard rest api getRevenueLTV
- searchUsers
- analyzes data and manages cohorts
- amplitude get event segmentation
- amplitude list all cohorts
- amplitude get revenue ltv data
- requestCohortExport
- getUserActivity
- export raw event data and manage behavioral cohorts. for data analysts.
- getEventSegmentation
- behavioral cohorts api getCohortExportStatus
- export api exportEvents
- getRevenueLTV
- behavioral cohorts api requestCohortExport
- behavioral cohorts api downloadCohortExport
- analytics
- amplitude upload a cohort
- behavioral cohorts api listCohorts
- behavioral cohorts api uploadCohort
- manage event schemas and chart annotations. for data governance teams.
- getRetentionAnalysis
- amplitude get user activity
- manages privacy and compliance
- experimentation
- dashboard rest api getRetentionAnalysis
- dashboard rest api listEventTypes
- amplitude export raw event data
- amplitude download cohort export file
- dashboard rest api getEventSegmentation
- amplitude get cohort export status
- dashboard rest api getFunnelAnalysis
- amplitude search users
- dashboard rest api searchUsers
- feature flags
- amplitude get retention analysis
- a/b testing
- scim provisioning and privacy compliance. for it admins and compliance teams.
- amplitude list event types
slug: amplitude-data-export-and-cohorts
tags:
- Amplitude
- Analytics
- Data Export
tools:
- description: Amplitude List All Cohorts
  hints:
    readOnly: true
  name: behavioral-cohorts-api-listCohorts
- description: Amplitude Request a Cohort Export
  hints:
    readOnly: true
  name: behavioral-cohorts-api-requestCohortExport
- description: Amplitude Get Cohort Export Status
  hints:
    readOnly: true
  name: behavioral-cohorts-api-getCohortExportStatus
- description: Amplitude Download Cohort Export File
  hints:
    readOnly: true
  name: behavioral-cohorts-api-downloadCohortExport
- description: Amplitude Upload a Cohort
  hints:
    readOnly: false
  name: behavioral-cohorts-api-uploadCohort
- description: Amplitude Get Event Segmentation
  hints:
    readOnly: true
  name: dashboard-rest-api-getEventSegmentation
- description: Amplitude Get Funnel Analysis
  hints:
    readOnly: true
  name: dashboard-rest-api-getFunnelAnalysis
- description: Amplitude Get Retention Analysis
  hints:
    readOnly: true
  name: dashboard-rest-api-getRetentionAnalysis
- description: Amplitude Get User Activity
  hints:
    readOnly: true
  name: dashboard-rest-api-getUserActivity
- description: Amplitude Search Users
  hints:
    readOnly: true
  name: dashboard-rest-api-searchUsers
- description: Amplitude Get Revenue LTV Data
  hints:
    readOnly: true
  name: dashboard-rest-api-getRevenueLTV
- description: Amplitude List Event Types
  hints:
    readOnly: true
  name: dashboard-rest-api-listEventTypes
- description: Amplitude Export Raw Event Data
  hints:
    readOnly: true
  name: export-api-exportEvents
---
