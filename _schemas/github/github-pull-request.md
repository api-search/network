---
description: A GitHub pull request representing a proposed change to a repository, including metadata for code review, merging, and CI/CD status.
layout: schema
name: GitHub Pull Request
properties_list:
- description: The unique identifier of the pull request.
  name: id
  type: integer
- description: The GraphQL node ID for the pull request.
  name: node_id
  type: string
- description: The API URL for the pull request.
  name: url
  type: string
- description: The URL of the pull request on GitHub.
  name: html_url
  type: string
- description: The URL to the pull request diff.
  name: diff_url
  type: string
- description: The URL to the pull request patch.
  name: patch_url
  type: string
- description: The pull request number within the repository.
  name: number
  type: integer
- description: The current state of the pull request.
  name: state
  type: string
- description: Whether the pull request is locked.
  name: locked
  type: boolean
- description: The title of the pull request.
  name: title
  type: string
- description: The contents of the pull request description in Markdown format.
  name: body
  type:
  - string
  - 'null'
- description: ''
  name: user
  type: object
- description: Labels applied to the pull request.
  name: labels
  type: array
- description: Users assigned to the pull request.
  name: assignees
  type: array
- description: Users requested to review the pull request.
  name: requested_reviewers
  type: array
- description: Teams requested to review the pull request.
  name: requested_teams
  type: array
- description: ''
  name: head
  type: object
- description: ''
  name: base
  type: object
- description: Whether the pull request is a draft.
  name: draft
  type: boolean
- description: Whether the pull request has been merged.
  name: merged
  type: boolean
- description: Whether the pull request can be merged. Null if not yet computed.
  name: mergeable
  type:
  - boolean
  - 'null'
- description: The mergeability state of the pull request.
  name: mergeable_state
  type: string
- description: The SHA of the merge commit, if merged.
  name: merge_commit_sha
  type:
  - string
  - 'null'
- description: The user who merged the pull request.
  name: merged_by
  type: object
- description: The number of comments on the pull request.
  name: comments
  type: integer
- description: The number of review comments on the pull request.
  name: review_comments
  type: integer
- description: The number of commits in the pull request.
  name: commits
  type: integer
- description: The number of lines added.
  name: additions
  type: integer
- description: The number of lines deleted.
  name: deletions
  type: integer
- description: The number of changed files.
  name: changed_files
  type: integer
- description: The date and time the pull request was created.
  name: created_at
  type: string
- description: The date and time the pull request was last updated.
  name: updated_at
  type: string
- description: The date and time the pull request was closed.
  name: closed_at
  type:
  - string
  - 'null'
- description: The date and time the pull request was merged.
  name: merged_at
  type:
  - string
  - 'null'
- description: Auto-merge configuration if enabled.
  name: auto_merge
  type:
  - object
  - 'null'
- description: How the author is associated with the repository.
  name: author_association
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-pull-request-schema.json
slug: github-pull-request
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: GitHub Pull Request
---
