---
aid: atlassian:atlassian-atlassiancheckissueimportstatus
name: Check Issue Import Status
tags:
- Issue tracker
humanURL: 
properties: []
description: >-
  When using GET, this endpoint reports the status of the current import task.<br><br>After the job has been scheduled, but before it starts executing, the endpoint<br>returns a 202 response with status `ACCEPTED`.<br><br>Once it starts running, it is a 202 response with status `STARTED` and progress filled.<br><br>After it is finished, it becomes a 200 response with status `SUCCESS` or `FAILURE`.

---
