---
description: Provides information about the number of S3 buckets that are or aren't shared with other Amazon Web Services accounts, Amazon CloudFront origin access identities (OAIs), or CloudFront origin access controls (OACs). In this data, an <i>Amazon Macie organization</i> is defined as a set of Macie accounts that are centrally managed as a group of related accounts through Organizations or by Macie invitation.
layout: schema
name: BucketCountBySharedAccessType
properties_list:
- description: ''
  name: external
  type: object
- description: ''
  name: internal
  type: object
- description: ''
  name: notShared
  type: object
- description: ''
  name: unknown
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-bucket-count-by-shared-access-type-schema.json
slug: amazon-macie-bucket-count-by-shared-access-type
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: BucketCountBySharedAccessType
---
