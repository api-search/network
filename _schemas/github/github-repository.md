---
description: A GitHub repository containing source code, issues, pull requests, and other project resources.
layout: schema
name: GitHub Repository
properties_list:
- description: The unique identifier of the repository.
  name: id
  type: integer
- description: The GraphQL node ID for the repository.
  name: node_id
  type: string
- description: The name of the repository without the owner prefix.
  name: name
  type: string
- description: The full name of the repository in owner/name format.
  name: full_name
  type: string
- description: ''
  name: owner
  type: object
- description: Whether the repository is private.
  name: private
  type: boolean
- description: The URL of the repository on GitHub.
  name: html_url
  type: string
- description: A short description of the repository.
  name: description
  type:
  - string
  - 'null'
- description: Whether the repository is a fork of another repository.
  name: fork
  type: boolean
- description: The API URL for the repository.
  name: url
  type: string
- description: The date and time the repository was created.
  name: created_at
  type: string
- description: The date and time the repository was last updated.
  name: updated_at
  type: string
- description: The date and time of the last push to the repository.
  name: pushed_at
  type: string
- description: The URL of the repository's homepage.
  name: homepage
  type:
  - string
  - 'null'
- description: The size of the repository in kilobytes.
  name: size
  type: integer
- description: The number of stars the repository has received.
  name: stargazers_count
  type: integer
- description: The number of watchers on the repository.
  name: watchers_count
  type: integer
- description: The primary programming language of the repository.
  name: language
  type:
  - string
  - 'null'
- description: The number of forks of the repository.
  name: forks_count
  type: integer
- description: The number of open issues in the repository.
  name: open_issues_count
  type: integer
- description: The default branch of the repository.
  name: default_branch
  type: string
- description: The visibility level of the repository.
  name: visibility
  type: string
- description: The topics (tags) associated with the repository.
  name: topics
  type: array
- description: Whether the repository has issues enabled.
  name: has_issues
  type: boolean
- description: Whether the repository has projects enabled.
  name: has_projects
  type: boolean
- description: Whether the repository has the wiki enabled.
  name: has_wiki
  type: boolean
- description: Whether the repository has GitHub Pages enabled.
  name: has_pages
  type: boolean
- description: Whether the repository has downloads enabled.
  name: has_downloads
  type: boolean
- description: Whether the repository has discussions enabled.
  name: has_discussions
  type: boolean
- description: Whether the repository is archived and read-only.
  name: archived
  type: boolean
- description: Whether the repository is disabled.
  name: disabled
  type: boolean
- description: Whether the repository is a template repository.
  name: is_template
  type: boolean
- description: Whether forking is allowed on the repository.
  name: allow_forking
  type: boolean
- description: ''
  name: license
  type: object
- description: ''
  name: permissions
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repository-schema.json
slug: github-repository
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: GitHub Repository
---
