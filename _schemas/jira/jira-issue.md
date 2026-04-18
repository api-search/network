---
description: A Jira issue representing a unit of work such as a bug, story, task, epic, or sub-task tracked within a Jira project.
layout: schema
name: Jira Issue
properties_list:
- description: The unique identifier of the issue.
  name: id
  type: string
- description: The key of the issue in PROJECT-NUMBER format (e.g., PROJ-123).
  name: key
  type: string
- description: The URL of the issue in the Jira REST API.
  name: self
  type: string
- description: The expand options applied to the issue response.
  name: expand
  type: string
- description: ''
  name: fields
  type: object
- description: HTML-rendered versions of applicable issue fields.
  name: renderedFields
  type: object
- description: A mapping of field IDs to their human-readable names.
  name: names
  type: object
- description: JSON Schema definitions for each field on the issue.
  name: schema
  type: object
- description: The list of workflow transitions available for the issue.
  name: transitions
  type: array
- description: ''
  name: changelog
  type: object
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-issue-schema.json
slug: jira-issue
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: Jira Issue
---
