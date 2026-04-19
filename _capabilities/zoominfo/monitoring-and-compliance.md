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
- create a new webhook subscription.
- validate a webhook target url.
- b2b
- data
- zoominfo
- validate a webhook target url is reachable.
- monitoring
- sales intelligence
- list all configured webhook subscriptions.
- available webhook subscription types.
- get subscription types
- data compliance operations.
- api usage tracking.
- get api usage data and consumption metrics.
- contacts
- b2b data
- api usage
- list all webhook subscriptions.
- check compliance status for specified contacts.
- update an existing webhook subscription.
- company data
- create a new webhook subscription for data change notifications.
- validate target url
- compliance
- marketing intelligence
- list webhooks
- get available webhook subscription types.
- check data compliance status for specified contacts.
- individual webhook management.
- webhook subscription management.
- lead generation
- delete webhook
- delete a webhook subscription.
- update webhook
- contact database
- get usage
- webhooks
- check compliance
- get api usage data.
- create webhook
- webhook target url validation.
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
