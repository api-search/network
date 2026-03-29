---
aid: factset:factset-getentitytaskstatus
name: Gets the status of the requested taskId or all tasks for a User
tags:
- - - - Entity Match - Bulk
humanURL: 
properties: []
description: >-
  Pulls the **status** for ALL the Entity Tasks submitted by a client within the last 30 days, and related details such as task duration and decision rates. Specific Tasks can also be retrieved by using the _taskId_ parameter.<p>Status types include -   * PENDING - The task has not yet started.   * IN_PROGRESS - The task is submitted and decisions are in progress.   * SUCCESS - The task was successful! Move to the /entity-decisions endpoint to retrieve decisions.   * FAILURE - The task failed. ...

---
