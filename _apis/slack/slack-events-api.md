---
aid: slack:slack-events-api
baseURL: https://slack.com/api
description: The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occur, such as new messages, reactions, channel changes, or user updates. The Events API offers two delivery options - a public HTTP endpoint that Slack sends event payloads to, or Socket Mode which uses WebSockets for apps that cannot expose a public URL.
humanURL: https://docs.slack.dev/apis/events-api
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Slack Events API
properties:
- type: Documentation
  url: https://docs.slack.dev/apis/events-api
- type: SocketMode
  url: https://docs.slack.dev/apis/events-api/using-socket-mode
- type: Guide
  url: https://docs.slack.dev/apis/events-api/comparing-http-socket-mode
- type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/slack/refs/heads/main/asyncapi/slack-events-asyncapi.yml
provider_name: Slack
provider_slug: slack
slug: slack-events-api
tags:
- Events
- Real Time
- Webhooks
---
