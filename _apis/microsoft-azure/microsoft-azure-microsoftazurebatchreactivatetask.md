---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchreactivatetask
name: Microsoft Azure Reactivates A Task, Allowing It To Run Again Even If Its Retry Count Has Been
exhausted
tags:
- Jobs
humanURL: 
properties: []
description: >-
  Reactivation makes a Task eligible to be retried again up to its maximum retry<br>count. The Task's state is changed to active. As the Task is no longer in the<br>completed state, any previous exit code or failure information is no longer<br>available after reactivation. Each time a Task is reactivated, its retry count<br>is reset to 0. Reactivation will fail for Tasks that are not completed or that<br>previously completed successfully (with an exit code of 0). Additionally, it<br>will fail i...

---
