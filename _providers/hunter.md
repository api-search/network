---
api_count: 13
apis:
- description: Returns all the email addresses found using a given domain name, with sources.
  name: Hunter Domain Search API
  slug: domain-search
- description: Generates the most likely email address from a domain name, a first name and a last name.
  name: Hunter Email Finder API
  slug: email-finder
- description: Verifies the deliverability of a given email address.
  name: Hunter Email Verifier API
  slug: email-verifier
- description: Returns the number of email addresses found for a given domain.
  name: Hunter Email Count API
  slug: email-count
- description: Returns information about the account associated with the API key.
  name: Hunter Account API
  slug: account
- description: Returns companies matching a set of criteria using natural language queries or robust filters to find companies aligned with your ideal customer profile.
  name: Hunter Discover API
  slug: discover
- description: Returns comprehensive personal information linked to an email address or LinkedIn profile, providing enriched data points about the person.
  name: Hunter Email Enrichment API
  slug: email-enrichment
- description: Returns detailed organizational data associated with a domain name, including company size, industry, location, and other firmographic information.
  name: Hunter Company Enrichment API
  slug: company-enrichment
- description: Merges person and company information for a single email address, returning enriched records combining both datasets.
  name: Hunter Combined Enrichment API
  slug: combined-enrichment
- description: Allows you to manage the leads stored in Hunter, including listing, creating, updating, upserting, and deleting leads.
  name: Hunter Leads API
  slug: leads
- description: Allows you to manage leads lists in Hunter, including listing, creating, updating, and deleting lead collection groups.
  name: Hunter Leads Lists API
  slug: leads-lists
- description: Allows you to manage email sequences including listing campaigns, managing recipients, and starting sequences for automated email outreach.
  name: Hunter Campaigns API
  slug: campaigns
- description: Retrieves any company logo using a domain name. Free to use with no authentication required, just a backlink from your site to hunter.io.
  name: Hunter Logo API
  slug: logo
capabilities:
- description: Unified workflow for sales prospecting including email discovery, verification, enrichment, lead management, and outreach campaigns. Used by sales development representatives and marketing teams.
  name: Hunter Sales Prospecting
  slug: sales-prospecting
common:
- title: ''
  type: Portal
  url: https://hunter.io/api
- title: ''
  type: Documentation
  url: https://hunter.io/api-documentation/v2
- title: ''
  type: OpenAPI
  url: openapi/hunter-api-openapi.yml
- title: ''
  type: JSONSchema
  url: json-schema/hunter-lead-schema.json
- title: ''
  type: JSONLD
  url: json-ld/hunter-context.jsonld
- title: ''
  type: Authentication
  url: https://hunter.io/api-documentation/v2#authentication
- title: ''
  type: RateLimits
  url: https://hunter.io/api-documentation/v2#rate-limiting
- title: ''
  type: Pricing
  url: https://hunter.io/pricing
- title: ''
  type: TermsOfService
  url: https://hunter.io/terms
- title: ''
  type: PrivacyPolicy
  url: https://hunter.io/privacy-policy
- title: ''
  type: StatusPage
  url: https://status.hunter.io
- title: ''
  type: Blog
  url: https://hunter.io/blog
- title: ''
  type: Login
  url: https://hunter.io/users/sign_in
- title: ''
  type: SignUp
  url: https://hunter.io/users/sign_up
- title: ''
  type: ChangeLog
  url: https://hunter.io/changelog
- title: ''
  type: GitHubOrganization
  url: https://github.com/hunter-io
- title: ''
  type: Contact
  url: https://hunter.io/contact
- title: ''
  type: Support
  url: https://help.hunter.io
- title: Hunter API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/hunter-api.yaml
- title: Sales Prospecting Workflow
  type: NaftikoCapability
  url: capabilities/sales-prospecting.yaml
created: '2024-01-01'
description: Hunter is an email finding and verification service that helps find professional email addresses associated with a domain and verify email deliverability.
features:
- description: Find all email addresses associated with a domain name along with confidence scores and sources.
  name: Domain Search
- description: Generate the most likely email address for a person given their name and company domain.
  name: Email Finder
- description: Verify the deliverability and validity of email addresses with detailed status reporting.
  name: Email Verification
- description: Store, organize, and manage prospect leads with lists, tags, and CRM-like contact management.
  name: Lead Management
- description: Create and manage automated email outreach sequences with recipient tracking and scheduling.
  name: Email Campaigns
- description: Enrich email addresses and domains with personal, company, and firmographic data points.
  name: Data Enrichment
- description: Find companies matching ideal customer profiles using natural language queries and advanced filters.
  name: Company Discovery
image: https://hunter.io/images/hunter-logo.png
integrations:
- description: Push verified leads and enriched contacts directly to Salesforce CRM for pipeline management.
  name: Salesforce
- description: Sync leads and contact data with HubSpot CRM for unified sales and marketing workflows.
  name: HubSpot
- description: Export leads to Pipedrive CRM with enriched contact and company information.
  name: Pipedrive
- description: Connect Hunter with thousands of apps through Zapier for automated lead processing workflows.
  name: Zapier
- description: Export domain search results and verified emails directly to Google Sheets for analysis.
  name: Google Sheets
- description: Integrate lead data with Zoho CRM for end-to-end sales pipeline management.
  name: Zoho CRM
jsonld:
- class_count: 0
  name: Hunter Context
  property_count: 0
  slug: hunter-context
layout: provider
modified: '2026-04-18'
name: Hunter
rules:
- name: Hunter API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: hunter-spectral-rules
skills: []
slug: hunter
solutions: []
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
url: https://raw.githubusercontent.com/api-evangelist/hunter/refs/heads/main/apis.yml
use_cases:
- description: Find and verify email addresses for sales outreach by searching company domains and building prospect lists.
  name: Sales Prospecting
- description: Enrich leads with company and personal data to qualify prospects and prioritize outreach efforts.
  name: Lead Qualification
- description: Verify large email lists to reduce bounce rates and improve email deliverability.
  name: Email List Cleaning
- description: Discover key contacts at target accounts using domain search and build targeted outreach campaigns.
  name: Account-Based Marketing
- description: Find professional email addresses for passive candidates at target companies for recruitment campaigns.
  name: Recruitment Outreach
---
