---
description: A single comment attached to a problem.
layout: schema
name: Comment
properties_list:
- description: The unique identifier of the comment.
  name: id
  type: string
- description: The Unix timestamp in milliseconds when the comment was created.
  name: createdAtTimestamp
  type: integer
- description: The display name of the user who created the comment.
  name: authorName
  type: string
- description: The text content of the comment.
  name: content
  type: string
- description: Optional context reference attached to the comment.
  name: context
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-problems-v2-comment-schema.json
slug: dynatrace-problems-v2-comment
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
title: Comment
---
