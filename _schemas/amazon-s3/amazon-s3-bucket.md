---
description: Schema representing an Amazon S3 bucket resource. A bucket is a container for objects stored in Amazon S3. Every object is contained in a bucket. Buckets serve as the top-level namespace for S3 and provide mechanisms for controlling access, aggregating usage, and reporting.
layout: schema
name: Amazon S3 Bucket
properties_list:
- description: The name of the bucket. Bucket names must be between 3 (min) and 63 (max) characters long, can consist only of lowercase letters, numbers, hyphens (-), and periods (.), and must begin and end with a l
  name: Name
  type: string
- description: Date the bucket was created, in ISO 8601 format.
  name: CreationDate
  type: string
- description: The AWS Region where the bucket is located.
  name: Region
  type: string
- description: ''
  name: Owner
  type: object
- description: The Amazon Resource Name (ARN) of the bucket.
  name: ARN
  type: string
- description: ''
  name: VersioningConfiguration
  type: object
- description: ''
  name: Encryption
  type: object
- description: ''
  name: PublicAccessBlockConfiguration
  type: object
- description: A set of tags associated with the bucket.
  name: Tags
  type: array
- description: Server access logging configuration for the bucket.
  name: LoggingConfiguration
  type: object
- description: Lifecycle configuration for objects in the bucket.
  name: LifecycleConfiguration
  type: object
- description: Cross-Origin Resource Sharing (CORS) configuration for the bucket.
  name: CORSConfiguration
  type: object
- description: Website hosting configuration for the bucket.
  name: WebsiteConfiguration
  type: object
- description: Object Lock configuration for the bucket.
  name: ObjectLockConfiguration
  type: object
- description: Transfer Acceleration configuration for the bucket.
  name: AccelerateConfiguration
  type: object
- description: S3 Intelligent-Tiering configurations for the bucket.
  name: IntelligentTieringConfiguration
  type: array
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-bucket-schema.json
slug: amazon-s3-bucket
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: Amazon S3 Bucket
---
