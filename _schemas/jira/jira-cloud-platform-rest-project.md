---
description: A Jira project.
layout: schema
name: Project
properties_list:
- description: The URL of the project in the REST API.
  name: self
  type: string
- description: The ID of the project.
  name: id
  type: string
- description: The key of the project (e.g., PROJ).
  name: key
  type: string
- description: The name of the project.
  name: name
  type: string
- description: A description of the project.
  name: description
  type: string
- description: Components in the project.
  name: components
  type: array
- description: Issue types available in the project.
  name: issueTypes
  type: array
- description: A URL to the project.
  name: url
  type: string
- description: The default assignee type for the project.
  name: assigneeType
  type: string
- description: The versions defined in the project.
  name: versions
  type: array
- description: Project role URLs.
  name: roles
  type: object
- description: The project type.
  name: projectTypeKey
  type: string
- description: Whether the project is simplified (next-gen/team-managed).
  name: simplified
  type: boolean
- description: The style of the project. Classic or next-gen.
  name: style
  type: string
- description: Whether the project is archived.
  name: archived
  type: boolean
- description: Whether the project is marked as deleted.
  name: deleted
  type: boolean
- description: Insight information about the project.
  name: insight
  type: object
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-project-schema.json
slug: jira-cloud-platform-rest-project
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: Project
---
