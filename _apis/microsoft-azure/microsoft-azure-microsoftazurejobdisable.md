---
aid: microsoft-azure:microsoft-azure-microsoftazurejobdisable
name: Microsoft Azure Disables The Specified Job, Preventing New Tasks From Running
tags:
- Jobs
humanURL: 
properties: []
description: >-
  The Batch Service immediately moves the Job to the disabling state. Batch then uses the disableTasks parameter to determine what to do with the currently running Tasks of the Job. The Job remains in the disabling state until the disable operation is completed and all Tasks have been dealt with according to the disableTasks option; the Job then moves to the disabled state. No new Tasks are started under the Job until it moves back to active state. If you try to disable a Job that is in any sta...

---
