---
description: An object consists of data and its descriptive metadata.
layout: schema
name: Object
properties_list:
- description: The name assigned to an object which identifies it in the bucket.
  name: Key
  type: string
- description: Date and time the object was last modified.
  name: LastModified
  type: string
- description: The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object, not its metadata.
  name: ETag
  type: string
- description: Size in bytes of the object.
  name: Size
  type: integer
- description: The class of storage used to store the object.
  name: StorageClass
  type: string
- description: ''
  name: ChecksumAlgorithm
  type: array
- description: ''
  name: RestoreStatus
  type: object
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-object-schema.json
slug: amazon-s3-rest-object
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: Object
---
