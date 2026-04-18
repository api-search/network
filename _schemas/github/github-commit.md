---
description: A Git commit in a GitHub repository, including metadata about the author, committer, tree, parents, and verification status.
layout: schema
name: GitHub Commit
properties_list:
- description: The SHA-1 hash of the commit.
  name: sha
  type: string
- description: The GraphQL node ID for the commit.
  name: node_id
  type: string
- description: The API URL for the commit.
  name: url
  type: string
- description: The URL of the commit on GitHub.
  name: html_url
  type: string
- description: The API URL for the commit's comments.
  name: comments_url
  type: string
- description: ''
  name: commit
  type: object
- description: The GitHub user who authored the commit.
  name: author
  type: object
- description: The GitHub user who committed the changes.
  name: committer
  type: object
- description: The parent commits of this commit.
  name: parents
  type: array
- description: Statistics about the commit changes.
  name: stats
  type: object
- description: The files changed in the commit.
  name: files
  type: array
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-commit-schema.json
slug: github-commit
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: GitHub Commit
---
