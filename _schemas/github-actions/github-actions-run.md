---
description: Represents a single execution of a GitHub Actions workflow.
layout: schema
name: GitHub Actions Workflow Run
properties_list:
- description: The unique identifier of the workflow run.
  name: id
  type: integer
- description: The name of the workflow run.
  name: name
  type:
  - string
  - 'null'
- description: The GraphQL node ID of the workflow run.
  name: node_id
  type: string
- description: The branch associated with the workflow run's head commit.
  name: head_branch
  type:
  - string
  - 'null'
- description: The SHA of the head commit that points to the version of the workflow being run.
  name: head_sha
  type: string
- description: The path of the workflow file.
  name: path
  type: string
- description: The title of the workflow run as displayed in the GitHub UI.
  name: display_title
  type: string
- description: The auto-incrementing run number for the workflow run.
  name: run_number
  type: integer
- description: Attempt number of the run. 1 for the first attempt and higher if the workflow was re-run.
  name: run_attempt
  type: integer
- description: The event that triggered the workflow run.
  name: event
  type: string
- description: The current status of the workflow run.
  name: status
  type:
  - string
  - 'null'
- description: The result of the completed workflow run.
  name: conclusion
  type:
  - string
  - 'null'
- description: The ID of the parent workflow.
  name: workflow_id
  type: integer
- description: The API URL of the workflow run.
  name: url
  type: string
- description: The HTML URL of the workflow run on GitHub.
  name: html_url
  type: string
- description: The date and time the workflow run was created.
  name: created_at
  type: string
- description: The date and time the workflow run was last updated.
  name: updated_at
  type: string
- description: The date and time the workflow run started executing.
  name: run_started_at
  type: string
- description: The API URL for the jobs in this workflow run.
  name: jobs_url
  type: string
- description: The API URL for the logs of this workflow run.
  name: logs_url
  type: string
- description: The API URL for the artifacts of this workflow run.
  name: artifacts_url
  type: string
- description: The API URL to cancel this workflow run.
  name: cancel_url
  type: string
- description: The API URL to re-run this workflow run.
  name: rerun_url
  type: string
- description: The API URL of the parent workflow.
  name: workflow_url
  type: string
- description: The user who triggered the workflow run.
  name: actor
  type: object
- description: The user who triggered the workflow run (may differ from actor for re-runs).
  name: triggering_actor
  type: object
- description: The head commit for the workflow run.
  name: head_commit
  type:
  - object
  - 'null'
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-run-schema.json
slug: github-actions-run
tags: []
title: GitHub Actions Workflow Run
---
