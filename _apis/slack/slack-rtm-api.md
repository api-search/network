---
aid: slack:slack-rtm-api
name: Slack RTM API
tags:
  - Real Time Messaging
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-rtm-openapi.yml
    type: OpenAPI
description: "The Slack Real Time Messaging (RTM) API lets an app open a WebSocket connection to Slack and receive a live stream of JSON events from a workspace\x14such as new messages, edits, reactions, user presence and typing indicators, channel joins, and more\x14so you can build low\x11latency, interactive bots and clients. Apps typically use the RTM stream for listening and the Web API for performing actions like posting or updating messages. You start by calling rtm.connect (or rtm.start, historically) to obtain a WebSocket URL, then maintain the socket to process events as they happen. RTM is now considered legacy; for new apps Slack recommends using the Events API with the Web API, or Socket Mode if you can't expose a public HTTP endpoint."

---