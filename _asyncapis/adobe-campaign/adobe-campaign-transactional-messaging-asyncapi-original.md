---
channels:
- description: Channel for triggering transactional email messages. Events submitted here are processed asynchronously by the Campaign transactional messaging engine and result in personalized email delivery to the specified recipient.
  name: transactionalEvent/email
  operation: publish
  operation_id: triggerEmailEvent
  summary: Trigger a transactional email event
- description: Channel for triggering transactional SMS messages. Events submitted here result in personalized SMS delivery to the specified mobile phone number.
  name: transactionalEvent/sms
  operation: publish
  operation_id: triggerSmsEvent
  summary: Trigger a transactional SMS event
- description: Channel for triggering transactional push notifications. Events submitted here result in push notification delivery to the specified device via Apple Push Notification service (APNs) or Firebase Cloud Messaging (FCM).
  name: transactionalEvent/push
  operation: publish
  operation_id: triggerPushEvent
  summary: Trigger a transactional push notification event
- description: Channel for receiving transactional event status updates. After an event is submitted, its status transitions through the processing lifecycle and can be polled to determine the outcome.
  name: transactionalEvent/status
  operation: subscribe
  operation_id: receiveEventStatus
  summary: Receive event processing status updates
- description: Channel for submitting batches of real-time events via Campaign Classic SOAP interface. More efficient than individual event submission when processing high volumes of transactional events.
  name: batchEvent
  operation: publish
  operation_id: submitBatchEvents
  summary: Submit a batch of transactional events
description: Event-driven transactional messaging system for Adobe Campaign. Supports triggering personalized messages across email, SMS, and push notification channels in response to real-time customer events. Events follow an asynchronous lifecycle from submission through delivery or failure. Covers both Campaign Standard REST event triggers and Campaign Classic SOAP PushEvent patterns.
layout: asyncapi
messages:
- description: Event payload for triggering a transactional email message with personalization context data.
  name: TransactionalEmailEvent
  summary: Transactional email event
  title: TransactionalEmailEvent
- description: Event payload for triggering a transactional SMS message.
  name: TransactionalSmsEvent
  summary: Transactional SMS event
  title: TransactionalSmsEvent
- description: Event payload for triggering a transactional push notification.
  name: TransactionalPushEvent
  summary: Transactional push notification event
  title: TransactionalPushEvent
- description: Status update for a previously submitted transactional event, indicating its current position in the processing lifecycle.
  name: EventStatusUpdate
  summary: Event processing status
  title: EventStatusUpdate
- description: SOAP payload containing multiple real-time events for batch processing by Campaign Classic Message Center.
  name: BatchEventSubmission
  summary: Batch event submission
  title: BatchEventSubmission
name: Adobe Campaign Transactional Messaging Events
provider_name: Adobe Campaign
provider_slug: adobe-campaign
servers:
- description: Campaign Standard transactional event endpoint. Events are triggered via REST POST and status is polled via GET.
  name: standard
  protocol: https
  url: https://mc.adobe.io/{ORGANIZATION}/campaign
- description: Campaign Classic SOAP-based event endpoint. Events are pushed via nms:rtEvent#PushEvent and nms:batchEvent#PushEvents SOAP methods.
  name: classic
  protocol: https
  url: https://{instance}.campaign.adobe.com
slug: adobe-campaign-transactional-messaging-asyncapi-original
spec_file: asyncapi/adobe-campaign-transactional-messaging-asyncapi-original.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/asyncapi/adobe-campaign-transactional-messaging-asyncapi-original.yml
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
