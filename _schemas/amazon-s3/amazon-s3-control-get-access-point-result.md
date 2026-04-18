---
description: ''
layout: schema
name: GetAccessPointResult
properties_list:
- description: The name of the access point.
  name: Name
  type: string
- description: The name of the bucket associated with the access point.
  name: Bucket
  type: string
- description: Indicates whether this access point allows access from the public internet.
  name: NetworkOrigin
  type: string
- description: ''
  name: VpcConfiguration
  type: object
- description: The date and time when the access point was created.
  name: CreationDate
  type: string
- description: The alias for the access point.
  name: Alias
  type: string
- description: The ARN for the access point.
  name: AccessPointArn
  type: string
- description: ''
  name: Endpoints
  type: object
- description: The AWS account ID associated with the S3 bucket.
  name: BucketAccountId
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-control-get-access-point-result-schema.json
slug: amazon-s3-control-get-access-point-result
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: GetAccessPointResult
---
