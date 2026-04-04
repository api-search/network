---
aid: slack:slack-emoji-api
name: Slack Emoji API
tags:
  - Emoji
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-emoji-openapi.yml
    type: OpenAPI
description: >-
  Slack's Emoji API lets apps discover and manage a workspace's custom emoji.
  The core method, emoji.list (requires the emoji:read scope), returns a
  name-to-URL map of all custom emoji along with aliases (noted as
  alias:other_name) and a cache timestamp to help clients sync efficiently. Apps
  can also subscribe to the emoji_changed event to stay up to date when emoji
  are added, renamed, or removed. On Enterprise Grid, org admins get additional
  admin.emoji.* methods to programmatically add, rename, alias, or remove custom
  emoji with appropriate admin scopes. The API focuses on metadata and
  management of custom emoji (not standard Unicode emoji) and is separate from
  reactions APIs, which use emoji but are managed through different endpoints.

---