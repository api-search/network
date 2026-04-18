---
description: A reply to a discussion within a team.
layout: schema
name: team-discussion-comment
properties_list:
- description: ''
  name: author
  type: object
- description: The main text of the comment.
  name: body
  type: string
- description: ''
  name: body_html
  type: string
- description: The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server.
  name: body_version
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: last_edited_at
  type: string
- description: ''
  name: discussion_url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: node_id
  type: string
- description: The unique sequence number of a team discussion comment.
  name: number
  type: integer
- description: ''
  name: updated_at
  type: string
- description: ''
  name: url
  type: string
- description: ''
  name: reactions
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-teams-team-discussion-comment-schema.json
slug: github-teams-team-discussion-comment
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: team-discussion-comment
---
