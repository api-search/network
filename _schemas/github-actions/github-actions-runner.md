---
description: Represents a self-hosted runner configured for GitHub Actions.
layout: schema
name: GitHub Actions Self-Hosted Runner
properties_list:
- description: The unique identifier of the runner.
  name: id
  type: integer
- description: The name of the runner.
  name: name
  type: string
- description: The operating system of the runner.
  name: os
  type: string
- description: The status of the runner.
  name: status
  type: string
- description: Whether the runner is currently executing a job.
  name: busy
  type: boolean
- description: Labels assigned to the runner.
  name: labels
  type: array
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-runner-schema.json
slug: github-actions-runner
tags: []
title: GitHub Actions Self-Hosted Runner
---
