---
description: Request body for creating an issue.
layout: schema
name: IssueCreateRequest
properties_list:
- description: A map of operations to perform on issue fields. Each key is a field ID and the value is an array of operations.
  name: update
  type: object
- description: A map of field ID to field value for the issue. Required fields depend on the project and issue type.
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
schema_file: json-schema/jira-cloud-platform-rest-issue-create-request-schema.json
slug: jira-cloud-platform-rest-issue-create-request
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: IssueCreateRequest
---
