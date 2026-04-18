---
description: A Bitbucket Cloud pull request.
layout: schema
name: Pullrequest
properties_list:
- description: ''
  name: type
  type: string
- description: The pull request ID.
  name: id
  type: integer
- description: The pull request title.
  name: title
  type: string
- description: The pull request description.
  name: description
  type: string
- description: ''
  name: state
  type: string
- description: ''
  name: created_on
  type: string
- description: ''
  name: updated_on
  type: string
- description: ''
  name: close_source_branch
  type: boolean
- description: The author of the pull request.
  name: author
  type: object
- description: The source branch.
  name: source
  type: object
- description: The destination branch.
  name: destination
  type: object
- description: ''
  name: merge_commit
  type: object
- description: ''
  name: comment_count
  type: integer
- description: ''
  name: task_count
  type: integer
- description: ''
  name: reviewers
  type: array
- description: ''
  name: participants
  type: array
provider_name: Bitbucket
provider_slug: bitbucket
schema_file: json-schema/bitbucket-cloud-rest-api-pullrequest-schema.json
slug: bitbucket-cloud-rest-api-pullrequest
tags:
- Atlassian
- CI/CD
- Code Collaboration
- Code Review
- DevOps
- Git
- Pull Requests
- Repository Hosting
- Version Control
title: Pullrequest
---
