---
aid: salesforce:salesforce-executecompositerequest
name: Salesforce Execute a composite request with dependent subrequests
tags:
- Composite
humanURL: 
properties: []
description: >-
  Executes a series of REST API requests where later requests can reference the results of earlier requests using reference IDs. Supports up to 25 subrequests. If any subrequest fails and allOrNone is true, all changes are rolled back. Use this for complex multi-step operations where later steps depend on earlier results.

---
