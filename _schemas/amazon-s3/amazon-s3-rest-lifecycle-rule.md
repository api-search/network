---
description: A lifecycle rule for individual objects in an Amazon S3 bucket.
layout: schema
name: LifecycleRule
properties_list:
- description: Unique identifier for the rule.
  name: ID
  type: string
- description: The filter used to identify objects for the rule.
  name: Filter
  type: object
- description: If Enabled, Amazon S3 executes the lifecycle actions. If Disabled, Amazon S3 ignores the lifecycle actions.
  name: Status
  type: string
- description: ''
  name: Expiration
  type: object
- description: ''
  name: Transition
  type: array
- description: ''
  name: NoncurrentVersionExpiration
  type: object
- description: ''
  name: NoncurrentVersionTransition
  type: array
- description: ''
  name: AbortIncompleteMultipartUpload
  type: object
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-lifecycle-rule-schema.json
slug: amazon-s3-rest-lifecycle-rule
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: LifecycleRule
---
