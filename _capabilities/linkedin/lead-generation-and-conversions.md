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
- lead generation
- business
- validate organization role
- get lead forms
- fetch existing conversion rules.
- manages b2b ad campaigns and audience targeting on linkedin.
- create a new conversion rule.
- tracks employee learning activity and completions.
- demand generation
- get sponsored accounts
- posts jobs and manages candidates through ats integrations.
- b2b advertising, audience targeting, and campaign analytics.
- get conversion rules
- create conversion rule
- subscribe lead notifications
- get lead forms for a sponsored account.
- integrates linkedin authentication and sharing into applications.
- social media
- professional networking
- marketing
- subscribe for lead notification webhooks.
- fetch full lead data by id.
- message archiving and regulatory communications governance.
- archives communications for regulatory compliance.
- get the user's sponsored accounts.
- pull lead form responses.
- get lead by id
- conversions
- recruiting
- validate user's organization role for lead access.
- job posting, recruiting, and applicant tracking.
- data portability and advertiser transparency for dma.
- employee development tracking and content access.
- sales intelligence, lead management, and crm integration.
- uses sales navigator for lead generation and crm sync.
- authentication, sharing, and verification for consumer apps.
- linkedin
- careers
- get lead form responses
- stream conversion events.
- stream conversion events
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
