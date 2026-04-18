---
description: A Bitbucket Cloud repository.
layout: schema
name: Repository
properties_list:
- description: The resource type.
  name: type
  type: string
- description: The repository UUID.
  name: uuid
  type: string
- description: The full name of the repository (workspace/repo-slug).
  name: full_name
  type: string
- description: The name of the repository.
  name: name
  type: string
- description: The URL-friendly slug.
  name: slug
  type: string
- description: The repository description.
  name: description
  type: string
- description: Whether the repository is private.
  name: is_private
  type: boolean
- description: Creation timestamp.
  name: created_on
  type: string
- description: Last update timestamp.
  name: updated_on
  type: string
- description: The size of the repository in bytes.
  name: size
  type: integer
- description: The primary programming language.
  name: language
  type: string
- description: ''
  name: has_issues
  type: boolean
- description: ''
  name: has_wiki
  type: boolean
- description: ''
  name: fork_policy
  type: string
- description: ''
  name: scm
  type: string
- description: The project this repository belongs to.
  name: project
  type: object
- description: ''
  name: mainbranch
  type: object
- description: The owner of the repository.
  name: owner
  type: object
provider_name: Bitbucket
provider_slug: bitbucket
schema_file: json-schema/bitbucket-cloud-rest-api-repository-schema.json
slug: bitbucket-cloud-rest-api-repository
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
title: Repository
---
