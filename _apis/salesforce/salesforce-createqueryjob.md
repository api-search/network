---
aid: salesforce:salesforce-createqueryjob
name: Salesforce Create a query job
tags:
- Query Jobs
humanURL: 
properties: []
description: >-
  Creates a new query job to extract large volumes of data from Salesforce using a SOQL query. Query jobs are asynchronous; after creating the job, poll the job status until it reaches JobComplete, then retrieve results using the GET /query/{jobId}/results endpoint.

---
