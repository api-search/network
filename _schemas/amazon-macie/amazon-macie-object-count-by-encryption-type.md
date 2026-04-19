---
description: Provides information about the number of objects that are in an S3 bucket and use certain types of server-side encryption, use client-side encryption, or aren't encrypted.
layout: schema
name: ObjectCountByEncryptionType
properties_list:
- description: ''
  name: customerManaged
  type: object
- description: ''
  name: kmsManaged
  type: object
- description: ''
  name: s3Managed
  type: object
- description: ''
  name: unencrypted
  type: object
- description: ''
  name: unknown
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-object-count-by-encryption-type-schema.json
slug: amazon-macie-object-count-by-encryption-type
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: ObjectCountByEncryptionType
---
