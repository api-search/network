---
aid: factset:factset-getentitytaskforlist
name: Input a file with names and attributes, creating a taskId.
tags:
- - - - Entity Match - Bulk
humanURL: 
properties: []
description: >-
  Upload a Comma-Separated List file (.csv / UTF-8 encoding) with a list of names and attributes and receive a `taskId`. The taskId is then used for reference in the */entity-task-status* and */entity-decisions* endpoints to receive results once the task is successful.<p>This is the first step in the overall "Bulk" workflow. Use the /entity-task-status endpoint to check the status.</p> <p> A universeId must be included in request. If you do not have a universe created, reference the `/universe`...

---
