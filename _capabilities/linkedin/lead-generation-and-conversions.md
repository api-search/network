---
consumed_apis:
- marketing-leads
- marketing-conversions
description: Unified workflow for demand generation managers to capture leads, sync lead data, track conversions, and measure attribution -- combining lead sync and conversions APIs.
layout: capability
name: LinkedIn Lead Generation And Conversions
operations:
- description: Get lead forms for a sponsored account.
  method: GET
  name: get-lead-forms
  path: /v1/lead-forms
- description: Pull lead form responses.
  method: GET
  name: get-lead-form-responses
  path: /v1/lead-form-responses
- description: Fetch full lead data by ID.
  method: GET
  name: get-lead-by-id
  path: /v1/lead-form-responses/{lead_id}
- description: Subscribe for lead notification webhooks.
  method: POST
  name: subscribe-lead-notifications
  path: /v1/lead-notifications
- description: Fetch existing conversion rules.
  method: GET
  name: get-conversion-rules
  path: /v1/conversions
- description: Create a new conversion rule.
  method: POST
  name: create-conversion-rule
  path: /v1/conversions
- description: Stream conversion events.
  method: POST
  name: stream-conversion-events
  path: /v1/conversion-events
personas: []
provider_name: LinkedIn
provider_slug: linkedin
search_terms:
- business
- subscribe for lead notification webhooks.
- b2b advertising, audience targeting, and campaign analytics.
- sales intelligence, lead management, and crm integration.
- job posting, recruiting, and applicant tracking.
- subscribe lead notifications
- lead generation
- demand generation
- uses sales navigator for lead generation and crm sync.
- archives communications for regulatory compliance.
- message archiving and regulatory communications governance.
- stream conversion events
- validate user's organization role for lead access.
- careers
- get sponsored accounts
- manages b2b ad campaigns and audience targeting on linkedin.
- get lead form responses
- linkedin
- recruiting
- stream conversion events.
- get conversion rules
- get the user's sponsored accounts.
- conversions
- get lead forms
- authentication, sharing, and verification for consumer apps.
- professional networking
- fetch existing conversion rules.
- create a new conversion rule.
- get lead by id
- validate organization role
- posts jobs and manages candidates through ats integrations.
- marketing
- social media
- fetch full lead data by id.
- get lead forms for a sponsored account.
- pull lead form responses.
- create conversion rule
- data portability and advertiser transparency for dma.
- tracks employee learning activity and completions.
- integrates linkedin authentication and sharing into applications.
- employee development tracking and content access.
slug: lead-generation-and-conversions
tags:
- LinkedIn
- Lead Generation
- Conversions
- Demand Generation
tools:
- description: Validate user's organization role for lead access.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: validate-organization-role
- description: Get the user's sponsored accounts.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-sponsored-accounts
- description: Get lead forms for a sponsored account.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-lead-forms
- description: Pull lead form responses.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-lead-form-responses
- description: Fetch full lead data by ID.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-lead-by-id
- description: Subscribe for lead notification webhooks.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: subscribe-lead-notifications
- description: Fetch existing conversion rules.
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-conversion-rules
- description: Create a new conversion rule.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-conversion-rule
- description: Stream conversion events.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: stream-conversion-events
---
