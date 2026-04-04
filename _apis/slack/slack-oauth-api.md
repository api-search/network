---
aid: slack:slack-oauth-api
name: Slack OAuth API
tags:
  - OAuth
  - Authentication
  - Authorization
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-oauth-openapi.yml
    type: OpenAPI
description: "The Slack OAuth API implements the OAuth 2.0 flow that lets developers securely install Slack apps to workspaces and obtain access tokens with specific, granular scopes. An app redirects a user to Slack for consent; after approval, Slack returns an authorization code that the app exchanges for tokens (typically a bot token, and optionally a user token) to call the Web API within the granted permissions. The OAuth system manages scopes, workspace and enterprise installations, admin approvals, reauthorization when scopes change, token rotation with refresh tokens, and revocation when apps are uninstalled or access is removed. For user sign-in, Slack also offers an OpenID Connect\x13based flow. In short, it provides consent-driven installation, permissioning, and token lifecycle management for Slack apps."

---