---
consumed_apis:
- project-rest
description: Unified project management workflow combining the Microsoft Project Online REST API for managing projects, tasks, resources, assignments, timesheets, and workflows. Used by project managers, resource managers, and PMO teams.
layout: capability
name: Microsoft Project Management
operations:
- description: List all projects
  method: GET
  name: list-projects
  path: /v1/projects
- description: Create a new project
  method: POST
  name: create-project
  path: /v1/projects
- description: Get project details
  method: GET
  name: get-project
  path: /v1/projects/{projectId}
- description: Delete a project
  method: DELETE
  name: delete-project
  path: /v1/projects/{projectId}
- description: List all tasks in a project
  method: GET
  name: list-tasks
  path: /v1/projects/{projectId}/tasks
- description: List all assignments in a project
  method: GET
  name: list-assignments
  path: /v1/projects/{projectId}/assignments
- description: List enterprise resources
  method: GET
  name: list-resources
  path: /v1/resources
- description: List enterprise calendars
  method: GET
  name: list-calendars
  path: /v1/calendars
- description: List timesheet periods
  method: GET
  name: list-timesheet-periods
  path: /v1/timesheets
personas: []
provider_name: Microsoft Project
provider_slug: microsoft-project
search_terms:
- unified project management workflow for managing projects, tasks, resources, assignments, timesheets, and workflows.
- custom fields, lookup tables, and event handlers
- microsoft
- Project Manager
- single project operations
- delete a project
- project management
- list all tasks in a project
- list stages
- list all timesheet periods
- enterprise resources and task assignments
- list custom fields
- microsoft project
- list all enterprise resources across projects
- resource management
- task creation, dependencies, and scheduling
- gantt charts
- list enterprise resources
- list assignments
- delete a project by id
- create a new enterprise resource
- list all resource assignments in a project
- plans, executes, and tracks projects with task scheduling, resource assignments, and progress reporting.
- assignment management for a project
- program management office managing portfolios, governance workflows, and enterprise configurations.
- timesheet management and approval
- list all microsoft project online projects
- project lifecycle management
- create a new project with name and description
- create draft task
- PMO
- create project
- publish project
- list phases
- create a new task in a project draft
- enterprise resource management
- list all enterprise custom field definitions
- budgeting
- get project
- list all enterprise calendars
- get a specific task from a project
- list resources
- timesheets
- list projects
- list all projects
- create a new project
- task management
- create enterprise resource
- check out project
- list all workflow stages
- project creation, checkout, publishing, and workflow governance
- get project details
- list all workflow phases
- manages enterprise resource pools, capacity planning, and assignment optimization.
- timesheet management
- scheduling
- check out a project for editing
- get details of a specific project by id
- list all assignments in a project
- delete project
- list tasks
- task management for a project
- list timesheet periods
- publish a project draft to make changes visible
- get task
- portfolio management
- list enterprise calendars
- calendar management
- list calendars
slug: project-management
tags:
- Microsoft Project
- Project Management
- Resource Management
- Task Management
- Timesheets
tools:
- description: List all Microsoft Project Online projects
  hints:
    openWorld: true
    readOnly: true
  name: list-projects
- description: Get details of a specific project by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-project
- description: Create a new project with name and description
  hints:
    readOnly: false
  name: create-project
- description: Delete a project by ID
  hints:
    destructive: true
    readOnly: false
  name: delete-project
- description: Check out a project for editing
  hints:
    readOnly: false
  name: check-out-project
- description: Publish a project draft to make changes visible
  hints:
    readOnly: false
  name: publish-project
- description: List all tasks in a project
  hints:
    idempotent: true
    readOnly: true
  name: list-tasks
- description: Get a specific task from a project
  hints:
    idempotent: true
    readOnly: true
  name: get-task
- description: Create a new task in a project draft
  hints:
    readOnly: false
  name: create-draft-task
- description: List all enterprise resources across projects
  hints:
    openWorld: true
    readOnly: true
  name: list-enterprise-resources
- description: Create a new enterprise resource
  hints:
    readOnly: false
  name: create-enterprise-resource
- description: List all resource assignments in a project
  hints:
    idempotent: true
    readOnly: true
  name: list-assignments
- description: List all enterprise calendars
  hints:
    readOnly: true
  name: list-calendars
- description: List all enterprise custom field definitions
  hints:
    readOnly: true
  name: list-custom-fields
- description: List all timesheet periods
  hints:
    readOnly: true
  name: list-timesheet-periods
- description: List all workflow phases
  hints:
    readOnly: true
  name: list-phases
- description: List all workflow stages
  hints:
    readOnly: true
  name: list-stages
---
