---
description: Represents a Planner task in Microsoft 365 as defined by the Microsoft Graph API v1.0. A task is contained in a plannerPlan and can be assigned to a plannerBucket within the plan. Each task can be assigned to users, categorized, and tracked for completion.
layout: schema
name: Microsoft Planner Task
properties_list:
- description: The ETag of the resource, used for optimistic concurrency control via the If-Match header on PATCH and DELETE operations.
  name: '@odata.etag'
  type: string
- description: Read-only unique identifier of the task. It is 28 characters long and case-sensitive. Format validation is performed by the service.
  name: id
  type: string
- description: Title of the task.
  name: title
  type: string
- description: The ID of the plan to which the task belongs. Tasks cannot be created without specifying a plan.
  name: planId
  type: string
- description: The ID of the bucket to which the task belongs. The bucket must be in the same plan as the task. It is 28 characters long and case-sensitive.
  name: bucketId
  type:
  - string
  - 'null'
- description: The set of assignees the task is assigned to. Each key is the user ID of the assignee.
  name: assignments
  type: object
- description: The categories (labels) applied to the task. Category names are defined on the plan details.
  name: appliedCategories
  type: object
- description: Priority of the task. Valid range is 0-10, with 0 being highest priority. Values 0-1 map to 'urgent', 2-4 to 'important', 5-7 to 'medium', and 8-10 to 'low'. Planner sets 1 for urgent, 3 for important
  name: priority
  type: integer
- description: Percentage of task completion. When set to 100, the task is considered completed.
  name: percentComplete
  type: integer
- description: Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time.
  name: startDateTime
  type:
  - string
  - 'null'
- description: Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time.
  name: dueDateTime
  type:
  - string
  - 'null'
- description: Read-only. Date and time at which the percentComplete of the task was set to 100. ISO 8601 format, always in UTC.
  name: completedDateTime
  type:
  - string
  - 'null'
- description: Read-only. Identity of the user that completed the task.
  name: completedBy
  type: object
- description: Read-only. Date and time at which the task was created. ISO 8601 format, always in UTC.
  name: createdDateTime
  type: string
- description: Read-only. Identity of the user that created the task.
  name: createdBy
  type: object
- description: Read-only. True if the details object of the task has a nonempty description, false otherwise.
  name: hasDescription
  type: boolean
- description: Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.
  name: conversationThreadId
  type:
  - string
  - 'null'
- description: Hint used to order items of this type in a list view. The format is defined by the Planner order hints specification.
  name: orderHint
  type: string
- description: Hint used to order items of this type in a list view when grouped by the user assigned to.
  name: assigneePriority
  type: string
- description: The type of preview that shows up on the task.
  name: previewType
  type: string
- description: Read-only. Number of checklist items with value set to false, representing incomplete items.
  name: activeChecklistItemCount
  type: integer
- description: Read-only. Total number of checklist items present on the task.
  name: checklistItemCount
  type: integer
- description: Read-only. Number of external references that exist on the task.
  name: referenceCount
  type: integer
provider_name: Microsoft Planner
provider_slug: microsoft-planner
schema_file: json-schema/microsoft-planner-task-schema.json
slug: microsoft-planner-task
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
title: Microsoft Planner Task
---
