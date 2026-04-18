---
description: Represents a Planner task in Microsoft 365. A task is contained in a plan and can be assigned to a bucket within the plan.
layout: schema
name: PlannerTask
properties_list:
- description: The ETag of the resource, used for concurrency control
  name: '@odata.etag'
  type: string
- description: The unique identifier for the task. 28 characters long and case-sensitive.
  name: id
  type: string
- description: Title of the task
  name: title
  type: string
- description: Plan ID to which the task belongs
  name: planId
  type: string
- description: Bucket ID to which the task belongs. The bucket must be in the same plan as the task. 28 characters long and case-sensitive.
  name: bucketId
  type: '[''string'', ''null'']'
- description: Priority of the task. Valid range is 0-10 where 0 is highest priority. Values 0-1 are urgent, 2-4 are important, 5-7 are medium, 8-10 are low.
  name: priority
  type: integer
- description: Percentage of task completion. When set to 100, the task is considered completed.
  name: percentComplete
  type: integer
- description: Date and time at which the task starts. ISO 8601 format, always in UTC.
  name: startDateTime
  type: '[''string'', ''null'']'
- description: Date and time at which the task is due. ISO 8601 format, always in UTC.
  name: dueDateTime
  type: '[''string'', ''null'']'
- description: Date and time at which the percentComplete was set to 100. ISO 8601 format, always in UTC.
  name: completedDateTime
  type: '[''string'', ''null'']'
- description: Date and time at which the task was created. ISO 8601 format, always in UTC.
  name: createdDateTime
  type: string
- description: Indicates whether the details object of the task has a nonempty description.
  name: hasDescription
  type: boolean
- description: Thread ID of the conversation on the task in the containing group.
  name: conversationThreadId
  type: '[''string'', ''null'']'
- description: Hint used to order items of this type in a list view
  name: orderHint
  type: string
- description: Hint used to order items of this type when grouped by assignee
  name: assigneePriority
  type: string
- description: The type of preview that shows on the task
  name: previewType
  type: string
- description: Number of incomplete checklist items
  name: activeChecklistItemCount
  type: integer
- description: Total number of checklist items on the task
  name: checklistItemCount
  type: integer
- description: Number of external references on the task
  name: referenceCount
  type: integer
provider_name: Microsoft Planner
provider_slug: microsoft-planner
schema_file: json-schema/microsoft-planner-planner-task-schema.json
slug: microsoft-planner-planner-task
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
title: PlannerTask
---
