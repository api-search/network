---
description: Provides information about the block public access settings for an S3 bucket. These settings can apply to a bucket at the account or bucket level. For detailed information about each setting, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html">Blocking public access to your Amazon S3 storage</a> in the <i>Amazon Simple Storage Service User Guide</i>.
layout: schema
name: BlockPublicAccess
properties_list:
- description: ''
  name: blockPublicAcls
  type: object
- description: ''
  name: blockPublicPolicy
  type: object
- description: ''
  name: ignorePublicAcls
  type: object
- description: ''
  name: restrictPublicBuckets
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-block-public-access-schema.json
slug: amazon-macie-block-public-access
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: BlockPublicAccess
---
