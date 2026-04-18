---
description: The container for the completed multipart upload response.
layout: schema
name: CompleteMultipartUploadResult
properties_list:
- description: The URI that identifies the newly created object.
  name: Location
  type: string
- description: The name of the bucket that contains the newly created object.
  name: Bucket
  type: string
- description: The object key of the newly created object.
  name: Key
  type: string
- description: Entity tag that identifies the newly created object's data.
  name: ETag
  type: string
- description: ''
  name: ChecksumCRC32
  type: string
- description: ''
  name: ChecksumCRC32C
  type: string
- description: ''
  name: ChecksumSHA1
  type: string
- description: ''
  name: ChecksumSHA256
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-complete-multipart-upload-result-schema.json
slug: amazon-s3-rest-complete-multipart-upload-result
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: CompleteMultipartUploadResult
---
