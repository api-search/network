---
aid: atlassian:atlassian-atlassiancheckissueexportstatus
name: Check Issue Export Status
tags:
- Issue tracker
humanURL: 
properties: []
description: >-
  This endpoint is used to poll for the progress of an issue export<br>job and return the zip file after the job is complete.<br>As long as the job is running, this will return a 202 response<br>with in the response body a description of the current status.<br><br>After the job has been scheduled, but before it starts executing, the endpoint<br>returns a 202 response with status `ACCEPTED`.<br><br>Once it starts running, it is a 202 response with status `STARTED` and progress filled.<br><br>Aft...

---
