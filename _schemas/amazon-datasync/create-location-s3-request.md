---
description: Request body for creating an Amazon S3 location.
layout: schema
name: Create Location S3 Request
properties_list:
- description: The ARN of the S3 bucket. This ARN uniquely identifies the bucket.
  name: S3BucketArn
  type: string
- description: ''
  name: S3StorageClass
  type: string
- description: ''
  name: Subdirectory
  type: string
- description: ''
  name: S3Config
  type: object
provider_name: Amazon DataSync
provider_slug: amazon-datasync
schema_file: json-schema/create-location-s3-request-schema.json
slug: create-location-s3-request
tags:
- AWS
- Data Transfer
- Migration
- Storage
- Automation
- Hybrid Cloud
title: Create Location S3 Request
---
