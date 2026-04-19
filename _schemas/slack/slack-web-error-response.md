---
description: Standard error response from the Slack API.
layout: schema
name: ErrorResponse
properties_list:
- description: ''
  name: ok
  type: boolean
- description: A short machine-readable error code such as "channel_not_found", "not_authed", "invalid_auth", "missing_scope", etc.
  name: error
  type: string
- description: ''
  name: response_metadata
  type: object
provider_name: Slack
provider_slug: slack
schema_file: json-schema/slack-web-error-response-schema.json
slug: slack-web-error-response
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
title: ErrorResponse
---
