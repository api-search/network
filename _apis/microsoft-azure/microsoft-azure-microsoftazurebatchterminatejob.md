---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchterminatejob
name: Microsoft Azure Terminates The Specified Job, Marking It As Completed
tags:
- Jobs
humanURL: 
properties: []
description: >-
  When a Terminate Job request is received, the Batch service sets the Job to the<br>terminating state. The Batch service then terminates any running Tasks<br>associated with the Job and runs any required Job release Tasks. Then the Job<br>moves into the completed state. If there are any Tasks in the Job in the active<br>state, they will remain in the active state. Once a Job is terminated, new<br>Tasks cannot be added and any remaining active Tasks will not be scheduled.

---
