---
channels:
- description: Channel for subscribing to a PushTopic that monitors SOQL-defined record changes. Receives events when records matching the PushTopic query are created, updated, deleted, or undeleted in Salesforce.
  name: /topic/{pushTopicName}
  operation: subscribe
  operation_id: receivePushTopicEvent
  summary: Receive a PushTopic record change event
- description: Channel for subscribing to a Generic Streaming channel. Receives custom events published to this channel by Salesforce Apex or REST API calls.
  name: /u/{streamingChannelName}
  operation: subscribe
  operation_id: receiveGenericStreamingEvent
  summary: Receive a generic streaming event
description: The Salesforce Streaming API uses a publish-subscribe model based on Bayeux/CometD to push near-real-time event notifications to subscribed clients. It supports PushTopic events (triggered by SOQL queries on record changes) and Generic Streaming events (custom notifications). Clients connect via long-polling over HTTPS to receive events as they occur.
layout: asyncapi
messages:
- description: ''
  name: PushTopicEvent
  summary: Notification of a Salesforce record change matching a PushTopic query
  title: Salesforce PushTopic Record Change Event
- description: ''
  name: GenericStreamingEvent
  summary: Custom event published to a Generic Streaming channel
  title: Salesforce Generic Streaming Event
name: Salesforce Streaming API
provider_name: Salesforce
provider_slug: salesforce
servers:
- description: Salesforce CometD streaming endpoint
  name: salesforce
  protocol: https
  url: https://{instanceName}.salesforce.com/cometd/{apiVersion}
slug: salesforce-streaming-asyncapi
spec_file: asyncapi/salesforce-streaming-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/asyncapi/salesforce-streaming-asyncapi.yml
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
version: '44.0'
---
