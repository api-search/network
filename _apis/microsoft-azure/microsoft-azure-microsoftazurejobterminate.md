---
aid: microsoft-azure:microsoft-azure-microsoftazurejobterminate
name: Microsoft Azure Terminates The Specified Job, Marking It As Completed
tags:
- Jobs
humanURL: 
properties: []
description: >-
  When a Terminate Job request is received, the Batch service sets the Job to the terminating state. The Batch service then terminates any running Tasks associated with the Job and runs any required Job release Tasks. Then the Job moves into the completed state. If there are any Tasks in the Job in the active state, they will remain in the active state. Once a Job is terminated, new Tasks cannot be added and any remaining active Tasks will not be scheduled.

---
