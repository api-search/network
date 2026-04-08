---
aid: microsoft-azure:microsoft-azure-microsoftazuretaskreactivate
name: Microsoft Azure Reactivates A Task, Allowing It To Run Again Even If Its Retry Count Has Been Exhausted
tags:
- Tasks
humanURL: 
properties: []
description: >-
  Reactivation makes a Task eligible to be retried again up to its maximum retry count. The Task's state is changed to active. As the Task is no longer in the completed state, any previous exit code or failure information is no longer available after reactivation. Each time a Task is reactivated, its retry count is reset to 0. Reactivation will fail for Tasks that are not completed or that previously completed successfully (with an exit code of 0). Additionally, it will fail if the Job has comp...

---
