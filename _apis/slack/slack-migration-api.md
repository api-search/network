---
aid: slack:slack-migration-api
name: Slack Migration API
tags:
  - Migration
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-migration-openapi.yml
    type: OpenAPI
description: "Slack's Migration API is a Web API used during Enterprise Grid migrations to translate legacy, workspace-scoped identifiers into their new, canonical IDs so apps keep working after a workspace moves or merges. By calling its migration.exchange method, developers and admins can map old user and channel IDs to the new values that Slack assigns in an Enterprise Grid org, allowing databases, webhooks, event subscriptions, and app configurations to be updated without losing references. It complements Admin and SCIM APIs in a migration runbook, but it doesn't move content or provision accounts\x14it strictly provides ID remapping to preserve continuity."

---