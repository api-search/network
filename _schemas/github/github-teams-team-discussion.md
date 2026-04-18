---
description: A team discussion is a persistent record of a free-form conversation within a team.
layout: schema
name: team-discussion
properties_list:
- description: ''
  name: author
  type: object
- description: The main text of the discussion.
  name: body
  type: string
- description: ''
  name: body_html
  type: string
- description: The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server.
  name: body_version
  type: string
- description: ''
  name: comments_count
  type: integer
- description: ''
  name: comments_url
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: last_edited_at
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: node_id
  type: string
- description: The unique sequence number of a team discussion.
  name: number
  type: integer
- description: Whether or not this discussion should be pinned for easy retrieval.
  name: pinned
  type: boolean
- description: Whether or not this discussion should be restricted to team members and organization owners.
  name: private
  type: boolean
- description: ''
  name: team_url
  type: string
- description: The title of the discussion.
  name: title
  type: string
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
schema_file: json-schema/github-teams-team-discussion-schema.json
slug: github-teams-team-discussion
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: team-discussion
---
