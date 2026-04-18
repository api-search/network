---
description: A Bitbucket Pipelines CI/CD pipeline.
layout: schema
name: Pipeline
properties_list:
- description: ''
  name: type
  type: string
- description: The pipeline UUID.
  name: uuid
  type: string
- description: The build number.
  name: build_number
  type: integer
- description: The user who triggered the pipeline.
  name: creator
  type: object
- description: The repository.
  name: repository
  type: object
- description: The pipeline target (branch, tag, etc.).
  name: target
  type: object
- description: The pipeline state.
  name: state
  type: object
- description: ''
  name: created_on
  type: string
- description: ''
  name: completed_on
  type: string
- description: ''
  name: build_seconds_used
  type: integer
provider_name: Bitbucket
provider_slug: bitbucket
schema_file: json-schema/bitbucket-cloud-rest-api-pipeline-schema.json
slug: bitbucket-cloud-rest-api-pipeline
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
title: Pipeline
---
