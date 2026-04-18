---
description: Container for all error elements.
layout: schema
name: Error
properties_list:
- description: The error code is a string that uniquely identifies an error condition. Examples include NoSuchBucket, NoSuchKey, AccessDenied, InvalidBucketName, etc.
  name: Code
  type: string
- description: A human-readable description of the error.
  name: Message
  type: string
- description: The bucket or object that is involved in the error.
  name: Resource
  type: string
- description: Unique identifier for the request.
  name: RequestId
  type: string
- description: A special token to help AWS troubleshoot problems.
  name: HostId
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-error-schema.json
slug: amazon-s3-rest-error
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: Error
---
