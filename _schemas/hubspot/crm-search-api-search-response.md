---
description: The response from a CRM search operation.
layout: schema
name: SearchResponse
properties_list:
- description: The total number of records matching the search criteria.
  name: total
  type: integer
- description: The matching CRM records for the current page.
  name: results
  type: array
- description: Pagination information for the response.
  name: paging
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-search-api-search-response-schema.json
slug: crm-search-api-search-response
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
title: SearchResponse
---
