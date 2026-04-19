---
description: Provides information about the total storage size (in bytes) or number of objects that Amazon Macie can't analyze in one or more S3 buckets. In a BucketMetadata or MatchingBucket object, this data is for a specific bucket. In a GetBucketStatisticsResponse object, this data is aggregated for all the buckets in the query results. If versioning is enabled for a bucket, storage size values are based on the size of the latest version of each applicable object in the bucket.
layout: schema
name: ObjectLevelStatistics
properties_list:
- description: ''
  name: fileType
  type: object
- description: ''
  name: storageClass
  type: object
- description: ''
  name: total
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-object-level-statistics-schema.json
slug: amazon-macie-object-level-statistics
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: ObjectLevelStatistics
---
