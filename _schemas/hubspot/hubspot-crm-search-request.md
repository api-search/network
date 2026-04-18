---
description: Schema for a CRM search request body used with POST /crm/v3/objects/{objectType}/search. Supports complex filtering, sorting, and pagination of CRM object records.
layout: schema
name: HubSpot CRM Search Request
properties_list:
- description: An array of filter groups. Records matching ANY filter group will be included in the results (OR logic between groups). Within each filter group, ALL filters must match (AND logic within a group). Max
  name: filterGroups
  type: array
- description: An array of sort criteria to order the results. When multiple sort criteria are specified, they are applied in order.
  name: sorts
  type: array
- description: A full-text search query string. When provided, returns records where any searchable default text property contains the query term. Can be combined with filterGroups for more specific searches.
  name: query
  type: string
- description: An array of property names to include in the response for each matching record. If not specified, a default set of properties is returned. Use this to request additional properties beyond the defaults
  name: properties
  type: array
- description: The maximum number of results to return in a single response. Defaults to 10 if not specified. Maximum value is 200.
  name: limit
  type: integer
- description: The pagination cursor token from the previous response's paging.next.after field. Used to retrieve the next page of search results.
  name: after
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-search-request-schema.json
slug: hubspot-crm-search-request
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: HubSpot CRM Search Request
---
