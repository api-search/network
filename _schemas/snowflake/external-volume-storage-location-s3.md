---
description: ''
layout: schema
name: StorageLocationS3
properties_list:
- description: Specifies the case-sensitive Amazon Resource Name (ARN) of the AWS identity and access management (IAM) role that grants privileges on the S3 bucket containing your data files.
  name: storage_aws_role_arn
  type: string
- description: Specifies the base URL for your cloud storage location.
  name: storage_base_url
  type: string
- description: Optionally specifies an external ID that Snowflake uses to establish a trust relationship with AWS.
  name: storage_aws_external_id
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/external-volume-storage-location-s3-schema.json
slug: external-volume-storage-location-s3
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: StorageLocationS3
---
