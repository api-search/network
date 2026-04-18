---
description: Request body for performing an issue transition.
layout: schema
name: IssueTransitionRequest
properties_list:
- description: A map of field ID to field value to set during the transition.
  name: fields
  type: object
- description: A map of operations to perform on issue fields during the transition.
  name: update
  type: object
- description: Metadata about the history entry.
  name: historyMetadata
  type: object
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-issue-transition-request-schema.json
slug: jira-cloud-platform-rest-issue-transition-request
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: IssueTransitionRequest
---
