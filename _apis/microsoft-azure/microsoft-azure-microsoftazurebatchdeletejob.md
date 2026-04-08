---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchdeletejob
name: Microsoft Azure Deletes A Job
tags:
- Jobs
humanURL: 
properties: []
description: >-
  Deleting a Job also deletes all Tasks that are part of that Job, and all Job<br>statistics. This also overrides the retention period for Task data; that is, if<br>the Job contains Tasks which are still retained on Compute Nodes, the Batch<br>services deletes those Tasks' working directories and all their contents.  When<br>a Delete Job request is received, the Batch service sets the Job to the<br>deleting state. All update operations on a Job that is in deleting state will<br>fail with status...

---
