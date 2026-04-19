---
consumed_apis:
- hunter
description: Unified workflow for sales prospecting including email discovery, verification, enrichment, lead management, and outreach campaigns. Used by sales development representatives and marketing teams.
layout: capability
name: Hunter Sales Prospecting
operations:
- description: Search for emails by domain.
  method: GET
  name: domain-search
  path: /v1/domain-search
- description: Find email for a person.
  method: GET
  name: find-email
  path: /v1/email-finder
- description: Verify email deliverability.
  method: GET
  name: verify-email
  path: /v1/email-verifier
- description: List all leads.
  method: GET
  name: list-leads
  path: /v1/leads
- description: Create a lead.
  method: POST
  name: create-lead
  path: /v1/leads
- description: Get lead details.
  method: GET
  name: get-lead
  path: /v1/leads/{id}
- description: Update a lead.
  method: PUT
  name: update-lead
  path: /v1/leads/{id}
- description: Delete a lead.
  method: DELETE
  name: delete-lead
  path: /v1/leads/{id}
- description: Enrich personal data from email.
  method: GET
  name: enrich-email
  path: /v1/enrichment/email
- description: Enrich company data from domain.
  method: GET
  name: enrich-company
  path: /v1/enrichment/company
- description: Discover companies.
  method: GET
  name: discover-companies
  path: /v1/discover
personas: []
provider_name: Hunter
provider_slug: hunter
search_terms:
- individual lead management.
- get leads list
- enrich combined
- search for emails by domain.
- get lead details.
- list all lead lists.
- prospecting
- company discovery.
- find email addresses.
- contact discovery
- email outreach
- list leads
- delete lead
- get lead list details.
- sales intelligence
- company enrichment.
- enrich company data from domain.
- create a new lead.
- verify email
- get account
- hunter
- create a new lead list.
- get lead
- discover companies matching criteria.
- email
- find email for a person.
- verify email deliverability.
- update lead
- list all leads.
- update a lead list.
- find email
- get combined person and company data.
- update leads list
- list campaigns
- create lead
- discover companies.
- find the most likely email for a person at a company.
- delete a lead list.
- count emails
- enrich personal data from email address.
- email verification
- lead generation
- list leads lists
- create a lead.
- create leads list
- delete leads list
- verify emails.
- lead management.
- enrich personal data from email.
- enrich email
- enrich company
- delete a lead.
- discover companies
- sales prospecting
- update a lead.
- count emails for a domain.
- email enrichment.
- get account information and usage.
- domain search
- search emails by domain.
- search for email addresses by domain.
- list all email campaigns.
slug: sales-prospecting
tags:
- Hunter
- Sales Prospecting
- Lead Generation
- Email Outreach
tools:
- description: Search for email addresses by domain.
  hints:
    openWorld: true
    readOnly: true
  name: domain-search
- description: Find the most likely email for a person at a company.
  hints:
    readOnly: true
  name: find-email
- description: Verify email deliverability.
  hints:
    readOnly: true
  name: verify-email
- description: Count emails for a domain.
  hints:
    readOnly: true
  name: count-emails
- description: Get account information and usage.
  hints:
    readOnly: true
  name: get-account
- description: List all leads.
  hints:
    openWorld: true
    readOnly: true
  name: list-leads
- description: Create a new lead.
  hints:
    readOnly: false
  name: create-lead
- description: Get lead details.
  hints:
    readOnly: true
  name: get-lead
- description: Update a lead.
  hints:
    idempotent: true
    readOnly: false
  name: update-lead
- description: Delete a lead.
  hints:
    destructive: true
    idempotent: true
  name: delete-lead
- description: List all lead lists.
  hints:
    readOnly: true
  name: list-leads-lists
- description: Create a new lead list.
  hints:
    readOnly: false
  name: create-leads-list
- description: Get lead list details.
  hints:
    readOnly: true
  name: get-leads-list
- description: Update a lead list.
  hints:
    idempotent: true
    readOnly: false
  name: update-leads-list
- description: Delete a lead list.
  hints:
    destructive: true
    idempotent: true
  name: delete-leads-list
- description: Discover companies matching criteria.
  hints:
    openWorld: true
    readOnly: true
  name: discover-companies
- description: Enrich personal data from email address.
  hints:
    readOnly: true
  name: enrich-email
- description: Enrich company data from domain.
  hints:
    readOnly: true
  name: enrich-company
- description: Get combined person and company data.
  hints:
    readOnly: true
  name: enrich-combined
- description: List all email campaigns.
  hints:
    readOnly: true
  name: list-campaigns
---
