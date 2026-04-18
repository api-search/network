---
description: The result of a JQL search.
layout: schema
name: SearchResults
properties_list:
- description: The expand options applied.
  name: expand
  type: string
- description: The index of the first result returned.
  name: startAt
  type: integer
- description: The maximum number of results returned per page.
  name: maxResults
  type: integer
- description: The total number of results matching the JQL query.
  name: total
  type: integer
- description: The list of issues matching the JQL query.
  name: issues
  type: array
- description: Warning messages about the JQL query.
  name: warningMessages
  type: array
- description: Field name mapping.
  name: names
  type: object
- description: JSON Schema for each field.
  name: schema
  type: object
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-search-results-schema.json
slug: jira-cloud-platform-rest-search-results
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: SearchResults
---
