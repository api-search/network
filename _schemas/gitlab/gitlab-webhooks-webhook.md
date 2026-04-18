---
description: Webhook from GitLab API
layout: schema
name: Webhook
properties_list:
- description: The unique identifier of the webhook.
  name: id
  type: integer
- description: The URL that receives webhook POST requests.
  name: url
  type: string
- description: Optional name for the webhook.
  name: name
  type: string
- description: Optional description of the webhook.
  name: description
  type: string
- description: The ID of the project the webhook belongs to.
  name: project_id
  type: integer
- description: The date and time the webhook was created.
  name: created_at
  type: string
- description: Whether the webhook triggers on push events.
  name: push_events
  type: boolean
- description: Whether the webhook triggers on tag push events.
  name: tag_push_events
  type: boolean
- description: Whether the webhook triggers on issue events.
  name: issues_events
  type: boolean
- description: Whether the webhook triggers on confidential issue events.
  name: confidential_issues_events
  type: boolean
- description: Whether the webhook triggers on merge request events.
  name: merge_requests_events
  type: boolean
- description: Whether the webhook triggers on comment events.
  name: note_events
  type: boolean
- description: Whether the webhook triggers on confidential comment events.
  name: confidential_note_events
  type: boolean
- description: Whether the webhook triggers on job status change events.
  name: job_events
  type: boolean
- description: Whether the webhook triggers on pipeline status change events.
  name: pipeline_events
  type: boolean
- description: Whether the webhook triggers on wiki page events.
  name: wiki_page_events
  type: boolean
- description: Whether the webhook triggers on deployment events.
  name: deployment_events
  type: boolean
- description: Whether the webhook triggers on release events.
  name: releases_events
  type: boolean
- description: Whether the webhook triggers on group member events.
  name: member_events
  type: boolean
- description: Whether SSL certificate verification is enabled for the webhook URL.
  name: enable_ssl_verification
  type: boolean
- description: Branch name or wildcard pattern to filter push events.
  name: push_events_branch_filter
  type: string
- description: The strategy used for filtering branches.
  name: branch_filter_strategy
  type: string
- description: The current alert status of the webhook based on delivery failures.
  name: alert_status
  type: string
- description: If set, the webhook is temporarily disabled until this time.
  name: disabled_until
  type: string
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-webhooks-webhook-schema.json
slug: gitlab-webhooks-webhook
tags:
- Code
- Platform
- Software Development
- Source Control
title: Webhook
---
