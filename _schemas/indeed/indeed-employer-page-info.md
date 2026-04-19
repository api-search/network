---
description: Pagination information for list responses.
layout: schema
name: PageInfo
properties_list:
- description: Whether there are more results available.
  name: hasNextPage
  type: boolean
- description: Whether there are previous results available.
  name: hasPreviousPage
  type: boolean
- description: Cursor for the first item in the current page.
  name: startCursor
  type: string
- description: Cursor for the last item in the current page.
  name: endCursor
  type: string
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-page-info-schema.json
slug: indeed-employer-page-info
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: PageInfo
---
