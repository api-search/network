---
aid: microsoft-azure:microsoft-azure-microsoftazurejobenable
name: Microsoft Azure Enables The Specified Job, Allowing New Tasks To Run
tags:
- Jobs
humanURL: 
properties: []
description: >-
  When you call this API, the Batch service sets a disabled Job to the enabling state. After the this operation is completed, the Job moves to the active state, and scheduling of new Tasks under the Job resumes. The Batch service does not allow a Task to remain in the active state for more than 180 days. Therefore, if you enable a Job containing active Tasks which were added more than 180 days ago, those Tasks will not run.

---
