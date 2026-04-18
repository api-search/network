---
description: Request body for searching commerce payments
layout: schema
name: SearchRequest
properties_list:
- description: Search query string
  name: query
  type: string
- description: Maximum number of results
  name: limit
  type: integer
- description: Pagination cursor
  name: after
  type: string
- description: Sort order for results
  name: sorts
  type: array
- description: Properties to return
  name: properties
  type: array
- description: Filter groups for the search
  name: filterGroups
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-commerce-payments-search-request-schema.json
slug: hubspot-commerce-payments-search-request
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
