---
description: Paginated collection of blog authors
layout: schema
name: BlogAuthorCollection
properties_list:
- description: Total number of authors matching the query
  name: total
  type: integer
- description: Array of blog authors
  name: results
  type: array
- description: Pagination information for navigating result sets
  name: paging
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/authors-api-blog-author-collection-schema.json
slug: authors-api-blog-author-collection
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
title: BlogAuthorCollection
---
