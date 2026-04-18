---
description: Details of a newly created issue.
layout: schema
name: CreatedIssue
properties_list:
- description: The ID of the created issue.
  name: id
  type: string
- description: The key of the created issue (e.g., PROJ-123).
  name: key
  type: string
- description: The URL of the created issue in the REST API.
  name: self
  type: string
- description: Status of the transition applied during creation.
  name: transition
  type: object
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-created-issue-schema.json
slug: jira-cloud-platform-rest-created-issue
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: CreatedIssue
---
