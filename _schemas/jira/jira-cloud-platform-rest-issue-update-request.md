---
description: Request body for editing an issue.
layout: schema
name: IssueUpdateRequest
properties_list:
- description: A map of operations to perform on issue fields.
  name: update
  type: object
- description: A map of field ID to field value for the issue.
  name: fields
  type: object
- description: Metadata about the history entry.
  name: historyMetadata
  type: object
- description: Entity properties to set on the issue.
  name: properties
  type: array
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-issue-update-request-schema.json
slug: jira-cloud-platform-rest-issue-update-request
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: IssueUpdateRequest
---
