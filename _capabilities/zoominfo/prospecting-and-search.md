---
consumed_apis:
- zoominfo
description: Unified capability for B2B prospecting workflows combining contact search, company search, intent signals, news, and scoops. Used by sales development reps and account executives to identify and prioritize target accounts and contacts.
layout: capability
name: ZoomInfo Prospecting And Search
operations:
- description: Search ZoomInfo contacts by criteria such as job title, company, location, and more.
  method: POST
  name: search-contacts
  path: /v1/contacts
- description: Search ZoomInfo companies by criteria such as industry, revenue, employee count, and more.
  method: POST
  name: search-companies
  path: /v1/companies
- description: Search ZoomInfo scoops for buying signals like funding, expansion, and leadership changes.
  method: POST
  name: search-scoops
  path: /v1/scoops
- description: Search ZoomInfo news for recent company events and announcements.
  method: POST
  name: search-news
  path: /v1/news
- description: Search ZoomInfo intent data to identify companies actively researching topics.
  method: POST
  name: search-intent
  path: /v1/intent
- description: Get available industry code lookup values.
  method: GET
  name: get-industries
  path: /v1/lookups/industries
- description: Get available department lookup values.
  method: GET
  name: get-departments
  path: /v1/lookups/departments
- description: Get available job function lookup values.
  method: GET
  name: get-job-functions
  path: /v1/lookups/job-functions
- description: Get available management level lookup values.
  method: GET
  name: get-management-levels
  path: /v1/lookups/management-levels
- description: Get available revenue range lookup values.
  method: GET
  name: get-revenue-ranges
  path: /v1/lookups/revenue-ranges
- description: Get available intent topic lookup values.
  method: GET
  name: get-intent-topics
  path: /v1/lookups/intent-topics
personas: []
provider_name: ZoomInfo
provider_slug: zoominfo
search_terms:
- get intent topics
- search zoominfo news for recent company events and announcements.
- get available intent topic lookup values.
- search companies
- search zoominfo contacts by criteria such as job title, company, location, and more.
- get departments
- get available revenue range lookup values.
- reference data for industry codes.
- marketing intelligence
- get job functions
- get available job function lookup values for filtering contact searches.
- prospecting
- search scoops
- search zoominfo intent data to identify companies actively researching topics.
- get available industry code lookup values for filtering searches.
- get available management level lookup values.
- contacts
- search for contacts matching prospecting criteria.
- search zoominfo scoops for buying signals like funding, expansion, and leadership changes.
- reference data for contact departments.
- reference data for revenue ranges.
- b2b
- reference data for management levels.
- zoominfo
- search for buying signals and scoops.
- reference data for job functions.
- search for companies matching prospecting criteria.
- get available industry code lookup values.
- sales intelligence
- get available department lookup values.
- search intent
- search news
- get industries
- get available job function lookup values.
- search zoominfo companies by criteria such as industry, revenue, employee count, and more.
- company data
- get revenue ranges
- search for buyer intent signals.
- get management levels
- search for company news articles.
- data
- reference data for intent topics.
- contact database
- lead generation
- get available department lookup values for filtering contact searches.
- b2b data
- search contacts
slug: prospecting-and-search
tags:
- ZoomInfo
- Prospecting
- Sales Intelligence
- B2B Data
tools:
- description: Search ZoomInfo contacts by criteria such as job title, company, location, and more.
  hints:
    openWorld: true
    readOnly: true
  name: search-contacts
- description: Search ZoomInfo companies by criteria such as industry, revenue, employee count, and more.
  hints:
    openWorld: true
    readOnly: true
  name: search-companies
- description: Search ZoomInfo scoops for buying signals like funding, expansion, and leadership changes.
  hints:
    openWorld: true
    readOnly: true
  name: search-scoops
- description: Search ZoomInfo news for recent company events and announcements.
  hints:
    openWorld: true
    readOnly: true
  name: search-news
- description: Search ZoomInfo intent data to identify companies actively researching topics.
  hints:
    openWorld: true
    readOnly: true
  name: search-intent
- description: Get available industry code lookup values for filtering searches.
  hints:
    idempotent: true
    readOnly: true
  name: get-industries
- description: Get available department lookup values for filtering contact searches.
  hints:
    idempotent: true
    readOnly: true
  name: get-departments
- description: Get available job function lookup values for filtering contact searches.
  hints:
    idempotent: true
    readOnly: true
  name: get-job-functions
- description: Get available management level lookup values.
  hints:
    idempotent: true
    readOnly: true
  name: get-management-levels
- description: Get available revenue range lookup values.
  hints:
    idempotent: true
    readOnly: true
  name: get-revenue-ranges
- description: Get available intent topic lookup values.
  hints:
    idempotent: true
    readOnly: true
  name: get-intent-topics
---
