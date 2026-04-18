---
description: A record of a webhook delivery from GitHub, including the request headers, payload, and response information.
layout: schema
name: GitHub Webhook Delivery
properties_list:
- description: The unique identifier of the webhook delivery.
  name: id
  type: integer
- description: The globally unique identifier for the delivery (X-GitHub-Delivery header).
  name: guid
  type: string
- description: The date and time the delivery was made.
  name: delivered_at
  type: string
- description: Whether this delivery is a redelivery of a previous delivery.
  name: redelivery
  type: boolean
- description: The time in seconds the delivery took.
  name: duration
  type: number
- description: The HTTP status description returned by the receiver.
  name: status
  type: string
- description: The HTTP status code returned by the receiver.
  name: status_code
  type: integer
- description: The event type that triggered the delivery (X-GitHub-Event header).
  name: event
  type: string
- description: The action within the event that triggered the delivery.
  name: action
  type:
  - string
  - 'null'
- description: The GitHub App installation ID, if applicable.
  name: installation_id
  type:
  - integer
  - 'null'
- description: The repository ID associated with the delivery.
  name: repository_id
  type:
  - integer
  - 'null'
- description: The API URL for the delivery record.
  name: url
  type: string
- description: ''
  name: request
  type: object
- description: ''
  name: response
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-webhook-delivery-schema.json
slug: github-webhook-delivery
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: GitHub Webhook Delivery
---
