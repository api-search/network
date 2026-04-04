---
aid: slack:slack-search-api
name: Slack Search API
tags:
  - Search
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-search-openapi.yml
    type: OpenAPI
description: >-
  Slack's Search API lets apps programmatically find messages and files in a
  workspace using the same query syntax users have in Slack (e.g., in:, from:,
  has:, before:/after:, is:thread). Through endpoints like search.messages and
  search.files, it returns ranked matches with snippets and optional
  highlighting, plus rich metadata such as channel, timestamps, user, thread
  context, permalinks, and file details. You can sort by relevance or time,
  filter with operators, and page through results. All results respect the app's
  scopes and the workspace's permissions, retention, and data controls, and the
  methods are subject to rate limits. Teams use it to power features like
  knowledge lookup, linking related conversations, and enabling bots to retrieve
  relevant historical context.

---