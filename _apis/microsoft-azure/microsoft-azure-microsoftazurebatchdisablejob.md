---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchdisablejob
name: Microsoft Azure Disables The Specified Job, Preventing New Tasks From Running
tags:
- Jobs
humanURL: 
properties: []
description: >-
  The Batch Service immediately moves the Job to the disabling state. Batch then<br>uses the disableTasks parameter to determine what to do with the currently<br>running Tasks of the Job. The Job remains in the disabling state until the<br>disable operation is completed and all Tasks have been dealt with according to<br>the disableTasks option; the Job then moves to the disabled state. No new Tasks<br>are started under the Job until it moves back to active state. If you try to<br>disable a Job ...

---
