---
description: WebhookEvent from GitLab API
layout: schema
name: WebhookEvent
properties_list:
- description: The unique identifier of the webhook event delivery.
  name: id
  type: integer
- description: The URL the event was delivered to.
  name: url
  type: string
- description: The event type that triggered the webhook delivery.
  name: trigger
  type: string
- description: HTTP headers sent with the webhook request.
  name: request_headers
  type: object
- description: The JSON payload body sent in the webhook request.
  name: request_data
  type: string
- description: HTTP headers returned in the webhook response.
  name: response_headers
  type: object
- description: The body of the response from the webhook receiver.
  name: response_body
  type: string
- description: The HTTP response status code returned by the receiver.
  name: response_status
  type: string
- description: Time in milliseconds the webhook delivery took.
  name: execution_duration
  type: number
- description: The date and time the event was delivered.
  name: created_at
  type: string
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-webhooks-webhook-event-schema.json
slug: gitlab-webhooks-webhook-event
tags:
- Code
- Platform
- Software Development
- Source Control
title: WebhookEvent
---
