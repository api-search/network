---
description: A GitHub issue used for tracking bugs, feature requests, tasks, and discussions within a repository.
layout: schema
name: GitHub Issue
properties_list:
- description: The unique identifier of the issue.
  name: id
  type: integer
- description: The GraphQL node ID for the issue.
  name: node_id
  type: string
- description: The API URL for the issue.
  name: url
  type: string
- description: The URL of the issue on GitHub.
  name: html_url
  type: string
- description: The issue number within the repository.
  name: number
  type: integer
- description: The current state of the issue.
  name: state
  type: string
- description: The reason the issue state was changed.
  name: state_reason
  type:
  - string
  - 'null'
- description: The title of the issue.
  name: title
  type: string
- description: The contents of the issue in Markdown format.
  name: body
  type:
  - string
  - 'null'
- description: ''
  name: user
  type: object
- description: Labels applied to the issue.
  name: labels
  type: array
- description: The primary user assigned to the issue.
  name: assignee
  type: object
- description: All users assigned to the issue.
  name: assignees
  type: array
- description: The milestone the issue is associated with.
  name: milestone
  type: object
- description: Whether the issue is locked.
  name: locked
  type: boolean
- description: The reason the issue was locked.
  name: active_lock_reason
  type:
  - string
  - 'null'
- description: The number of comments on the issue.
  name: comments
  type: integer
- description: Pull request metadata if this issue is also a pull request.
  name: pull_request
  type: object
- description: The date and time the issue was created.
  name: created_at
  type: string
- description: The date and time the issue was last updated.
  name: updated_at
  type: string
- description: The date and time the issue was closed.
  name: closed_at
  type:
  - string
  - 'null'
- description: The user who closed the issue.
  name: closed_by
  type: object
- description: How the author is associated with the repository.
  name: author_association
  type: string
- description: ''
  name: reactions
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-issue-schema.json
slug: github-issue
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: GitHub Issue
---
