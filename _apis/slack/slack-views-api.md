---
aid: slack:slack-views-api
name: Slack Views API
tags:
  - Views
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-views-openapi.yml
    type: OpenAPI
description: "The Slack Views API lets your app build and control Block Kit interfaces inside Slack\x14primarily modals and the App Home tab. With methods like views.open, views.update, and views.push, your app can launch multi-step modal flows in response to interactive triggers (slash commands, shortcuts, or message actions), update them in place, or push new steps onto the stack. Using views.publish, you can render a personalized, dynamic Home tab for each user. Submissions and closes generate interactivity payloads (view_submission and view_closed) that let you validate inputs, return per-field errors, and persist state; you can also pass callback_id and private_metadata to track context. Concurrency is handled via a view hash to avoid overwriting stale content. In short, the Views API provides the lifecycle and plumbing for rich, interactive app experiences directly in Slack."

---