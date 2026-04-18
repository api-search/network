---
description: A Jira project used to organize and track issues. Projects can be software, service desk, or business type and may be team-managed (next-gen) or company-managed (classic).
layout: schema
name: Jira Project
properties_list:
- description: The URL of the project in the Jira REST API.
  name: self
  type: string
- description: The unique identifier of the project.
  name: id
  type: string
- description: The project key used as a prefix for issue keys (e.g., PROJ).
  name: key
  type: string
- description: The name of the project.
  name: name
  type: string
- description: A description of the project.
  name: description
  type:
  - string
  - 'null'
- description: A URL associated with the project.
  name: url
  type:
  - string
  - 'null'
- description: ''
  name: lead
  type: object
- description: The type of the project.
  name: projectTypeKey
  type: string
- description: Whether the project uses simplified (team-managed/next-gen) configuration.
  name: simplified
  type: boolean
- description: The project style indicating its management model.
  name: style
  type: string
- description: Whether the project is archived.
  name: archived
  type: boolean
- description: Whether the project is in the trash.
  name: deleted
  type: boolean
- description: The default assignee type when creating issues in this project.
  name: assigneeType
  type: string
- description: The components defined in the project.
  name: components
  type: array
- description: The issue types available in the project.
  name: issueTypes
  type: array
- description: The versions (releases) defined in the project.
  name: versions
  type: array
- description: A mapping of role names to their REST API URLs.
  name: roles
  type: object
- description: ''
  name: avatarUrls
  type: object
- description: ''
  name: projectCategory
  type: object
- description: ''
  name: insight
  type: object
- description: ''
  name: permissions
  type: object
- description: Entity properties stored on the project.
  name: properties
  type: object
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-project-schema.json
slug: jira-project
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: Jira Project
---
