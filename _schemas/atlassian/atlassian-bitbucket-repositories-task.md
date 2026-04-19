---
description: A task object.
layout: schema
name: task
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: created_on
  type: string
- description: ''
  name: updated_on
  type: string
- description: ''
  name: state
  type: string
- description: ''
  name: content
  type: object
- description: ''
  name: pending
  type: boolean
- description: The ISO8601 timestamp for when the task was resolved.
  name: resolved_on
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-bitbucket-repositories-task-schema.json
slug: atlassian-bitbucket-repositories-task
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: task
---
