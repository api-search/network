---
channels:
- description: The endpoint that receives all Figma webhook event deliveries. The specific event type is identified by the event_type field in the payload. Figma webhooks are team-scoped and can subscribe to specific event types.
  name: /webhook
  operation: publish
  operation_id: receiveFigmaWebhookEvent
  summary: Receive a Figma webhook event
description: Figma Webhooks allow applications to receive real-time notifications when events occur in Figma files and projects. Webhooks are configured at the team level and send HTTP POST requests with JSON payloads to a specified endpoint URL. Supported events include file updates, comments, library publish changes, and version history updates. Webhooks use a passcode for payload verification.
layout: asyncapi
messages:
- description: The PING event is sent immediately when a new webhook is created via the POST /v2/webhooks endpoint. This event confirms that your endpoint is reachable and can process Figma webhook payloads. The webhook will be set to ACTIVE status if the ping succeeds.
  name: ping
  summary: Test event sent when a webhook is first created to verify the endpoint is reachable.
  title: Ping Event
- description: The FILE_UPDATE event fires whenever a Figma file within the subscribed team is modified and saved. This includes changes to the document tree, styles, components, and other file properties. Multiple rapid saves may be batched into a single webhook delivery.
  name: file_update
  summary: Triggered when a file in the team is saved or modified.
  title: File Update Event
- description: The FILE_VERSION_UPDATE event fires when a user creates a named version in a file's version history. This does not fire for auto-saved versions.
  name: file_version_update
  summary: Triggered when a named version is created in the file's version history.
  title: File Version Update Event
- description: The FILE_DELETE event fires when a Figma file within the subscribed team is permanently deleted. This event is not triggered when a file is moved to trash but only when it is permanently removed.
  name: file_delete
  summary: Triggered when a file in the team is deleted.
  title: File Delete Event
- description: The FILE_COMMENT event fires when a user posts a new comment on a Figma file within the subscribed team. This includes both top-level comments and replies. The payload includes the comment text, author, and location metadata.
  name: file_comment
  summary: Triggered when a new comment is posted on a file.
  title: File Comment Event
- description: The LIBRARY_PUBLISH event fires when a library file within the subscribed team publishes updates to its components, component sets, or styles. The payload includes lists of created, modified, and deleted library items.
  name: library_publish
  summary: Triggered when a library file publishes new components or styles.
  title: Library Publish Event
name: Figma Webhooks
provider_name: Figma
provider_slug: figma
servers:
- description: Your webhook receiver endpoint. Figma sends POST requests to this URL when subscribed events occur on the specified team. The endpoint must respond with a 200-level status code within 10 seconds.
  name: webhook-receiver
  protocol: https
  url: '{webhookUrl}'
slug: figma-webhooks-asyncapi
spec_file: asyncapi/figma-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/asyncapi/figma-webhooks-asyncapi.yml
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
- AsyncAPI
- Webhooks
- Events
version: 2.0.0
---
