---
aid: slack:slack-auth-api
name: Slack Auth API
tags:
  - Authentication
  - Authorization
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-auth-openapi.yml
    type: OpenAPI
description: "Slack's Auth API covers the authentication and authorization pieces that let apps securely identify users and workspaces and manage access. It includes OAuth 2.0 endpoints used during app installation to request scopes and exchange authorization codes for tokens (with optional token rotation), plus OpenID Connect for \x1CSign in with Slack\x1D so you can authenticate users and retrieve standard identity claims. Within the Web API, methods like auth.test let you verify a token and learn which user and workspace it belongs to, auth.revoke allows you to invalidate tokens, and auth.teams.list helps enumerate the workspaces a user can use with your app (useful for multi-workspace and Enterprise Grid scenarios). Together, these capabilities ensure your app knows who is calling, what it's allowed to do, and where, before invoking other Slack APIs."

---