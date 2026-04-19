---
description: Specifies which S3 buckets contain the objects that a classification job analyzes, and the scope of that analysis. The bucket specification can be static (bucketDefinitions) or dynamic (bucketCriteria). If it's static, the job analyzes objects in the same predefined set of buckets each time the job runs. If it's dynamic, the job analyzes objects in any buckets that match the specified criteria each time the job starts to run.
layout: schema
name: S3JobDefinition
properties_list:
- description: ''
  name: bucketCriteria
  type: object
- description: ''
  name: bucketDefinitions
  type: object
- description: ''
  name: scoping
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-s3-job-definition-schema.json
slug: amazon-macie-s3-job-definition
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: S3JobDefinition
---
