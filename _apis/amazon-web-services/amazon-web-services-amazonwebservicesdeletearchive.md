---
aid: amazon-web-services:amazon-web-services-amazonwebservicesdeletearchive
name: Deletearchive
tags:
- API
humanURL: 
properties: []
description: >-
  This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:   If the archive retrieval job is actively preparing the data for download when Amazon S3 Glacier receives the delete archive request, the archival retrieval operation might fail.   If the archive retrieval job has successfully prepared the archive for down...

---
