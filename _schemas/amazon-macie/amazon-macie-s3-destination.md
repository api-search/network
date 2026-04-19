---
description: Specifies an S3 bucket to store data classification results in, and the encryption settings to use when storing results in that bucket.
layout: schema
name: S3Destination
properties_list:
- description: ''
  name: bucketName
  type: object
- description: ''
  name: keyPrefix
  type: object
- description: ''
  name: kmsKeyArn
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-s3-destination-schema.json
slug: amazon-macie-s3-destination
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: S3Destination
---
