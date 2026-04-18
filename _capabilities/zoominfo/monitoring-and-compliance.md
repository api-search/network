---
consumed_apis:
- zoominfo
description: Unified capability for monitoring and compliance workflows combining webhook management, API usage tracking, and compliance operations. Used by platform admins and data governance teams to manage data monitoring, ensure compliance, and track API consumption.
layout: capability
name: ZoomInfo Monitoring And Compliance
operations:
- description: Create a new webhook subscription.
  method: POST
  name: create-webhook
  path: /v1/webhooks
- description: List all webhook subscriptions.
  method: GET
  name: list-webhooks
  path: /v1/webhooks
- description: Update an existing webhook subscription.
  method: PUT
  name: update-webhook
  path: /v1/webhooks/{webhookId}
- description: Delete a webhook subscription.
  method: DELETE
  name: delete-webhook
  path: /v1/webhooks/{webhookId}
- description: Validate a webhook target URL.
  method: POST
  name: validate-target-url
  path: /v1/webhooks/validate
- description: Get available webhook subscription types.
  method: GET
  name: get-subscription-types
  path: /v1/webhooks/subscription-types
- description: Check compliance status for specified contacts.
  method: POST
  name: check-compliance
  path: /v1/compliance
- description: Get API usage data.
  method: GET
  name: get-usage
  path: /v1/usage
personas: []
provider_name: ZoomInfo
provider_slug: zoominfo
search_terms:
- data compliance operations.
- get api usage data.
- lead generation
- validate a webhook target url.
- compliance
- api usage tracking.
- webhook subscription management.
- individual webhook management.
- create a new webhook subscription.
- api usage
- check compliance status for specified contacts.
- b2b data
- create webhook
- delete a webhook subscription.
- contact database
- list all webhook subscriptions.
- validate target url
- update webhook
- zoominfo
- list webhooks
- delete webhook
- monitoring
- company data
- check compliance
- marketing intelligence
- contacts
- validate a webhook target url is reachable.
- get subscription types
- sales intelligence
- list all configured webhook subscriptions.
- create a new webhook subscription for data change notifications.
- get usage
- get api usage data and consumption metrics.
- webhooks
- webhook target url validation.
- get available webhook subscription types.
- available webhook subscription types.
- b2b
- check data compliance status for specified contacts.
- data
- update an existing webhook subscription.
slug: monitoring-and-compliance
tags:
- ZoomInfo
- Monitoring
- Compliance
- Webhooks
- API Usage
tools:
- description: Create a new webhook subscription for data change notifications.
  hints:
    idempotent: false
    readOnly: false
  name: create-webhook
- description: List all configured webhook subscriptions.
  hints:
    idempotent: true
    readOnly: true
  name: list-webhooks
- description: Update an existing webhook subscription.
  hints:
    idempotent: true
    readOnly: false
  name: update-webhook
- description: Delete a webhook subscription.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-webhook
- description: Validate a webhook target URL is reachable.
  hints:
    idempotent: true
    readOnly: true
  name: validate-target-url
- description: Get available webhook subscription types.
  hints:
    idempotent: true
    readOnly: true
  name: get-subscription-types
- description: Check data compliance status for specified contacts.
  hints:
    openWorld: true
    readOnly: true
  name: check-compliance
- description: Get API usage data and consumption metrics.
  hints:
    idempotent: true
    readOnly: true
  name: get-usage
---
