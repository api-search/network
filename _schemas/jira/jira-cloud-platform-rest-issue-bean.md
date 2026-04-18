---
description: A Jira issue with all fields and metadata.
layout: schema
name: IssueBean
properties_list:
- description: The ID of the issue.
  name: id
  type: string
- description: The key of the issue (e.g., PROJ-123).
  name: key
  type: string
- description: The URL of the issue in the REST API.
  name: self
  type: string
- description: The expand options applied to the issue.
  name: expand
  type: string
- description: HTML-rendered versions of the issue fields.
  name: renderedFields
  type: object
- description: Field name mapping for the issue.
  name: names
  type: object
- description: JSON Schema for each field in the issue.
  name: schema
  type: object
- description: Transitions available for the issue.
  name: transitions
  type: array
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-issue-bean-schema.json
slug: jira-cloud-platform-rest-issue-bean
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: IssueBean
---
