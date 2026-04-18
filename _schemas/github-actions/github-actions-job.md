---
description: ''
layout: schema
name: Job
properties_list:
- description: The id of the job.
  name: id
  type: integer
- description: The id of the associated workflow run.
  name: run_id
  type: integer
- description: ''
  name: run_url
  type: string
- description: ''
  name: run_attempt
  type: integer
- description: ''
  name: node_id
  type: string
- description: ''
  name: head_sha
  type: string
- description: ''
  name: url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: conclusion
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: started_at
  type: string
- description: ''
  name: completed_at
  type: string
- description: The name of the job.
  name: name
  type: string
- description: ''
  name: steps
  type: array
- description: ''
  name: labels
  type: array
- description: ''
  name: runner_id
  type: integer
- description: ''
  name: runner_name
  type: string
- description: ''
  name: runner_group_id
  type: integer
- description: ''
  name: runner_group_name
  type: string
- description: ''
  name: workflow_name
  type: string
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-job-schema.json
slug: github-actions-job
tags: []
title: Job
---
