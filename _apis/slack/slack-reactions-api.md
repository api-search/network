---
aid: slack:slack-reactions-api
name: Slack Reactions API
tags:
  - Reactions
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-reactions-openapi.yml
    type: OpenAPI
description: >-
  Slack's Reactions API lets apps programmatically manage emoji reactions on
  messages and files, making it easy to capture lightweight feedback like
  approvals, acknowledgments, or votes. Through Web API methods (reactions.add,
  reactions.remove, reactions.get, reactions.list) and the Events API
  (reaction_added and reaction_removed), apps can add or delete reactions, read
  which reactions are on an item, and monitor reaction activity in real time. It
  works with messages (including threads), files, and file comments in channels,
  DMs, and group DMs where the app has access. Responses include reaction names,
  counts, and user IDs, and support both standard and custom emoji. Proper
  scopes (reactions:read and reactions:write, plus relevant conversation/file
  scopes) and channel visibility rules apply, rate limits are enforced, and each
  user can apply at most one instance of a given emoji per item.

---