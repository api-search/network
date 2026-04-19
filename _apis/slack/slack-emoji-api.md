---
aid: slack:slack-emoji-api
baseURL: https://slack.com/api
description: Slack's Emoji API lets apps discover and manage a workspace's custom emoji. The core method, emoji.list (requires the emoji:read scope), returns a name-to-URL map of all custom emoji along with aliases (noted as alias:other_name) and a cache timestamp to help clients sync efficiently. Apps can also subscribe to the emoji_changed event to stay up to date when emoji are added, renamed, or removed.
humanURL: https://docs.slack.dev/reference/methods
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Slack Emoji API
properties:
- type: Documentation
  url: https://docs.slack.dev/reference/methods
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/slack/refs/heads/main/openapi/slack-emoji-openapi.yml
provider_name: Slack
provider_slug: slack
slug: slack-emoji-api
tags:
- Emoji
---
