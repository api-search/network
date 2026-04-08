---
aid: microsoft-azure:microsoft-azure-microsoftazuretaskdelete
name: Microsoft Azure Deletes A Task From The Specified Job
tags:
- Tasks
humanURL: 
properties: []
description: >-
  When a Task is deleted, all of the files in its directory on the Compute Node where it ran are also deleted (regardless of the retention time). For multi-instance Tasks, the delete Task operation applies synchronously to the primary task; subtasks and their files are then deleted asynchronously in the background.

---
