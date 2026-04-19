---
consumed_apis:
- planner
description: Manage plans, tasks, and buckets in Microsoft Planner for team collaboration and project management. Used by project managers and team leads.
layout: capability
name: Microsoft Planner Task Management
operations:
- description: Create a new plan
  method: POST
  name: create-plan
  path: /v1/plans
- description: List plans for a group
  method: GET
  name: list-group-plans
  path: /v1/plans
- description: Get plan details
  method: GET
  name: get-plan
  path: /v1/plans/{planId}
- description: Update a plan
  method: PATCH
  name: update-plan
  path: /v1/plans/{planId}
- description: Delete a plan
  method: DELETE
  name: delete-plan
  path: /v1/plans/{planId}
- description: Create a new task
  method: POST
  name: create-task
  path: /v1/tasks
- description: Get task details
  method: GET
  name: get-task
  path: /v1/tasks/{taskId}
- description: Update a task
  method: PATCH
  name: update-task
  path: /v1/tasks/{taskId}
- description: Delete a task
  method: DELETE
  name: delete-task
  path: /v1/tasks/{taskId}
- description: Create a new bucket
  method: POST
  name: create-bucket
  path: /v1/buckets
- description: Get bucket details
  method: GET
  name: get-bucket
  path: /v1/buckets/{bucketId}
- description: Update a bucket
  method: PATCH
  name: update-bucket
  path: /v1/buckets/{bucketId}
- description: Delete a bucket
  method: DELETE
  name: delete-bucket
  path: /v1/buckets/{bucketId}
personas: []
provider_name: Microsoft Planner
provider_slug: microsoft-planner
search_terms:
- task management
- manage a specific plan
- manage a specific bucket
- delete bucket
- manage buckets
- get plan details
- get task details
- create plan
- delete a plan
- list bucket tasks
- delete a bucket
- list group plans
- get details of a specific task
- create bucket
- get details of a specific plan
- microsoft
- list all tasks in a plan
- update bucket
- create a new task
- list all buckets in a plan
- get details of a specific bucket
- manage tasks
- collaboration
- list plans for a group
- get bucket details
- manage a specific task
- get task
- get plan details including category labels
- create a new task in a plan
- get task details including checklist and references
- update a task
- list plan buckets
- update a bucket
- list tasks in a specific bucket
- project management
- update task details
- planner
- manage plans
- create a new bucket in a plan
- delete task
- create a new planner plan
- create a new bucket
- list plan tasks
- update plan details
- update task details including checklist items
- productivity
- get plan
- list my tasks
- delete a task
- get bucket
- create task
- list tasks assigned to the current user
- microsoft 365
- update task
- update a plan
- update plan
- delete plan
- create a new plan
slug: task-management
tags:
- Microsoft
- Planner
- Task Management
- Collaboration
tools:
- description: Create a new Planner plan
  hints:
    readOnly: false
  name: create-plan
- description: Get details of a specific plan
  hints:
    readOnly: true
  name: get-plan
- description: Update a plan
  hints:
    idempotent: true
    readOnly: false
  name: update-plan
- description: Delete a plan
  hints:
    destructive: true
    idempotent: true
  name: delete-plan
- description: List all tasks in a plan
  hints:
    readOnly: true
  name: list-plan-tasks
- description: List all buckets in a plan
  hints:
    readOnly: true
  name: list-plan-buckets
- description: Get plan details including category labels
  hints:
    readOnly: true
  name: get-plan-details
- description: Update plan details
  hints:
    idempotent: true
    readOnly: false
  name: update-plan-details
- description: Create a new task in a plan
  hints:
    readOnly: false
  name: create-task
- description: Get details of a specific task
  hints:
    readOnly: true
  name: get-task
- description: Update a task
  hints:
    idempotent: true
    readOnly: false
  name: update-task
- description: Delete a task
  hints:
    destructive: true
    idempotent: true
  name: delete-task
- description: Get task details including checklist and references
  hints:
    readOnly: true
  name: get-task-details
- description: Update task details including checklist items
  hints:
    idempotent: true
    readOnly: false
  name: update-task-details
- description: Create a new bucket in a plan
  hints:
    readOnly: false
  name: create-bucket
- description: Get details of a specific bucket
  hints:
    readOnly: true
  name: get-bucket
- description: Update a bucket
  hints:
    idempotent: true
    readOnly: false
  name: update-bucket
- description: Delete a bucket
  hints:
    destructive: true
    idempotent: true
  name: delete-bucket
- description: List tasks in a specific bucket
  hints:
    readOnly: true
  name: list-bucket-tasks
- description: List tasks assigned to the current user
  hints:
    readOnly: true
  name: list-my-tasks
---
