---
consumed_apis:
- zoominfo-api
description: Workflow for sales teams to find, qualify, and enrich prospect data. Combines contact search, company search, intent signals, and enrichment for targeted outreach.
layout: capability
name: ZoomInfo Sales Prospecting
operations:
- description: Search for contacts matching sales criteria
  method: POST
  name: search-contacts
  path: /v1/contacts/search
- description: Search for companies matching ideal customer profile
  method: POST
  name: search-companies
  path: /v1/companies/search
- description: Enrich a contact with verified data
  method: POST
  name: enrich-contact
  path: /v1/contacts/enrich
- description: Enrich a company with firmographic data
  method: POST
  name: enrich-company
  path: /v1/companies/enrich
- description: Find companies showing buying intent
  method: POST
  name: search-intent
  path: /v1/intent
- description: Search for business scoops about companies
  method: POST
  name: search-scoops
  path: /v1/scoops
personas: []
provider_name: ZoomInfo
provider_slug: zoominfo
search_terms:
- buyer intent signals
- enrich contact records
- contact database
- search and discover contacts
- search scoops
- company data
- sales prospecting
- enrich contact
- search for companies matching ideal customer profile
- search for business scoops about companies
- enrich technology
- lead generation
- search zoominfo for companies by industry, revenue, employee count, and tech stack
- enrich orgchart
- search for recent news about target companies
- intent data
- search intent
- search and discover companies
- search for business intelligence scoops about target companies
- find companies showing buying intent
- get org chart to identify decision makers at target company
- enrich company
- enrich a company with firmographic data
- company search
- business intelligence scoops
- get intent data for a specific company
- marketing intelligence
- enrich company records
- find companies showing buying intent signals in your category
- enrich a contact with verified data
- b2b data
- search companies
- enrich a contact record with verified email, phone, and professional details
- get technology stack details for a target company
- search zoominfo for contacts by job title, company, location, and industry
- search news
- search for contacts matching sales criteria
- zoominfo
- data
- enrich a company with firmographic data including revenue and employee count
- contacts
- b2b
- sales intelligence
- enrich intent
- search contacts
- contact search
slug: sales-prospecting
tags:
- ZoomInfo
- Sales Prospecting
- Lead Generation
- Contact Search
- Company Search
- Intent Data
tools:
- description: Search ZoomInfo for contacts by job title, company, location, and industry
  hints:
    openWorld: true
    readOnly: true
  name: search-contacts
- description: Search ZoomInfo for companies by industry, revenue, employee count, and tech stack
  hints:
    openWorld: true
    readOnly: true
  name: search-companies
- description: Enrich a contact record with verified email, phone, and professional details
  hints:
    openWorld: true
    readOnly: true
  name: enrich-contact
- description: Enrich a company with firmographic data including revenue and employee count
  hints:
    openWorld: true
    readOnly: true
  name: enrich-company
- description: Find companies showing buying intent signals in your category
  hints:
    openWorld: true
    readOnly: true
  name: search-intent
- description: Get intent data for a specific company
  hints:
    openWorld: true
    readOnly: true
  name: enrich-intent
- description: Search for business intelligence scoops about target companies
  hints:
    openWorld: true
    readOnly: true
  name: search-scoops
- description: Get technology stack details for a target company
  hints:
    openWorld: true
    readOnly: true
  name: enrich-technology
- description: Get org chart to identify decision makers at target company
  hints:
    openWorld: true
    readOnly: true
  name: enrich-orgchart
- description: Search for recent news about target companies
  hints:
    openWorld: true
    readOnly: true
  name: search-news
---
