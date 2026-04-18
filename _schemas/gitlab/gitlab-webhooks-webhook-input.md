---
description: WebhookInput from GitLab API
layout: schema
name: WebhookInput
properties_list:
- description: The URL to send webhook POST requests to.
  name: url
  type: string
- description: Optional name for the webhook.
  name: name
  type: string
- description: Optional description of the webhook.
  name: description
  type: string
- description: A secret token to validate received payloads. Sent as the X-Gitlab-Token header.
  name: secret_token
  type: string
- description: Whether to verify SSL certificates on the webhook URL.
  name: enable_ssl_verification
  type: boolean
- description: Trigger on push events.
  name: push_events
  type: boolean
- description: Trigger on tag push events.
  name: tag_push_events
  type: boolean
- description: Trigger on issue events.
  name: issues_events
  type: boolean
- description: Trigger on confidential issue events.
  name: confidential_issues_events
  type: boolean
- description: Trigger on merge request events.
  name: merge_requests_events
  type: boolean
- description: Trigger on comment events.
  name: note_events
  type: boolean
- description: Trigger on confidential comment events.
  name: confidential_note_events
  type: boolean
- description: Trigger on job status change events.
  name: job_events
  type: boolean
- description: Trigger on pipeline status change events.
  name: pipeline_events
  type: boolean
- description: Trigger on wiki page events.
  name: wiki_page_events
  type: boolean
- description: Trigger on deployment events.
  name: deployment_events
  type: boolean
- description: Trigger on release events.
  name: releases_events
  type: boolean
- description: Trigger on group member events.
  name: member_events
  type: boolean
- description: Branch name or wildcard pattern to filter push events.
  name: push_events_branch_filter
  type: string
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-webhooks-webhook-input-schema.json
slug: gitlab-webhooks-webhook-input
tags:
- Code
- Platform
- Software Development
- Source Control
title: WebhookInput
---
