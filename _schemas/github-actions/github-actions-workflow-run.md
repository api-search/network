---
description: ''
layout: schema
name: WorkflowRun
properties_list:
- description: The ID of the workflow run.
  name: id
  type: integer
- description: The name of the workflow run.
  name: name
  type: string
- description: ''
  name: node_id
  type: string
- description: ''
  name: head_branch
  type: string
- description: The SHA of the head commit that points to the version of the workflow being run.
  name: head_sha
  type: string
- description: ''
  name: path
  type: string
- description: The title of the workflow run displayed in the UI.
  name: display_title
  type: string
- description: The auto incrementing run number for the workflow run.
  name: run_number
  type: integer
- description: Attempt number of the run, 1 for first attempt and higher if the workflow was re-run.
  name: run_attempt
  type: integer
- description: The event that triggered the workflow run.
  name: event
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: conclusion
  type: string
- description: ''
  name: workflow_id
  type: integer
- description: ''
  name: url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: run_started_at
  type: string
- description: ''
  name: jobs_url
  type: string
- description: ''
  name: logs_url
  type: string
- description: ''
  name: artifacts_url
  type: string
- description: ''
  name: cancel_url
  type: string
- description: ''
  name: rerun_url
  type: string
- description: ''
  name: workflow_url
  type: string
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-workflow-run-schema.json
slug: github-actions-workflow-run
tags: []
title: WorkflowRun
---
