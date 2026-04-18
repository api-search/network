---
description: The configuration information for the bucket.
layout: schema
name: CreateBucketConfiguration
properties_list:
- description: Specifies the Region where the bucket will be created. If you do not specify a Region, the bucket is created in the us-east-1 Region.
  name: LocationConstraint
  type: string
- description: Specifies the location of the bucket.
  name: Location
  type: object
- description: Specifies the information about the bucket to create.
  name: Bucket
  type: object
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-rest-create-bucket-configuration-schema.json
slug: amazon-s3-rest-create-bucket-configuration
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: CreateBucketConfiguration
---
