---
aid: slack:slack-team-api
name: Slack Team API
tags:
  - Teams
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-team-openapi.yml
    type: OpenAPI
description: >-
  Slack's Team API is the part of the Slack Web API that lets apps read
  workspace-level (team) information and, for admins, certain audit and billing
  data. With it, apps can fetch basic workspace identity and metadata (name,
  domain, icon, enterprise association), discover team preferences and custom
  profile fields, and, where permitted, retrieve billable info plus access and
  integration logs for auditing and compliance use cases. This helps apps tailor
  behavior to a workspace's settings, build admin dashboards, or automate
  governance. Access is gated by OAuth scopes (for example, team:read and
  various admin scopes), and many methods are limited to workspace or org
  admins; it doesn't handle messages or individual user data beyond what's
  needed to describe the workspace.

---