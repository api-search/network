---
description: ''
layout: schema
name: AccessGrantsInstance
properties_list:
- description: The ID of the S3 Access Grants instance.
  name: AccessGrantsInstanceId
  type: string
- description: The Amazon Resource Name (ARN) of the S3 Access Grants instance.
  name: AccessGrantsInstanceArn
  type: string
- description: The date and time when the instance was created.
  name: CreatedAt
  type: string
- description: If you associated your S3 Access Grants instance with an IAM Identity Center instance, this field returns the ARN of the IAM Identity Center instance application.
  name: IdentityCenterArn
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-control-access-grants-instance-schema.json
slug: amazon-s3-control-access-grants-instance
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: AccessGrantsInstance
---
