---
description: API_Entities_Job model
layout: schema
name: API_Entities_Job
properties_list:
- description: The ID of the job
  name: id
  type: integer
- description: The name of the job
  name: name
  type: string
- description: The current status of the job
  name: status
  type: string
- description: The stage of the job in the CI/CD pipeline
  name: stage
  type: string
- description: The creation time of the job
  name: created_at
  type: string
- description: The start time of the job
  name: started_at
  type: string
- description: The finish time of the job
  name: finished_at
  type: string
- description: ''
  name: commit
  type: object
- description: Indicates if the job is archived
  name: archived
  type: boolean
- description: Indicates if the job is allowed to fail
  name: allow_failure
  type: boolean
- description: The time when the job was erased, if applicable
  name: erased_at
  type: string
- description: The duration of the job in seconds
  name: duration
  type: integer
- description: The duration the job was queued before execution, in seconds
  name: queued_duration
  type: number
- description: The reference for the job
  name: ref
  type: string
- description: The artifacts produced by the job
  name: artifacts
  type: array
- description: Indicates if the job is tagged
  name: tag
  type: boolean
- description: The URL for accessing the job in the web interface
  name: web_url
  type: string
- description: ''
  name: project
  type: object
- description: The user that started the job
  name: user
  type: object
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-api-v4-projects-api_entities_job-schema.json
slug: gitlab-api-v4-projects-api_entities_job
tags:
- Code
- Platform
- Software Development
- Source Control
title: API_Entities_Job
---
