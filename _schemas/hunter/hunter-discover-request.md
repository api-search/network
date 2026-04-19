---
description: ''
layout: schema
name: DiscoverRequest
properties_list:
- description: Natural language search query to find matching companies.
  name: query
  type: string
- description: Filter by organization attributes.
  name: organization
  type: object
- description: Filter by geographic location of headquarters.
  name: headquarters_location
  type: object
- description: Filter by industry classification.
  name: industry
  type: object
- description: Filter by company headcount ranges.
  name: headcount
  type: array
- description: Filter by company entity type.
  name: company_type
  type: object
- description: Filter by year the company was founded.
  name: year_founded
  type: object
- description: Filter by technologies used by the company.
  name: technology
  type: object
- description: Filter by business keywords.
  name: keywords
  type: object
- description: Filter by funding information.
  name: funding
  type: object
- description: Maximum number of results to return.
  name: limit
  type: integer
- description: Number of results to skip for pagination.
  name: offset
  type: integer
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-discover-request-schema.json
slug: hunter-discover-request
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: DiscoverRequest
---
