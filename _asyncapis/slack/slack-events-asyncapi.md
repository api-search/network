---
channels:
- description: Primary channel for receiving all subscribed Slack events. Events are delivered as HTTP POST requests wrapped in an event callback envelope containing metadata about the event and the inner event payload. Your app must respond with HTTP 200 within 3 seconds. If not acknowledged, Slack retries up to 3 times with exponential backoff.
  name: eventCallback
- description: Used during initial app configuration. When you first configure your Request URL, Slack sends a url_verification challenge event. Your app must respond with the challenge value to confirm ownership.
  name: urlVerification
description: 'The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occur, such as new messages, reactions, channel changes, or user updates. The Events API offers two delivery options: a public HTTP endpoint that Slack sends event payloads to, or Socket Mode which uses WebSockets for apps that cannot expose a public URL. Events are categorized into Team Events (workspace-scoped, requiring corresponding OAuth scopes) and Bot Events (subscribed on behalf of the app''s bot user).'
layout: asyncapi
messages:
- description: The outer envelope for all event deliveries. Contains metadata about the event and the inner event object with the actual event data.
  name: EventCallback
  summary: An event callback payload from the Slack Events API
  title: Slack Event Callback
- description: ''
  name: UrlVerification
  summary: URL verification challenge sent during Request URL configuration
  title: Slack URL Verification Challenge
name: Slack Events API
provider_name: Slack
provider_slug: slack
servers:
- description: Your app's Request URL that receives HTTP POST payloads from Slack when subscribed events occur. Must respond with HTTP 200 within 3 seconds.
  name: httpEndpoint
  protocol: https
  url: ''
- description: Slack Socket Mode WebSocket connection for receiving events without exposing a public HTTP endpoint. Initiated via apps.connections.open Web API method.
  name: socketMode
  protocol: wss
  url: ''
slug: slack-events-asyncapi
spec_file: asyncapi/slack-events-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/slack/refs/heads/main/asyncapi/slack-events-asyncapi.yml
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
