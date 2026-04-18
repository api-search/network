---
consumed_apis:
- jira-cloud
description: Unified project management workflow combining issue tracking, workflow transitions, JQL search, and project management. Used by project managers, developers, and team leads to manage agile software delivery.
layout: capability
name: Jira Project Management
operations:
- description: Create a new issue.
  method: POST
  name: create-issue
  path: /v1/issues
- description: Get issue details.
  method: GET
  name: get-issue
  path: /v1/issues/{issueIdOrKey}
- description: Edit an issue.
  method: PUT
  name: edit-issue
  path: /v1/issues/{issueIdOrKey}
- description: Delete an issue.
  method: DELETE
  name: delete-issue
  path: /v1/issues/{issueIdOrKey}
- description: Get available transitions.
  method: GET
  name: get-transitions
  path: /v1/issues/{issueIdOrKey}/transitions
- description: Perform a transition.
  method: POST
  name: do-transition
  path: /v1/issues/{issueIdOrKey}/transitions
- description: Get issue comments.
  method: GET
  name: get-comments
  path: /v1/issues/{issueIdOrKey}/comments
- description: Add a comment.
  method: POST
  name: add-comment
  path: /v1/issues/{issueIdOrKey}/comments
- description: Search with JQL.
  method: GET
  name: search-issues
  path: /v1/search
- description: List all projects.
  method: GET
  name: list-projects
  path: /v1/projects
- description: Get project details.
  method: GET
  name: get-project
  path: /v1/projects/{projectIdOrKey}
personas: []
provider_name: Jira
provider_slug: jira
search_terms:
- create a new jira issue.
- create issue
- search issues
- add a comment.
- edit an issue.
- get jira issue details.
- delete issue
- search with jql.
- jira
- issue comments.
- list all jira projects.
- get all jira priorities.
- get issue
- get project
- get priorities
- service management
- list all projects.
- get project details.
- get comments
- get issue types
- get available transitions.
- add comment
- get comments on a jira issue.
- get statuses
- edit an existing jira issue.
- get issue details.
- agile
- get transitions
- get issue comments.
- delete a jira issue.
- get available workflow transitions.
- search jira issues using jql.
- issue lifecycle management.
- get jira project details.
- delete an issue.
- issue tracking
- perform a transition.
- single project.
- edit issue
- do transition
- single issue operations.
- add a comment to a jira issue.
- get all jira issue types.
- create a new issue.
- jql issue search.
- project management.
- project management
- transition an issue through its workflow.
- get all jira issue statuses.
- itsm
- workflow transitions.
- list projects
slug: project-management
tags:
- Jira
- Project Management
- Issue Tracking
- Agile
tools:
- description: Create a new Jira issue.
  hints:
    readOnly: false
  name: create-issue
- description: Get Jira issue details.
  hints:
    idempotent: true
    readOnly: true
  name: get-issue
- description: Edit an existing Jira issue.
  hints:
    idempotent: true
    readOnly: false
  name: edit-issue
- description: Delete a Jira issue.
  hints:
    destructive: true
    readOnly: false
  name: delete-issue
- description: Get available workflow transitions.
  hints:
    idempotent: true
    readOnly: true
  name: get-transitions
- description: Transition an issue through its workflow.
  hints:
    readOnly: false
  name: do-transition
- description: Get comments on a Jira issue.
  hints:
    idempotent: true
    readOnly: true
  name: get-comments
- description: Add a comment to a Jira issue.
  hints:
    readOnly: false
  name: add-comment
- description: Search Jira issues using JQL.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: search-issues
- description: List all Jira projects.
  hints:
    idempotent: true
    readOnly: true
  name: list-projects
- description: Get Jira project details.
  hints:
    idempotent: true
    readOnly: true
  name: get-project
- description: Get all Jira issue statuses.
  hints:
    idempotent: true
    readOnly: true
  name: get-statuses
- description: Get all Jira issue types.
  hints:
    idempotent: true
    readOnly: true
  name: get-issue-types
- description: Get all Jira priorities.
  hints:
    idempotent: true
    readOnly: true
  name: get-priorities
---
