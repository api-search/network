---
description: Provides aggregated statistical data for sensitive data discovery metrics that apply to S3 buckets. Each field contains aggregated data for all the buckets that have a sensitivity score (sensitivityScore) of a specified value or within a specified range (BucketStatisticsBySensitivity). If automated sensitive data discovery is currently disabled for your account, the value for each field is 0.
layout: schema
name: SensitivityAggregations
properties_list:
- description: ''
  name: classifiableSizeInBytes
  type: object
- description: ''
  name: publiclyAccessibleCount
  type: object
- description: ''
  name: totalCount
  type: object
- description: ''
  name: totalSizeInBytes
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-sensitivity-aggregations-schema.json
slug: amazon-macie-sensitivity-aggregations
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: SensitivityAggregations
---
