---
description: ''
layout: schema
name: PendingDeployment
properties_list:
- description: ''
  name: environment
  type: object
- description: ''
  name: wait_timer
  type: integer
- description: ''
  name: wait_timer_started_at
  type: string
- description: ''
  name: current_user_can_approve
  type: boolean
- description: ''
  name: reviewers
  type: array
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-pending-deployment-schema.json
slug: github-actions-pending-deployment
tags: []
title: PendingDeployment
---
