---
description: Delivery made by a webhook.
layout: schema
name: hook-delivery
properties_list:
- description: Unique identifier of the delivery.
  name: id
  type: integer
- description: Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event).
  name: guid
  type: string
- description: Time when the delivery was delivered.
  name: delivered_at
  type: string
- description: Whether the delivery is a redelivery.
  name: redelivery
  type: boolean
- description: Time spent delivering.
  name: duration
  type: number
- description: Description of the status of the attempted delivery
  name: status
  type: string
- description: Status code received when delivery was made.
  name: status_code
  type: integer
- description: The event that triggered the delivery.
  name: event
  type: string
- description: The type of activity for the event that triggered the delivery.
  name: action
  type: string
- description: The id of the GitHub App installation associated with this event.
  name: installation_id
  type: integer
- description: The id of the repository associated with this event.
  name: repository_id
  type: integer
- description: The URL target of the delivery.
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
schema_file: json-schema/github-app-api-hook-delivery-schema.json
slug: github-app-api-hook-delivery
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: hook-delivery
---
