---
aid: amazon-web-services:amazon-web-services-amazonwebservicesuploadmultipartpart
name: Uploadmultipartpart
tags:
- API
humanURL: 
properties: []
description: >-
  This operation uploads a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload. Amazon Glacier rejects your upload part request if any of the following conditions is true:    SHA256 tree hash does not matchTo ensure that part data is not corrupted in transmission, you compute a SHA256 tree hash of the part and include it in your request. Upon receiving the part data, Amazon S3 Glacier also ...

---
