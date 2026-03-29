---
aid: amazon-web-services:amazon-web-services-amazonwebservicesupdaterecords
name: Updaterecords
tags:
- API
humanURL: 
properties: []
description: >-
  Posts updates to records and adds and deletes records for a dataset and user. The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the curre...

---
