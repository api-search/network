---
consumed_apis:
- zoominfo
description: Unified capability for B2B data enrichment workflows combining contact, company, org chart, corporate hierarchy, location, technology, intent, and IP enrichment. Used by sales ops, marketing ops, and data teams to enrich CRM and marketing automation records.
layout: capability
name: ZoomInfo Data Enrichment
operations:
- description: Enrich a contact record with ZoomInfo person data.
  method: POST
  name: enrich-contact
  path: /v1/contacts/enrich
- description: Enrich a company record with ZoomInfo firmographic data.
  method: POST
  name: enrich-company
  path: /v1/companies/enrich
- description: Enrich a company record with ZoomInfo master company data.
  method: POST
  name: enrich-company-master
  path: /v1/companies/master-enrich
- description: Get org chart data for a company.
  method: POST
  name: enrich-orgchart
  path: /v1/org-charts
- description: Get corporate hierarchy data showing parent/subsidiary relationships.
  method: POST
  name: enrich-corporate-hierarchy
  path: /v1/corporate-hierarchies
- description: Get location data for a company.
  method: POST
  name: enrich-location
  path: /v1/locations
- description: Get technology stack data for a company.
  method: POST
  name: enrich-technology
  path: /v1/technologies
- description: Get hashtag data for a contact.
  method: POST
  name: enrich-hashtags
  path: /v1/hashtags
- description: Get intent signal data for a company.
  method: POST
  name: enrich-intent
  path: /v1/intent/enrich
- description: Get news data for a company.
  method: POST
  name: enrich-news
  path: /v1/news/enrich
- description: Get scoop data for a company.
  method: POST
  name: enrich-scoop
  path: /v1/scoops/enrich
- description: Get company data associated with an IP address.
  method: POST
  name: enrich-ip
  path: /v1/ip-addresses
- description: Submit a bulk contact search job.
  method: POST
  name: bulk-search-contacts
  path: /v1/bulk/contacts
- description: Submit a bulk contact enrichment job.
  method: POST
  name: bulk-enrich-contacts
  path: /v1/bulk/contacts
- description: Submit a bulk company search job.
  method: POST
  name: bulk-search-companies
  path: /v1/bulk/companies
- description: Submit a bulk company enrichment job.
  method: POST
  name: bulk-enrich-companies
  path: /v1/bulk/companies
- description: Get the status of a bulk job.
  method: GET
  name: get-bulk-job-status
  path: /v1/bulk/jobs/{jobId}/status
- description: Get the results of a completed bulk job.
  method: GET
  name: get-bulk-job-results
  path: /v1/bulk/jobs/{jobId}/results
personas: []
provider_name: ZoomInfo
provider_slug: zoominfo
search_terms:
- contacts
- get news data for a company.
- bulk company search and enrichment.
- retrieve intent signal enrichment data.
- bulk search contacts
- enrich hashtags
- bulk enrich contacts
- enrich intent
- get org chart data for a company.
- sales intelligence
- retrieve organizational chart data.
- get organizational chart data for a company.
- retrieve corporate hierarchy data.
- enrich location
- submit a bulk contact enrichment job.
- bulk search companies
- enrich a company record with zoominfo master company data.
- zoominfo
- retrieve bulk job results.
- get hashtag data for a contact.
- check bulk job status.
- enrich company master
- get technology stack data for a company.
- get intent signal data for a company.
- get corporate hierarchy data showing parent/subsidiary relationships.
- get bulk job results
- company data
- crm integration
- enrich contact records with zoominfo data.
- retrieve news enrichment data.
- data
- enrich company
- retrieve technology stack data.
- enrich technology
- submit a bulk company enrichment job.
- b2b
- bulk enrich companies
- get location data for a company.
- data enrichment
- enrich a company record with zoominfo firmographic data.
- enrich news
- enrich a contact record with zoominfo person data including email, phone, title, and company.
- get company data associated with an ip address.
- submit a bulk contact search job.
- get bulk job status
- enrich corporate hierarchy
- get scoop data for a company.
- enrich company records with zoominfo data.
- enrich scoop
- bulk contact search and enrichment.
- marketing intelligence
- enrich company records with zoominfo master data.
- enrich orgchart
- retrieve company location data.
- retrieve scoop enrichment data.
- b2b data
- enrich a company record with zoominfo firmographic data including revenue, employees, and industry.
- retrieve contact hashtag data.
- submit a bulk company search job.
- enrich ip
- enrich ip addresses with company data.
- get corporate hierarchy showing parent/subsidiary relationships.
- lead generation
- get the results of a completed bulk job.
- get the status of a bulk job.
- contact database
- enrich contact
- enrich a contact record with zoominfo person data.
slug: data-enrichment
tags:
- ZoomInfo
- Data Enrichment
- CRM Integration
- B2B Data
tools:
- description: Enrich a contact record with ZoomInfo person data including email, phone, title, and company.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-contact
- description: Enrich a company record with ZoomInfo firmographic data including revenue, employees, and industry.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-company
- description: Enrich a company record with ZoomInfo master company data.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-company-master
- description: Get organizational chart data for a company.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-orgchart
- description: Get corporate hierarchy showing parent/subsidiary relationships.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-corporate-hierarchy
- description: Get location data for a company.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-location
- description: Get technology stack data for a company.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-technology
- description: Get hashtag data for a contact.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-hashtags
- description: Get intent signal data for a company.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-intent
- description: Get news data for a company.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-news
- description: Get scoop data for a company.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-scoop
- description: Get company data associated with an IP address.
  hints:
    openWorld: true
    readOnly: true
  name: enrich-ip
- description: Submit a bulk contact search job.
  hints:
    idempotent: false
    readOnly: false
  name: bulk-search-contacts
- description: Submit a bulk company search job.
  hints:
    idempotent: false
    readOnly: false
  name: bulk-search-companies
- description: Submit a bulk contact enrichment job.
  hints:
    idempotent: false
    readOnly: false
  name: bulk-enrich-contacts
- description: Submit a bulk company enrichment job.
  hints:
    idempotent: false
    readOnly: false
  name: bulk-enrich-companies
- description: Get the status of a bulk job.
  hints:
    idempotent: true
    readOnly: true
  name: get-bulk-job-status
- description: Get the results of a completed bulk job.
  hints:
    idempotent: true
    readOnly: true
  name: get-bulk-job-results
---
