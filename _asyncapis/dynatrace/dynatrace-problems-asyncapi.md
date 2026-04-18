---
channels:
- description: 'Represents the client''s webhook endpoint that receives Dynatrace problem notifications. Dynatrace sends an HTTP POST to this channel when a problem is opened, updated, merged, or resolved. The channel operates in a push model: Dynatrace (publisher) pushes events to the client''s webhook (subscriber).'
  name: /webhook/problems
  operation: subscribe
  operation_id: receiveProblemNotification
  summary: Receive problem notification
- description: The Dynatrace Configuration API endpoint for managing webhook notification integrations. Clients POST to this channel to register their webhook URL with Dynatrace, specifying which events should trigger notifications and what payload format to use.
  name: /api/config/v1/notifications
  operation: publish
  operation_id: registerWebhookNotification
  summary: Register webhook notification configuration
description: Dynatrace delivers problem lifecycle notifications to client-provided webhook endpoints via HTTP POST. When a problem is opened, updated, merged, or resolved, Dynatrace sends a notification payload to the registered webhook URL. Clients register their webhook endpoints using the Dynatrace Configuration API (POST /api/config/v1/notifications), specifying the URL, optional authentication headers, and payload template. This AsyncAPI document describes the webhook notification channel that clients implement to receive Dynatrace problem events.
layout: asyncapi
messages:
- description: Dynatrace sends this notification when the Davis AI engine opens a new problem. The problem may affect one or more monitored entities and includes initial root cause analysis, severity assessment, and the list of affected services or infrastructure.
  name: ProblemOpened
  summary: Notification sent when a new problem is detected by Dynatrace Davis AI
  title: Problem Opened
- description: Dynatrace sends this notification when the Davis AI engine detects that a previously opened problem has been resolved. The payload includes the resolution timestamp (endTime) and the full problem details at the time of resolution.
  name: ProblemResolved
  summary: Notification sent when a problem is resolved by Dynatrace Davis AI
  title: Problem Resolved
- description: Dynatrace sends this notification when the Davis AI engine determines that two separate problems share the same root cause and merges them into a single problem. The payload reflects the merged problem state.
  name: ProblemMerged
  summary: Notification sent when two problems are merged into a single problem by Davis AI
  title: Problem Merged
- description: The configuration object sent to the Dynatrace Configuration API to register a new webhook notification integration. This defines the target URL, authentication, and which alerting profiles trigger the webhook delivery.
  name: NotificationRegistration
  summary: Configuration payload for registering a webhook notification integration
  title: Webhook Notification Registration
name: Dynatrace Problem Notifications API
provider_name: Dynatrace
provider_slug: dynatrace
servers:
- description: The client-provided HTTPS webhook endpoint that receives Dynatrace problem notification POST requests. The URL is configured in Dynatrace under Settings > Integration > Problem notifications.
  name: webhook-endpoint
  protocol: https
  url: https://{your-webhook-host}/{your-webhook-path}
- description: The Dynatrace Configuration API endpoint used to register webhook notification integrations. Clients POST to this server to configure which webhook URL receives problem notifications and what event types trigger notifications.
  name: dynatrace-config-api
  protocol: https
  url: https://{environmentId}.live.dynatrace.com/api/config/v1
slug: dynatrace-problems-asyncapi
spec_file: asyncapi/dynatrace-problems-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/asyncapi/dynatrace-problems-asyncapi.yml
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
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
