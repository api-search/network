---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchenablejob
name: Microsoft Azure Enables The Specified Job, Allowing New Tasks To Run
tags:
- Jobs
humanURL: 
properties: []
description: >-
  When you call this API, the Batch service sets a disabled Job to the enabling<br>state. After the this operation is completed, the Job moves to the active<br>state, and scheduling of new Tasks under the Job resumes. The Batch service<br>does not allow a Task to remain in the active state for more than 180 days.<br>Therefore, if you enable a Job containing active Tasks which were added more<br>than 180 days ago, those Tasks will not run.

---
