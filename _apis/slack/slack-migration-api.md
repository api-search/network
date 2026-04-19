---
aid: slack:slack-migration-api
baseURL: https://slack.com/api
description: Slack's Migration API is a Web API used during Enterprise Grid migrations to translate legacy, workspace-scoped identifiers into their new, canonical IDs so apps keep working after a workspace moves or merges. By calling its migration.exchange method, developers and admins can map old user and channel IDs to the new values that Slack assigns in an Enterprise Grid org, allowing databases, webhooks, event subscriptions, and app configurations to be updated without losing references.
humanURL: https://docs.slack.dev/reference/methods
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Slack Migration API
properties:
- type: Documentation
  url: https://docs.slack.dev/reference/methods
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/slack/refs/heads/main/openapi/slack-migration-openapi.yml
provider_name: Slack
provider_slug: slack
slug: slack-migration-api
tags:
- Migration
---
