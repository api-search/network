---
consumed_apis:
- sales-navigator
description: Unified workflow for sales representatives to manage Sales Navigator contracts, export analytics, associate CRM profiles, and validate CRM data.
layout: capability
name: LinkedIn Sales Engagement
operations:
- description: Find all contracts where user has an active seat.
  method: GET
  name: get-contracts
  path: /v1/sales-contracts
- description: Create sales analytics export job.
  method: POST
  name: create-export-job
  path: /v1/sales-analytics-export-jobs
- description: Fetch export job status.
  method: GET
  name: get-export-job
  path: /v1/sales-analytics-export-jobs/{JobId}
- description: Get sales access token.
  method: GET
  name: get-sales-access-token
  path: /v1/sales-access-tokens
- description: Batch fetch profile associations.
  method: GET
  name: batch-get-profile-associations
  path: /v1/profile-associations
- description: Create CRM data validation job.
  method: POST
  name: create-crm-validation-job
  path: /v1/crm-validation-jobs
- description: Get CRM validation job status.
  method: GET
  name: get-crm-validation-job
  path: /v1/crm-validation-jobs/{JobId}
personas: []
provider_name: LinkedIn
provider_slug: linkedin
search_terms:
- get crm validation job status.
- business
- create new sales analytics export job.
- manages b2b ad campaigns and audience targeting on linkedin.
- get sales access token.
- create export job
- sales
- get contracts
- sales navigator
- tracks employee learning activity and completions.
- posts jobs and manages candidates through ats integrations.
- b2b advertising, audience targeting, and campaign analytics.
- create crm validation job
- crm integration
- integrates linkedin authentication and sharing into applications.
- social media
- professional networking
- create crm data validation export job.
- get export job
- marketing
- retrieve sales access token.
- message archiving and regulatory communications governance.
- fetch sales analytics export job by id.
- archives communications for regulatory compliance.
- create crm data validation job.
- batch get profile associations
- get sales access token
- fetch export job status.
- get crm data validation export job status.
- recruiting
- create sales analytics export job.
- job posting, recruiting, and applicant tracking.
- find all contracts where user has an active seat.
- data portability and advertiser transparency for dma.
- employee development tracking and content access.
- sales intelligence, lead management, and crm integration.
- batch fetch profile associations from crm records.
- uses sales navigator for lead generation and crm sync.
- linkedin
- get crm validation job
- careers
- batch fetch profile associations.
- authentication, sharing, and verification for consumer apps.
slug: sales-engagement
tags:
- LinkedIn
- Sales Navigator
- CRM Integration
- Sales
tools:
- description: Find all contracts where user has an active seat.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-contracts
- description: Create new sales analytics export job.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-export-job
- description: Fetch sales analytics export job by ID.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-export-job
- description: Retrieve sales access token.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-sales-access-token
- description: Batch fetch profile associations from CRM records.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: batch-get-profile-associations
- description: Create CRM data validation export job.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-crm-validation-job
- description: Get CRM data validation export job status.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-crm-validation-job
---
