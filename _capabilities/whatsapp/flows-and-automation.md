---
consumed_apis:
- whatsapp-flows
- whatsapp-business-mgmt
description: Unified workflow for creating and managing interactive flows, publishing lifecycle management, and webhook subscriptions. Combines Flows API and Business Management API webhook capabilities used by developers building guided conversational experiences and automation integrations.
layout: capability
name: WhatsApp Flows And Automation
operations:
- description: Lists all flows for a WABA.
  method: GET
  name: list-flows
  path: /v1/flows
- description: Creates a new flow.
  method: POST
  name: create-flow
  path: /v1/flows
- description: Retrieves details about a flow.
  method: GET
  name: get-flow
  path: /v1/flows/{flow_id}
- description: Updates a draft flow.
  method: POST
  name: update-flow
  path: /v1/flows/{flow_id}
- description: Deletes a draft flow.
  method: DELETE
  name: delete-flow
  path: /v1/flows/{flow_id}
- description: Retrieves flow assets.
  method: GET
  name: get-flow-assets
  path: /v1/flows/{flow_id}/assets
- description: Uploads flow JSON definition.
  method: POST
  name: upload-flow-json
  path: /v1/flows/{flow_id}/assets
- description: Publishes a draft flow.
  method: POST
  name: publish-flow
  path: /v1/flows/{flow_id}/publish
- description: Deprecates a published flow.
  method: POST
  name: deprecate-flow
  path: /v1/flows/{flow_id}/deprecate
- description: Lists webhook subscriptions.
  method: GET
  name: list-subscribed-apps
  path: /v1/webhook-subscriptions
- description: Subscribes app to webhooks.
  method: POST
  name: subscribe-app
  path: /v1/webhook-subscriptions
- description: Unsubscribes app from webhooks.
  method: DELETE
  name: unsubscribe-app
  path: /v1/webhook-subscriptions
personas: []
provider_name: WhatsApp
provider_slug: whatsapp
search_terms:
- creates a new flow.
- deprecates a published flow. deprecated flows remain in history but cannot be sent to customers.
- lists all flows for a waba.
- retrieves details about a specific flow including status, categories, and validation errors.
- flow json assets.
- retrieves the flow json assets including download urls.
- subscribe app
- retrieves details about a flow.
- deletes a draft flow. only draft flows can be deleted; published flows must be deprecated.
- whatsapp
- creates a new interactive flow. supports appointment booking, surveys, lead capture, and other guided experiences.
- get flow
- update flow
- publish a flow.
- webhooks
- subscribes the current app to receive webhook events for a waba.
- uploads flow json definition.
- lists webhook subscriptions.
- retrieves flow assets.
- publish flow
- subscribes app to webhooks.
- deletes a draft flow.
- list flows
- deprecates a published flow.
- unsubscribes the current app from webhook events.
- publishes a draft flow.
- lists all flows for a whatsapp business account.
- individual flow management.
- flows
- uploads or replaces the flow json definition file. the file is validated on upload.
- create flow
- publishes a draft flow, making it available for use in messages. requires valid flow json with no errors.
- deprecate a flow.
- deprecate flow
- unsubscribe app
- get flow assets
- upload flow json
- delete flow
- list subscribed apps
- automation
- conversational design
- updates a draft flow. only draft flows can be updated; published flows must be cloned.
- lists all apps subscribed to webhook events for a waba.
- interactive experiences
- flow management.
- unsubscribes app from webhooks.
- webhook subscription management.
- updates a draft flow.
slug: flows-and-automation
tags:
- WhatsApp
- Flows
- Automation
- Webhooks
- Interactive Experiences
- Conversational Design
tools:
- description: Lists all flows for a WhatsApp Business Account.
  hints:
    idempotent: true
    readOnly: true
  name: list-flows
- description: Creates a new interactive flow. Supports appointment booking, surveys, lead capture, and other guided experiences.
  hints:
    destructive: false
    readOnly: false
  name: create-flow
- description: Retrieves details about a specific flow including status, categories, and validation errors.
  hints:
    idempotent: true
    readOnly: true
  name: get-flow
- description: Updates a draft flow. Only DRAFT flows can be updated; published flows must be cloned.
  hints:
    idempotent: true
    readOnly: false
  name: update-flow
- description: Deletes a draft flow. Only DRAFT flows can be deleted; published flows must be deprecated.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-flow
- description: Retrieves the flow JSON assets including download URLs.
  hints:
    idempotent: true
    readOnly: true
  name: get-flow-assets
- description: Uploads or replaces the flow JSON definition file. The file is validated on upload.
  hints:
    destructive: false
    readOnly: false
  name: upload-flow-json
- description: Publishes a draft flow, making it available for use in messages. Requires valid flow JSON with no errors.
  hints:
    destructive: false
    readOnly: false
  name: publish-flow
- description: Deprecates a published flow. Deprecated flows remain in history but cannot be sent to customers.
  hints:
    destructive: true
    readOnly: false
  name: deprecate-flow
- description: Lists all apps subscribed to webhook events for a WABA.
  hints:
    idempotent: true
    readOnly: true
  name: list-subscribed-apps
- description: Subscribes the current app to receive webhook events for a WABA.
  hints:
    destructive: false
    readOnly: false
  name: subscribe-app
- description: Unsubscribes the current app from webhook events.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: unsubscribe-app
---
