---
aid: microsoft-graph:microsoft-graph-startapplicationssynchronizationjobs
name: Microsoft Graph Create Start
tags:
- Applications Synchronization
humanURL: 
properties: []
description: >-
  Start an existing synchronization job. If the job is in a paused state, it continues processing changes from the point where it was paused. If the job is in quarantine, the quarantine status is cleared. Don't create scripts to call the start job continuously while it's running because that can cause the service to stop running. Use the start job only when the job is currently paused or in quarantine.

---
