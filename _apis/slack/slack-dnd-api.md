---
aid: slack:slack-dnd-api
name: Slack DND API
tags:
  - Do Not Disturb
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-dnd-openapi.yml
    type: OpenAPI
description: >-
  Slack's Do Not Disturb (DND) API lets apps read and manage users' notification
  quiet time so they don't get pinged when they've paused alerts. With the
  dnd:read and dnd:write scopes, an app can check a user's current DND state and
  scheduled quiet hours, retrieve team-wide DND summaries (where permitted),
  start or extend a snooze for a specified duration, and end snooze or active
  DND. Key methods include dnd.info, dnd.teamInfo, dnd.setSnooze, dnd.endSnooze,
  and dnd.endDnd. Responses provide whether DND is enabled and timestamps for
  when it starts and ends, enabling apps to defer messages, schedule work, or
  adjust notification behavior. The API is designed to respect user preferences
  and workspace policies; apps should handle rate limits and note that they can
  set temporary snoozes but cannot programmatically change a user's full DND
  schedule.

---