---
aid: slack:slack-user-groups-api
name: Slack User Groups API
tags:
  - Users
  - Groups
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: openapi/slack-usergroups-openapi.yml
    type: OpenAPI
description: >-
  Slack's User Groups API lets apps programmatically create and manage user
  groups (mentionable aliases like @eng or @oncall) in a workspace. It supports
  creating, renaming, and updating groups and their handles and descriptions;
  setting default channels; enabling or disabling groups; listing groups; and
  adding or removing members in bulk. User groups make it easy to notify the
  right people with a single mention and to auto-add members to specific
  channels via default channel settings. Teams use the API to automate org
  changes, sync groups from an identity provider, manage on-call rotations, and
  streamline onboarding/offboarding. It's exposed via usergroups.* and
  usergroups.users.* Web API methods and typically requires the usergroups:read
  and usergroups:write scopes, with appropriate admin permissions and a paid
  Slack plan.

---