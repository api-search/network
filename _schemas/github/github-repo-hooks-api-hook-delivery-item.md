---
description: Delivery made by a webhook, without request and response information.
layout: schema
name: hook-delivery-item
properties_list:
- description: Unique identifier of the webhook delivery.
  name: id
  type: integer
- description: Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event).
  name: guid
  type: string
- description: Time when the webhook delivery occurred.
  name: delivered_at
  type: string
- description: Whether the webhook delivery is a redelivery.
  name: redelivery
  type: boolean
- description: Time spent delivering.
  name: duration
  type: number
- description: Describes the response returned after attempting the delivery.
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
- description: Time when the webhook delivery was throttled.
  name: throttled_at
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repo-hooks-api-hook-delivery-item-schema.json
slug: github-repo-hooks-api-hook-delivery-item
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: hook-delivery-item
---
