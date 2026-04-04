---
aid: microsoft-graph:microsoft-graph-subscriptions
name: Microsoft Graph Subscriptions
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/subscriptions-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Subscriptions let your app receive near real-time change
  notifications (webhooks) when Microsoft 365 data changessuch as Outlook mail
  and calendar items, users and groups, files in OneDrive/SharePoint, or Teams
  chats and channels. You register a subscription that specifies the resource to
  watch and a publicly reachable HTTPS endpoint; Microsoft Graph validates the
  endpoint and then posts notifications whenever relevant items are created,
  updated, or deleted. Subscriptions are time-limited and must be renewed, and
  notifications include information your app can use to verify authenticity and
  correlate events. You can receive a lightweight payload and fetch details via
  Graph, or include encrypted resource data directly in the notification. This
  enables reactive apps, workflows, and sync processes that trigger immediately
  on changes across Microsoft 365.

---