---
aid: slack:slack-users-api
name: Slack Users API
tags:
  - Users
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-users-openapi.yml
    type: OpenAPI
description: >-
  Slack's Users API is a set of Web API methods that let your app discover and
  work with people in a Slack workspace. It can list members, fetch details for
  a specific user, look up users by email, and retrieve profile data such as
  names, photos, status, time zones, and custom fields. Where permitted, it can
  also read presence and update a user's profile or photo with the proper
  user-level authorization. Developers use it to map real identities to Slack
  user IDs, personalize experiences, resolve mentions and DMs, and distinguish
  between human, bot, and app users. Access to specific data and actions depends
  on scopes (for example, users:read, users:read.email,
  users.profile:read/write), and certain capabilities like presence have
  additional restrictions. For provisioning and enterprise directory management,
  Slack's SCIM API is used instead.

---