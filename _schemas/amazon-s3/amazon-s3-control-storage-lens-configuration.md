---
description: A container for the Amazon S3 Storage Lens configuration.
layout: schema
name: StorageLensConfiguration
properties_list:
- description: A container for the Storage Lens configuration ID.
  name: Id
  type: string
- description: A container for the account-level settings for S3 Storage Lens.
  name: AccountLevel
  type: object
- description: ''
  name: Include
  type: object
- description: ''
  name: Exclude
  type: object
- description: ''
  name: DataExport
  type: object
- description: A container for whether the S3 Storage Lens configuration is enabled.
  name: IsEnabled
  type: boolean
- description: ''
  name: AwsOrg
  type: object
- description: ''
  name: StorageLensArn
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-control-storage-lens-configuration-schema.json
slug: amazon-s3-control-storage-lens-configuration
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: StorageLensConfiguration
---
