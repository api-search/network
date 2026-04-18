---
description: Request body for JQL search via POST.
layout: schema
name: SearchRequest
properties_list:
- description: The JQL query string.
  name: jql
  type: string
- description: The index of the first item to return (page offset).
  name: startAt
  type: integer
- description: The maximum number of items to return per page.
  name: maxResults
  type: integer
- description: 'Whether to validate the JQL query. Accepted values: strict, warn, none.'
  name: validateQuery
  type: string
- description: Fields to return for each issue.
  name: fields
  type: array
- description: Expand options for additional information.
  name: expand
  type: string
- description: Issue properties to return.
  name: properties
  type: array
- description: Whether to reference fields by keys rather than IDs.
  name: fieldsByKeys
  type: boolean
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-search-request-schema.json
slug: jira-cloud-platform-rest-search-request
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: SearchRequest
---
