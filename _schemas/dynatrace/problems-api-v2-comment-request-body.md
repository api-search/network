---
description: The request body for creating or updating a problem comment.
layout: schema
name: CommentRequestBody
properties_list:
- description: The text content of the comment.
  name: message
  type: string
- description: An optional context reference for the comment, such as a ticket ID, a link to a runbook, or a category label.
  name: context
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/problems-api-v2-comment-request-body-schema.json
slug: problems-api-v2-comment-request-body
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
title: CommentRequestBody
---
