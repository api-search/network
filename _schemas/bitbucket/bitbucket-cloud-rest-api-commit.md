---
description: A Bitbucket Cloud commit.
layout: schema
name: Commit
properties_list:
- description: ''
  name: type
  type: string
- description: The commit hash.
  name: hash
  type: string
- description: The commit date.
  name: date
  type: string
- description: The commit author.
  name: author
  type: object
- description: The commit message.
  name: message
  type: string
- description: ''
  name: parents
  type: array
- description: ''
  name: repository
  type: object
provider_name: Bitbucket
provider_slug: bitbucket
schema_file: json-schema/bitbucket-cloud-rest-api-commit-schema.json
slug: bitbucket-cloud-rest-api-commit
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
title: Commit
---
