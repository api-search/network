---
description: An application linking a candidate to a job in the ATS.
layout: schema
name: Application
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: remote_id
  type: string
- description: ''
  name: candidate
  type: string
- description: ''
  name: job
  type: string
- description: ''
  name: applied_at
  type: string
- description: ''
  name: rejected_at
  type: string
- description: Candidate source channel.
  name: source
  type: string
- description: ''
  name: credited_to
  type: string
- description: ''
  name: current_stage
  type: string
- description: ''
  name: reject_reason
  type: string
- description: ''
  name: remote_was_deleted
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: modified_at
  type: string
provider_name: Merge
provider_slug: merge
schema_file: json-schema/ats-api-application-schema.json
slug: ats-api-application
tags:
- Integrations
- Platform
- Unified API
title: Application
---
