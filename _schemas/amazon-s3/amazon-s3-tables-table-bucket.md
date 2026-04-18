---
description: ''
layout: schema
name: TableBucket
properties_list:
- description: The Amazon Resource Name (ARN) of the table bucket.
  name: arn
  type: string
- description: The name of the table bucket.
  name: name
  type: string
- description: The account ID of the owner.
  name: ownerAccountId
  type: string
- description: The date and time when the table bucket was created.
  name: createdAt
  type: string
- description: The unreferenced file removal settings for the table bucket.
  name: unreferencedFileRemoval
  type: object
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-tables-table-bucket-schema.json
slug: amazon-s3-tables-table-bucket
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: TableBucket
---
