---
channels:
- description: CometD channel for subscribing to a Platform Event type. Receives events published to this event type from Apex triggers, flows, REST API calls, or external systems via the REST API.
  name: /event/{platformEventApiName}
  operation: publish
  operation_id: publishPlatformEvent
  summary: Publish a Platform Event via CometD (internal use)
description: Salesforce Platform Events enables event-driven integration architectures on the Salesforce platform. Developers define custom event types as Salesforce objects with the __e suffix and publish or subscribe to events using the REST API, Apex triggers, or CometD subscriptions. Events are durable and stored for 72 hours, supporting replay for missed events.
layout: asyncapi
messages:
- description: ''
  name: PlatformEventMessage
  summary: A Platform Event notification received via CometD
  title: Salesforce Platform Event
- description: ''
  name: PlatformEventPublishMessage
  summary: Payload structure for publishing a Platform Event via REST API
  title: Platform Event Publish Payload
name: Salesforce Platform Events API
provider_name: Salesforce
provider_slug: salesforce
servers:
- description: CometD endpoint for subscribing to Platform Events
  name: salesforce-cometd
  protocol: https
  url: https://{instanceName}.salesforce.com/cometd/{apiVersion}
- description: Pub/Sub API gRPC endpoint (recommended for high-throughput subscriptions)
  name: salesforce-pubsub
  protocol: grpc
  url: api.pubsub.salesforce.com:443
slug: salesforce-platform-events-asyncapi
spec_file: asyncapi/salesforce-platform-events-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/asyncapi/salesforce-platform-events-asyncapi.yml
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
- AsyncAPI
- Webhooks
- Events
version: '59.0'
---
