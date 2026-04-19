---
description: Provides aggregated statistical data for sensitive data discovery metrics that apply to S3 buckets, grouped by bucket sensitivity score (sensitivityScore). If automated sensitive data discovery is currently disabled for your account, the value for each metric is 0.
layout: schema
name: BucketStatisticsBySensitivity
properties_list:
- description: ''
  name: classificationError
  type: object
- description: ''
  name: notClassified
  type: object
- description: ''
  name: notSensitive
  type: object
- description: ''
  name: sensitive
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-bucket-statistics-by-sensitivity-schema.json
slug: amazon-macie-bucket-statistics-by-sensitivity
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: BucketStatisticsBySensitivity
---
