---
channels:
- description: Generic webhook channel that receives all notification events from Cloudflare. Each notification includes the alert type, alert data, and metadata about the notification policy that triggered it.
  name: /webhook
  operation: publish
  operation_id: onNotificationEvent
  summary: Receive Cloudflare notification webhook
description: Cloudflare Notifications sends webhook events to configured endpoints when various alerts fire across your account. Webhooks deliver JSON payloads for events including DDoS attacks, SSL certificate expirations, origin health check failures, Workers errors, and many other alertable conditions. Professional and higher plans can configure generic webhooks or use pre-built integrations with Slack, Discord, PagerDuty, OpsGenie, and other services.
layout: asyncapi
messages:
- description: Fired when Cloudflare detects and mitigates a Layer 4 DDoS attack targeting your infrastructure. Contains details about the attack vector, protocol, target, and mitigation actions taken.
  name: DdosAttackL4Alert
  summary: Notification of a Layer 4 DDoS attack detected and mitigated
  title: DDoS Attack Layer 4 Alert
- description: Fired when Cloudflare detects a Layer 7 DDoS attack targeting your web application. Contains attack type, target hostname, and request rate information.
  name: DdosAttackL7Alert
  summary: Notification of a Layer 7 DDoS attack detected
  title: DDoS Attack Layer 7 Alert
- description: Fired when an SSL certificate is expiring soon, has expired, or has a status change. Contains certificate details, hostnames, and expiration information.
  name: SslCertificateAlert
  summary: Notification about an SSL certificate status change or upcoming expiration
  title: SSL Certificate Expiration Alert
- description: Fired when an origin health check detects a status change such as an origin becoming unhealthy or recovering. Contains the health check details and failing regions.
  name: HealthCheckAlert
  summary: Notification of an origin health status change
  title: Origin Health Check Alert
- description: Fired when a Workers script exceeds configured thresholds for CPU time, duration, request count, or error rates. Contains script metrics and route information.
  name: WorkersAlert
  summary: Notification about Workers script performance or error thresholds
  title: Workers Alert
- description: Generic payload structure for any Cloudflare notification alert. The data field contents vary depending on the specific alert type.
  name: GenericNotification
  summary: A generic notification event for any alert type
  title: Generic Notification
name: Cloudflare Notifications Webhooks
provider_name: Cloudflare
provider_slug: cloudflare
servers:
- description: Your configured webhook endpoint URL. Cloudflare sends HTTP POST requests to this URL when notification alerts fire. Validate incoming requests using the cf-webhook-auth header which contains your configured secret value.
  name: webhookEndpoint
  protocol: https
  url: '{webhookUrl}'
slug: cloudflare-notifications-webhooks-asyncapi
spec_file: asyncapi/cloudflare-notifications-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/cloudflare/refs/heads/main/asyncapi/cloudflare-notifications-webhooks-asyncapi.yml
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
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
