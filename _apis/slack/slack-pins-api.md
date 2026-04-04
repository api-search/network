---
aid: slack:slack-pins-api
name: Slack Pins API
tags:
  - Pins
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-pins-openapi.yml
    type: OpenAPI
description: >-
  The Slack Pins API is a set of Web API methods that let your app manage pinned
  items in conversations so important content is easy to find. With pins.add,
  pins.list, and pins.remove, you can programmatically pin or unpin messages,
  files, and file comments in channels, private channels, and DMs by providing
  the conversation ID and the message timestamp or file/comment ID. Pinned items
  surface in the conversation's details panel in the Slack client, and pins.list
  returns the same set so your app can mirror or analyze it. These methods
  require your app to be a member of the conversation and have appropriate
  permissions, and they observe Slack's standard rate limits.

---