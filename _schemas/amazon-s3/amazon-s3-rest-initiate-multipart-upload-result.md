---
description: Container for response to initiate multipart upload.
layout: schema
name: InitiateMultipartUploadResult
properties_list:
- description: The name of the bucket to which the multipart upload was initiated.
  name: Bucket
  type: string
- description: Object key for which the multipart upload was initiated.
  name: Key
  type: string
- description: ID for the initiated multipart upload. This ID is used in all subsequent multipart upload operations.
  name: UploadId
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-initiate-multipart-upload-result-schema.json
slug: amazon-s3-rest-initiate-multipart-upload-result
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: InitiateMultipartUploadResult
---
