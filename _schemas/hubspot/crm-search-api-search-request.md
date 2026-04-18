---
description: A search request for CRM objects. Filter groups are combined with OR logic; filters within a group are combined with AND logic.
layout: schema
name: SearchRequest
properties_list:
- description: An array of filter groups. Records matching any filter group will be included in results (OR logic between groups). Filters within a group are all required (AND logic within groups).
  name: filterGroups
  type: array
- description: An array of sort criteria to order the results.
  name: sorts
  type: array
- description: A full-text search query string. When provided, returns records where any searchable property contains the query term.
  name: query
  type: string
- description: An array of property names to include in the response for each record. If not specified, a default set of properties is returned.
  name: properties
  type: array
- description: The maximum number of results to return. Maximum value is 200.
  name: limit
  type: integer
- description: The cursor token for pagination. Use the value from the previous response's paging.next.after to get the next page of results.
  name: after
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-search-api-search-request-schema.json
slug: crm-search-api-search-request
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
title: SearchRequest
---
