---
description: A GitLab merge request proposing changes from a source branch to be merged into a target branch within a project.
layout: schema
name: GitLab Merge Request
properties_list:
- description: The globally unique identifier of the merge request.
  name: id
  type: integer
- description: The internal project-scoped ID of the merge request.
  name: iid
  type: integer
- description: The ID of the project the merge request belongs to.
  name: project_id
  type: integer
- description: The title of the merge request.
  name: title
  type: string
- description: The description of the merge request, supporting Markdown syntax.
  name: description
  type:
  - string
  - 'null'
- description: The current state of the merge request.
  name: state
  type: string
- description: Whether the merge request is in draft state and not ready for review.
  name: draft
  type: boolean
- description: The name of the source branch containing the changes.
  name: source_branch
  type: string
- description: The name of the target branch to merge changes into.
  name: target_branch
  type: string
- description: The ID of the project containing the source branch.
  name: source_project_id
  type: integer
- description: The ID of the project containing the target branch.
  name: target_project_id
  type: integer
- description: ''
  name: author
  type: object
- description: Users assigned to review and merge this merge request.
  name: assignees
  type: array
- description: Users requested to review this merge request.
  name: reviewers
  type: array
- description: The user who merged the merge request.
  name: merge_user
  type: object
- description: Labels applied to the merge request.
  name: labels
  type: array
- description: The milestone the merge request is associated with.
  name: milestone
  type: object
- description: The detailed merge readiness status of the merge request.
  name: detailed_merge_status
  type: string
- description: The HEAD commit SHA of the source branch.
  name: sha
  type:
  - string
  - 'null'
- description: The SHA of the merge commit, set after merging.
  name: merge_commit_sha
  type:
  - string
  - 'null'
- description: The SHA of the squash commit, set after squash merging.
  name: squash_commit_sha
  type:
  - string
  - 'null'
- description: Whether the merge request is configured to squash commits on merge.
  name: squash
  type: boolean
- description: ''
  name: references
  type: object
- description: The URL to view the merge request in a browser.
  name: web_url
  type: string
- description: The number of upvotes the merge request has received.
  name: upvotes
  type: integer
- description: The number of downvotes the merge request has received.
  name: downvotes
  type: integer
- description: The number of user-authored comments on the merge request.
  name: user_notes_count
  type: integer
- description: The number of files changed. May be a string for large diffs.
  name: changes_count
  type:
  - string
  - 'null'
- description: The date and time the merge request was created.
  name: created_at
  type: string
- description: The date and time the merge request was last updated.
  name: updated_at
  type: string
- description: The date and time the merge request was merged.
  name: merged_at
  type:
  - string
  - 'null'
- description: The date and time the merge request was prepared for merging.
  name: prepared_at
  type:
  - string
  - 'null'
- description: The date and time the merge request was closed without merging.
  name: closed_at
  type:
  - string
  - 'null'
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-merge-request-schema.json
slug: gitlab-merge-request
tags:
- Code
- Platform
- Software Development
- Source Control
title: GitLab Merge Request
---
