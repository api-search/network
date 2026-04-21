---
consumed_apis:
- compliance-events
- data-portability
- ads-transparency
description: Unified workflow for compliance officers to monitor regulated communications, export data for portability compliance, and access ads transparency data -- combining compliance events, data portability, and ads transparency APIs.
layout: capability
name: LinkedIn Compliance And Regulatory
operations:
- description: Opt in a member for compliance monitoring.
  method: POST
  name: opt-in-member
  path: /v1/compliance-authorizations
- description: Check member compliance monitoring status.
  method: GET
  name: check-member-status
  path: /v1/compliance-authorizations
- description: Retrieve compliance events.
  method: GET
  name: get-compliance-events
  path: /v1/compliance-events
- description: Batch get organizations for data portability.
  method: GET
  name: batch-get-organizations
  path: /v1/dma-organizations
- description: Get organization by ID.
  method: GET
  name: get-organization
  path: /v1/dma-organizations/{organizationId}
- description: Get posts for data portability.
  method: GET
  name: get-dma-posts
  path: /v1/dma-posts
- description: Get reactions for data portability.
  method: GET
  name: get-dma-reactions
  path: /v1/dma-reactions
- description: Get comments for data portability.
  method: GET
  name: get-dma-comments
  path: /v1/dma-comments
- description: Get events for data portability.
  method: GET
  name: get-dma-events
  path: /v1/dma-events
- description: Get advertiser transparency data.
  method: GET
  name: get-advertiser-transparency
  path: /v1/advertiser-transparency/{sponsoredaccount_id}
personas: []
provider_name: LinkedIn
provider_slug: linkedin
search_terms:
- business
- opt in a member for compliance monitoring.
- get advertiser transparency data for a sponsored account.
- b2b advertising, audience targeting, and campaign analytics.
- sales intelligence, lead management, and crm integration.
- compliance
- data portability
- job posting, recruiting, and applicant tracking.
- get organization by id.
- get posts for data portability.
- check member status
- opt out member
- uses sales navigator for lead generation and crm sync.
- archives communications for regulatory compliance.
- get business manager account relationships.
- message archiving and regulatory communications governance.
- get page content analytics
- careers
- manages b2b ad campaigns and audience targeting on linkedin.
- get dma lead gen responses
- get business manager relationships
- linkedin
- get organization by id for data portability.
- recruiting
- retrieve compliance events.
- get organization
- get dma comments
- opt in member
- get events for data portability.
- get reactions for data portability.
- opt out a member from compliance monitoring.
- get comments for data portability.
- authentication, sharing, and verification for consumer apps.
- check member compliance monitoring status.
- professional networking
- get lead gen responses for data portability.
- get dma posts
- get organization acls for data portability.
- batch get organizations for data portability.
- get compliance events
- get advertiser transparency data.
- posts jobs and manages candidates through ats integrations.
- marketing
- regulatory
- social media
- batch get organizations
- retrieve compliance events for a regulated member.
- get dma reactions
- data portability and advertiser transparency for dma.
- get organization acls
- get advertiser transparency
- get page content analytics for data portability.
- tracks employee learning activity and completions.
- integrates linkedin authentication and sharing into applications.
- get dma events
- employee development tracking and content access.
slug: compliance-and-regulatory
tags:
- LinkedIn
- Compliance
- Regulatory
- Data Portability
tools:
- description: Opt in a member for compliance monitoring.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: opt-in-member
- description: Check member compliance monitoring status.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: check-member-status
- description: Opt out a member from compliance monitoring.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: opt-out-member
- description: Retrieve compliance events for a regulated member.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-compliance-events
- description: Batch get organizations for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: batch-get-organizations
- description: Get organization by ID for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-organization
- description: Get organization ACLs for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-organization-acls
- description: Get page content analytics for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-page-content-analytics
- description: Get posts for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-dma-posts
- description: Get reactions for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-dma-reactions
- description: Get comments for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-dma-comments
- description: Get lead gen responses for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-dma-lead-gen-responses
- description: Get events for data portability.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-dma-events
- description: Get business manager account relationships.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-business-manager-relationships
- description: Get advertiser transparency data for a sponsored account.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-advertiser-transparency
---
