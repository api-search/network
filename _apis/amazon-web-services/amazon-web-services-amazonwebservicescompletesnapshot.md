---
aid: amazon-web-services:amazon-web-services-amazonwebservicescompletesnapshot
name: Completesnapshot
tags:
- API
humanURL: 
properties: []
description: >-
  Seals and completes the snapshot after all of the required blocks of data have been written to it. Completing the snapshot changes the status to completed. You cannot write new blocks to a snapshot after it has been completed.  You should always retry requests that receive server (5xx) error responses, and ThrottlingException and RequestThrottledException client error responses. For more information see Error retries in the Amazon Elastic Compute Cloud User Guide.

---
