---
channels:
- description: Challenge verification channel. When a webhook is registered, Adobe sends a GET request with a challenge query parameter. The webhook must respond with the challenge value in the body to prove ownership.
  name: /webhook/challenge
  operation: subscribe
  operation_id: onWebhookChallenge
  summary: Receive webhook challenge verification
- description: Primary event delivery channel. Adobe I/O Events sends POST requests to registered webhooks when events occur. Events conform to the CloudEvents specification.
  name: /webhook/event
  operation: subscribe
  operation_id: onEvent
  summary: Receive event notification
- description: Batch event delivery channel for high-volume event scenarios. Multiple events are grouped into a single POST request as a JSON array.
  name: /webhook/batch
  operation: subscribe
  operation_id: onBatchEvent
  summary: Receive batch event notifications
- description: Journaling channel for pull-based event consumption. Clients poll this endpoint with a position cursor to retrieve events. Events are retained for 7 days. Use the Link header from each response to get the next batch of events.
  name: /events/organizations/{orgId}/integrations/{integrationId}/{registrationId}
  operation: subscribe
  operation_id: pollJournalEvents
  summary: Poll journaling endpoint for events
description: Adobe I/O Events enables developers to receive near-real-time notifications when events occur across Adobe products and services. Events are delivered via webhooks or journaling (pull-based polling). Supported event providers include Creative Cloud, Experience Cloud, Document Cloud, and custom applications built on Adobe App Builder. Events follow the CloudEvents specification and include provenance metadata for traceability.
layout: asyncapi
messages:
- description: ''
  name: CreativeCloudAssetEvent
  summary: Event triggered when assets are created, updated, or deleted in Creative Cloud Libraries, Lightroom, or other CC storage.
  title: Creative Cloud Asset Event
- description: ''
  name: AEMAssetEvent
  summary: Event triggered by asset operations in Adobe Experience Manager such as asset creation, modification, or processing completion.
  title: AEM Asset Event
- description: ''
  name: AnalyticsEvent
  summary: Event triggered by Adobe Analytics notifications such as report completion, classification import completion, or segment publication.
  title: Adobe Analytics Event
- description: ''
  name: CampaignEvent
  summary: Event triggered by Adobe Campaign Standard operations such as delivery status updates, workflow transitions, or profile changes.
  title: Adobe Campaign Event
- description: ''
  name: CustomAppEvent
  summary: Event published by custom Adobe App Builder applications via the Events SDK. Developers define their own event types and payload structures.
  title: Custom Application Event
name: Adobe I/O Events
provider_name: Adobe Creative Cloud
provider_slug: adobe-creative-cloud
servers:
- description: Your webhook endpoint that receives event notifications from Adobe I/O Events. Must respond to a challenge verification request during registration and acknowledge events with a 200 status.
  name: webhook
  protocol: https
  url: '{webhookUrl}'
- description: Adobe I/O Events journaling endpoint for pull-based event consumption. Events are retained for 7 days and retrieved via polling with a position cursor.
  name: journaling
  protocol: https
  url: https://events-va6.adobe.io
slug: adobe-io-events-asyncapi-original
spec_file: asyncapi/adobe-io-events-asyncapi-original.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/adobe-creative-cloud/refs/heads/main/asyncapi/adobe-io-events-asyncapi-original.yml
tags:
- AI/ML
- Cloud
- Creative
- Design
- Documents
- Photography
- SaaS
- Video
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
