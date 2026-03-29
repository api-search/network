---
aid: amazon-web-services:amazon-web-services-amazonwebservicesdeleteobjectsoncancel
name: Deleteobjectsoncancel
tags:
- API
humanURL: 
properties: []
description: >-
  For a specific governed table, provides a list of Amazon S3 objects that will be written during the current transaction and that can be automatically deleted if the transaction is canceled. Without this call, no Amazon S3 objects are automatically deleted when a transaction cancels.   The Glue ETL library function write_dynamic_frame.from_catalog() includes an option to automatically call DeleteObjectsOnCancel before writes. For more information, see Rolling Back Amazon S3 Writes.

---
