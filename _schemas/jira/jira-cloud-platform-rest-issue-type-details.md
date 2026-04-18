---
description: Details of an issue type.
layout: schema
name: IssueTypeDetails
properties_list:
- description: The URL of the issue type in the REST API.
  name: self
  type: string
- description: The ID of the issue type.
  name: id
  type: string
- description: The description of the issue type.
  name: description
  type: string
- description: The URL of the issue type icon.
  name: iconUrl
  type: string
- description: The name of the issue type (e.g., Bug, Story, Task, Epic).
  name: name
  type: string
- description: Whether this issue type is used to create sub-tasks.
  name: subtask
  type: boolean
- description: The ID of the avatar for the issue type.
  name: avatarId
  type: integer
- description: The hierarchy level of the issue type.
  name: hierarchyLevel
  type: integer
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-issue-type-details-schema.json
slug: jira-cloud-platform-rest-issue-type-details
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: IssueTypeDetails
---
