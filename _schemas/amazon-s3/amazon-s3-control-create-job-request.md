---
description: ''
layout: schema
name: CreateJobRequest
properties_list:
- description: The action that you want the job to perform on each object.
  name: Operation
  type: object
- description: Configuration parameters for the optional completion report for the job.
  name: Report
  type: object
- description: Configuration parameters for the manifest.
  name: Manifest
  type: object
- description: The numerical priority for this job.
  name: Priority
  type: integer
- description: The Amazon Resource Name (ARN) for the IAM role.
  name: RoleArn
  type: string
- description: A description for this job.
  name: Description
  type: string
- description: Indicates whether confirmation is required before Amazon S3 runs the job.
  name: ConfirmationRequired
  type: boolean
- description: ''
  name: Tags
  type: array
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-control-create-job-request-schema.json
slug: amazon-s3-control-create-job-request
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: CreateJobRequest
---
