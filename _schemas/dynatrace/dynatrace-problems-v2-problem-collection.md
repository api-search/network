---
description: A paginated collection of problems.
layout: schema
name: ProblemCollection
properties_list:
- description: Cursor for the next page of results. Null if no more pages.
  name: nextPageKey
  type: string
- description: The total number of problems matching the query.
  name: totalCount
  type: integer
- description: The number of results returned on this page.
  name: pageSize
  type: integer
- description: The list of problems on this page.
  name: problems
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-problems-v2-problem-collection-schema.json
slug: dynatrace-problems-v2-problem-collection
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: ProblemCollection
---
