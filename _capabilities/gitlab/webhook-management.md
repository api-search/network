---
consumed_apis:
- gitlab-webhooks
description: Unified capability for managing GitLab project webhooks, including CRUD operations, custom header and URL variable configuration, delivery event history, and testing. Used by DevOps engineers and platform administrators to set up and maintain event-driven integrations.
layout: capability
name: GitLab Webhook Management
operations:
- description: List all webhooks for a project.
  method: GET
  name: list-project-webhooks
  path: /v1/projects/{id}/webhooks
- description: Add a new webhook to a project.
  method: POST
  name: add-project-webhook
  path: /v1/projects/{id}/webhooks
- description: Get details of a specific project webhook.
  method: GET
  name: get-project-webhook
  path: /v1/projects/{id}/webhooks/{hook_id}
- description: Update a project webhook configuration.
  method: PUT
  name: update-project-webhook
  path: /v1/projects/{id}/webhooks/{hook_id}
- description: Delete a project webhook.
  method: DELETE
  name: delete-project-webhook
  path: /v1/projects/{id}/webhooks/{hook_id}
- description: List delivery events for a webhook from the past 7 days.
  method: GET
  name: list-webhook-events
  path: /v1/projects/{id}/webhooks/{hook_id}/events
- description: Resend a previously triggered webhook event.
  method: POST
  name: resend-webhook-event
  path: /v1/projects/{id}/webhooks/{hook_id}/events/{hook_event_id}/resend
- description: Send a test webhook payload of a specified trigger type.
  method: POST
  name: test-project-webhook
  path: /v1/projects/{id}/webhooks/{hook_id}/tests/{trigger}
- description: Set a custom header for a webhook.
  method: PUT
  name: set-webhook-custom-header
  path: /v1/projects/{id}/webhooks/{hook_id}/custom-headers/{key}
- description: Delete a custom header from a webhook.
  method: DELETE
  name: delete-webhook-custom-header
  path: /v1/projects/{id}/webhooks/{hook_id}/custom-headers/{key}
- description: Set a URL variable for a webhook.
  method: PUT
  name: set-webhook-url-variable
  path: /v1/projects/{id}/webhooks/{hook_id}/url-variables/{key}
- description: Delete a URL variable from a webhook.
  method: DELETE
  name: delete-webhook-url-variable
  path: /v1/projects/{id}/webhooks/{hook_id}/url-variables/{key}
personas: []
provider_name: GitLab
provider_slug: gitlab
search_terms:
- event driven
- get configuration details for a specific project webhook.
- get details of a specific project webhook.
- update project webhook
- list webhook events
- update a project webhook configuration.
- software development
- send a test webhook payload of a specified trigger type to verify endpoint configuration.
- delete webhook custom header
- add or update a custom http header sent with webhook deliveries.
- create a new webhook for a project with configurable event triggers.
- gitlab
- add or update a url variable for dynamic webhook url substitution.
- list project webhooks
- delete a project webhook.
- set webhook url variable
- resend a webhook event delivery.
- list all webhooks configured for a project.
- delete project webhook
- custom http header management for webhook deliveries.
- send a test webhook payload of a specified trigger type.
- remove a url variable from a webhook.
- list delivery events for a webhook from the past 7 days.
- resend webhook event
- url variable management for dynamic webhook url substitution.
- webhooks
- set webhook custom header
- remove a webhook from a project.
- devops
- test project webhook
- get project webhook
- set a custom header for a webhook.
- remove a custom http header from a webhook.
- delete a custom header from a webhook.
- code
- delete a url variable from a webhook.
- platform
- project webhook collection operations.
- list all webhooks for a project.
- resend a previously triggered webhook event.
- update the configuration of an existing project webhook.
- individual webhook operations.
- source control
- integrations
- set a url variable for a webhook.
- delete webhook url variable
- webhook delivery event history.
- add a new webhook to a project.
- test webhook triggers.
- resend a previously triggered webhook event to retry failed deliveries.
- add project webhook
slug: webhook-management
tags:
- Gitlab
- Webhooks
- Integrations
- Devops
- Event Driven
tools:
- description: List all webhooks configured for a project.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-project-webhooks
- description: Create a new webhook for a project with configurable event triggers.
  hints:
    idempotent: false
    openWorld: true
    readOnly: false
  name: add-project-webhook
- description: Get configuration details for a specific project webhook.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-project-webhook
- description: Update the configuration of an existing project webhook.
  hints:
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-project-webhook
- description: Remove a webhook from a project.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-project-webhook
- description: List delivery events for a webhook from the past 7 days.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-webhook-events
- description: Resend a previously triggered webhook event to retry failed deliveries.
  hints:
    idempotent: false
    openWorld: true
    readOnly: false
  name: resend-webhook-event
- description: Send a test webhook payload of a specified trigger type to verify endpoint configuration.
  hints:
    idempotent: false
    openWorld: true
    readOnly: false
  name: test-project-webhook
- description: Add or update a custom HTTP header sent with webhook deliveries.
  hints:
    idempotent: true
    openWorld: true
    readOnly: false
  name: set-webhook-custom-header
- description: Remove a custom HTTP header from a webhook.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-webhook-custom-header
- description: Add or update a URL variable for dynamic webhook URL substitution.
  hints:
    idempotent: true
    openWorld: true
    readOnly: false
  name: set-webhook-url-variable
- description: Remove a URL variable from a webhook.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-webhook-url-variable
---
