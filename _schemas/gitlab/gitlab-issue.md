---
description: A GitLab issue used for tracking work, bugs, feature requests, or incidents within a project.
layout: schema
name: GitLab Issue
properties_list:
- description: The globally unique identifier of the issue.
  name: id
  type: integer
- description: The internal project-scoped ID of the issue.
  name: iid
  type: integer
- description: The ID of the project the issue belongs to.
  name: project_id
  type: integer
- description: The title of the issue.
  name: title
  type: string
- description: The description of the issue, supporting Markdown syntax.
  name: description
  type:
  - string
  - 'null'
- description: The current state of the issue.
  name: state
  type: string
- description: The type of issue.
  name: issue_type
  type: string
- description: The GitLab-internal issue type designation.
  name: type
  type: string
- description: Labels applied to the issue.
  name: labels
  type: array
- description: The milestone the issue is associated with.
  name: milestone
  type: object
- description: ''
  name: author
  type: object
- description: Users assigned to work on this issue.
  name: assignees
  type: array
- description: The user who closed the issue.
  name: closed_by
  type: object
- description: Whether the issue is confidential and visible only to project members with Reporter access or above.
  name: confidential
  type: boolean
- description: The weight assigned to the issue for effort estimation. Requires Premium or Ultimate tier.
  name: weight
  type:
  - integer
  - 'null'
- description: The severity level of the issue. Used for incidents.
  name: severity
  type: string
- description: The number of upvotes the issue has received.
  name: upvotes
  type: integer
- description: The number of downvotes the issue has received.
  name: downvotes
  type: integer
- description: The number of user-authored comments on the issue.
  name: user_notes_count
  type: integer
- description: The number of merge requests related to this issue.
  name: merge_requests_count
  type: integer
- description: ''
  name: references
  type: object
- description: The URL to view the issue in a browser.
  name: web_url
  type: string
- description: ''
  name: time_stats
  type: object
- description: ''
  name: task_completion_status
  type: object
- description: Whether the issue description contains task list items.
  name: has_tasks
  type: boolean
- description: The due date of the issue in YYYY-MM-DD format.
  name: due_date
  type:
  - string
  - 'null'
- description: The date and time the issue was created.
  name: created_at
  type: string
- description: The date and time the issue was last updated.
  name: updated_at
  type: string
- description: The date and time the issue was closed.
  name: closed_at
  type:
  - string
  - 'null'
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-issue-schema.json
slug: gitlab-issue
tags:
- Code
- Platform
- Software Development
- Source Control
title: GitLab Issue
---
