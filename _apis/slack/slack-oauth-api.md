---
aid: slack:slack-oauth-api
baseURL: https://slack.com/api
description: The Slack OAuth API implements the OAuth 2.0 flow that lets developers securely install Slack apps to workspaces and obtain access tokens with specific, granular scopes. An app redirects a user to Slack for consent; after approval, Slack returns an authorization code that the app exchanges for tokens (typically a bot token, and optionally a user token) to call the Web API within the granted permissions.
humanURL: https://docs.slack.dev/authentication
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Slack OAuth API
properties:
- type: Documentation
  url: https://docs.slack.dev/authentication
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/slack/refs/heads/main/openapi/slack-oauth-openapi.yml
provider_name: Slack
provider_slug: slack
slug: slack-oauth-api
tags:
- Authentication
- Authorization
- OAuth
---
