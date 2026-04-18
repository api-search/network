---
description: Configuration for a webhook notification integration in Dynatrace. Posted to POST /api/config/v1/notifications to register the webhook.
layout: schema
name: WebhookNotificationConfig
properties_list:
- description: The notification type. Must be WEBHOOK for webhook integrations.
  name: type
  type: string
- description: A display name for this notification configuration.
  name: name
  type: string
- description: Whether this notification integration is active.
  name: active
  type: boolean
- description: The HTTPS URL of the webhook endpoint that will receive problem notifications.
  name: url
  type: string
- description: The ID of the alerting profile (problem filter) that controls which problems trigger this notification.
  name: alertingProfile
  type: string
- description: Optional HTTP headers to include in the webhook request, such as authorization headers or content-type overrides.
  name: headers
  type: array
- description: Whether to accept any TLS certificate from the webhook endpoint. Should be false in production environments.
  name: acceptAnyCertificate
  type: boolean
- description: The custom payload template using Dynatrace placeholder variables such as {ProblemID}, {ProblemTitle}, {State}. If not specified, Dynatrace uses the default JSON payload format.
  name: payload
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/problems-webhook-notification-config-schema.json
slug: problems-webhook-notification-config
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
title: WebhookNotificationConfig
---
