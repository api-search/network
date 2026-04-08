---
aid: microsoft-azure:microsoft-azure-microsoftazuredeploymentsdeleteatscope
name: Microsoft Azure Deletes A Deployment From The Deployment History
tags:
- Deployments
humanURL: 
properties: []
description: >-
  A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the L...

---
