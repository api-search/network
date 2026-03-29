---
aid: amazon-web-services:amazon-web-services-amazonwebservicesstartsnapshot
name: Startsnapshot
tags:
- API
humanURL: 
properties: []
description: >-
  Creates a new Amazon EBS snapshot. The new snapshot enters the pending state after the request completes.  After creating the snapshot, use  PutSnapshotBlock to write blocks of data to the snapshot.  You should always retry requests that receive server (5xx) error responses, and ThrottlingException and RequestThrottledException client error responses. For more information see Error retries in the Amazon Elastic Compute Cloud User Guide.

---
