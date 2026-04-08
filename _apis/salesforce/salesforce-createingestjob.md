---
aid: salesforce:salesforce-createingestjob
name: Salesforce Create an ingest job
tags:
- Ingest Jobs
humanURL: 
properties: []
description: >-
  Creates a new ingest job for bulk data operations (insert, update, upsert, delete, or hardDelete). After creating the job, upload data using the PUT /ingest/{jobId}/batches endpoint, then close the job to begin processing. Monitor the job state until it reaches JobComplete or Failed.

---
