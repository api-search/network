---
description: Provides statistical data for sensitive data discovery metrics that apply to an S3 bucket that Amazon Macie monitors and analyzes for your account. The statistics capture the results of automated sensitive data discovery activities that Macie has performed for the bucket. The data is available only if automated sensitive data discovery is currently enabled for your account.
layout: schema
name: ResourceStatistics
properties_list:
- description: ''
  name: totalBytesClassified
  type: object
- description: ''
  name: totalDetections
  type: object
- description: ''
  name: totalDetectionsSuppressed
  type: object
- description: ''
  name: totalItemsClassified
  type: object
- description: ''
  name: totalItemsSensitive
  type: object
- description: ''
  name: totalItemsSkipped
  type: object
- description: ''
  name: totalItemsSkippedInvalidEncryption
  type: object
- description: ''
  name: totalItemsSkippedInvalidKms
  type: object
- description: ''
  name: totalItemsSkippedPermissionDenied
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-resource-statistics-schema.json
slug: amazon-macie-resource-statistics
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: ResourceStatistics
---
