---
description: The standard payload structure for Cloudflare notification webhooks. When an alert fires, Cloudflare sends an HTTP POST with this JSON payload to configured webhook endpoints.
layout: schema
name: Cloudflare Notification Webhook Payload
properties_list:
- description: The name of the notification policy that triggered this webhook.
  name: name
  type: string
- description: Human-readable description of the alert with interpolated values specific to the event.
  name: text
  type: string
- description: Alert-specific data whose structure varies depending on the alert_type. Contains detailed information about the event that triggered the notification.
  name: data
  type: object
- description: Unix timestamp in seconds when the notification was generated.
  name: ts
  type: integer
- description: The Cloudflare account identifier associated with the notification. May not be present in all notifications.
  name: account_id
  type: string
- description: The UUID of the notification policy that triggered the webhook.
  name: policy_id
  type: string
- description: The name of the notification policy.
  name: policy_name
  type: string
- description: The unique identifier for the alert category (e.g., advanced_ddos_attack_l4_alert, health_check_status_notification).
  name: alert_type
  type: string
- description: UUID for grouping related alerts that are part of the same incident.
  name: alert_correlation_id
  type: string
- description: The event state indicating whether the alert is starting or ending.
  name: alert_event
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-notification-webhook-payload-schema.json
slug: cloudflare-notification-webhook-payload
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: Cloudflare Notification Webhook Payload
---
