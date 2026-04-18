---
description: ''
layout: schema
name: SelfHostedRunner
properties_list:
- description: The id of the runner.
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
- description: ''
  name: busy
  type: boolean
- description: ''
  name: labels
  type: array
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-self-hosted-runner-schema.json
slug: github-actions-self-hosted-runner
tags: []
title: SelfHostedRunner
---
