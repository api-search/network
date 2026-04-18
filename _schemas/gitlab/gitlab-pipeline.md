---
description: A GitLab CI/CD pipeline that runs automated jobs defined in a .gitlab-ci.yml configuration file.
layout: schema
name: GitLab Pipeline
properties_list:
- description: The unique identifier of the pipeline.
  name: id
  type: integer
- description: The project-scoped sequential ID of the pipeline.
  name: iid
  type: integer
- description: The ID of the project the pipeline belongs to.
  name: project_id
  type: integer
- description: The user-defined name of the pipeline.
  name: name
  type:
  - string
  - 'null'
- description: The current execution status of the pipeline.
  name: status
  type: string
- description: The source that triggered the pipeline.
  name: source
  type: string
- description: The branch name, tag name, or commit SHA the pipeline runs on.
  name: ref
  type: string
- description: The full SHA of the commit the pipeline runs on.
  name: sha
  type: string
- description: Whether the pipeline was triggered by a tag push.
  name: tag
  type: boolean
- description: YAML configuration validation errors, if any.
  name: yaml_errors
  type:
  - string
  - 'null'
- description: ''
  name: user
  type: object
- description: The URL to view the pipeline in a browser.
  name: web_url
  type: string
- description: The SHA of the commit before the pipeline was triggered.
  name: before_sha
  type: string
- description: The total duration of the pipeline in seconds.
  name: duration
  type:
  - integer
  - 'null'
- description: The time in seconds the pipeline spent in the queue before starting.
  name: queued_duration
  type:
  - number
  - 'null'
- description: The code coverage percentage reported by the pipeline.
  name: coverage
  type:
  - string
  - 'null'
- description: Whether the pipeline has been archived.
  name: archived
  type: boolean
- description: The date and time the pipeline was created.
  name: created_at
  type: string
- description: The date and time the pipeline was last updated.
  name: updated_at
  type: string
- description: The date and time the pipeline started execution.
  name: started_at
  type:
  - string
  - 'null'
- description: The date and time the pipeline finished execution.
  name: finished_at
  type:
  - string
  - 'null'
- description: The date and time of the commit that triggered the pipeline.
  name: committed_at
  type:
  - string
  - 'null'
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-pipeline-schema.json
slug: gitlab-pipeline
tags:
- Code
- Platform
- Software Development
- Source Control
title: GitLab Pipeline
---
