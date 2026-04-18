---
channels:
- description: The channel through which Intuit delivers webhook notifications to your application. Your endpoint must accept POST requests and respond with HTTP 200 within 10 seconds. Failed deliveries are retried, but notifications are delivered on a best-effort basis.
  name: webhookNotification
description: QuickBooks Online Webhooks provide near real-time notifications when data changes in a QuickBooks Online company. When an entity is created, updated, merged, deleted, or voided, Intuit sends an HTTP POST notification to your registered endpoint. Webhook notifications are delivered as JSON payloads and are signed with an HMAC-SHA256 signature using your webhook verifier token. Your endpoint must respond with an HTTP 200 status within 10 seconds. Notifications may be batched, delivering multiple entity change events in a single payload. Notifications are sent on a best-effort basis and may arrive out of order; your application should use the query API to retrieve the current state of changed entities.
layout: asyncapi
messages:
- description: Contains one or more entity change events grouped by company (realm). Each event describes a single entity change operation. Multiple events for different entities and different companies may be included in a single notification delivery.
  name: WebhookNotification
  summary: A batch of entity change notifications from QuickBooks Online
  title: Webhook Notification
name: QuickBooks Online Webhooks
provider_name: Intuit
provider_slug: intuit
servers:
- description: Your application's webhook endpoint. This URL is registered in the Intuit Developer portal under the Webhooks section of your app settings. Intuit sends HTTP POST requests to this URL when entity changes occur.
  name: yourEndpoint
  protocol: https
  url: ''
slug: quickbooks-webhooks
spec_file: asyncapi/quickbooks-webhooks.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/intuit/refs/heads/main/asyncapi/quickbooks-webhooks.yml
tags:
- Accounting
- Custom Fields
- Financial
- Financial Services
- Invoicing
- Payments
- Payroll
- Project Management
- Sales Tax
- Small Business
- Tax
- Tax Preparation
- Taxes
- Time Tracking
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
