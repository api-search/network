---
aid: microsoft-azure:microsoft-azure-microsoftazurejobdelete
name: Microsoft Azure Deletes A Job
tags:
- Jobs
humanURL: 
properties: []
description: >-
  Deleting a Job also deletes all Tasks that are part of that Job, and all Job statistics. This also overrides the retention period for Task data; that is, if the Job contains Tasks which are still retained on Compute Nodes, the Batch services deletes those Tasks' working directories and all their contents.  When a Delete Job request is received, the Batch service sets the Job to the deleting state. All update operations on a Job that is in deleting state will fail with status code 409 (Conflic...

---
