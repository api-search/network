---
description: The fields of a Jira issue.
layout: schema
name: IssueFields
properties_list:
- description: The summary (title) of the issue.
  name: summary
  type: string
- description: The description of the issue in Atlassian Document Format (ADF).
  name: description
  type: string
- description: The user assigned to the issue.
  name: assignee
  type: string
- description: Labels applied to the issue.
  name: labels
  type: array
- description: Components associated with the issue.
  name: components
  type: array
- description: Fix versions for the issue.
  name: fixVersions
  type: array
- description: Affected versions for the issue.
  name: versions
  type: array
- description: The resolution of the issue.
  name: resolution
  type: string
- description: The date the issue was resolved.
  name: resolutiondate
  type: '[''string'', ''null'']'
- description: The date and time the issue was created.
  name: created
  type: string
- description: The date and time the issue was last updated.
  name: updated
  type: string
- description: The due date of the issue.
  name: duedate
  type: '[''string'', ''null'']'
- description: Sub-tasks of the issue.
  name: subtasks
  type: array
- description: The parent issue, if this is a sub-task.
  name: parent
  type: string
- description: The environment in which the issue was found in ADF.
  name: environment
  type: string
- description: Attachments on the issue.
  name: attachment
  type: array
- description: Links to other issues.
  name: issuelinks
  type: array
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-issue-fields-schema.json
slug: jira-cloud-platform-rest-issue-fields
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: IssueFields
---
