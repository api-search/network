---
description: A paginated collection of problem comments.
layout: schema
name: CommentCollection
properties_list:
- description: Cursor for the next page of results.
  name: nextPageKey
  type: string
- description: The total number of comments.
  name: totalCount
  type: integer
- description: The list of comments on this page.
  name: comments
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-problems-v2-comment-collection-schema.json
slug: dynatrace-problems-v2-comment-collection
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
title: CommentCollection
---
