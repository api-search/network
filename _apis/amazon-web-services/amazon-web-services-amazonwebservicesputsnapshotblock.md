---
aid: amazon-web-services:amazon-web-services-amazonwebservicesputsnapshotblock
name: Putsnapshotblock
tags:
- API
humanURL: 
properties: []
description: >-
  Writes a block of data to a snapshot. If the specified block contains data, the existing data is overwritten. The target snapshot must be in the pending state. Data written to a snapshot must be aligned with 512-KiB sectors.  You should always retry requests that receive server (5xx) error responses, and ThrottlingException and RequestThrottledException client error responses. For more information see Error retries in the Amazon Elastic Compute Cloud User Guide.

---
