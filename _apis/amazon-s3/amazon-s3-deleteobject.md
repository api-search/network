---
aid: amazon-s3:amazon-s3-deleteobject
name: Delete Object
tags:
- Objects
humanURL: 
properties: []
description: >-
  Removes the null version (if there is one) of an object and inserts a delete marker, which becomes the latest version of the object. If there is no null version, Amazon S3 does not remove any objects but will still respond that the command was successful. To remove a specific version, you must use the versionId sub-resource.

---
