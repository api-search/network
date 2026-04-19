---
description: Access control configuration structures for your resource. You specify the configuration as a type-value pair. You can specify only one type of access control configuration.
layout: schema
name: Configuration
properties_list:
- description: ''
  name: ebsSnapshot
  type: object
- description: ''
  name: ecrRepository
  type: object
- description: ''
  name: iamRole
  type: object
- description: ''
  name: efsFileSystem
  type: object
- description: ''
  name: kmsKey
  type: object
- description: ''
  name: rdsDbClusterSnapshot
  type: object
- description: ''
  name: rdsDbSnapshot
  type: object
- description: ''
  name: secretsManagerSecret
  type: object
- description: ''
  name: s3Bucket
  type: object
- description: ''
  name: snsTopic
  type: object
- description: ''
  name: sqsQueue
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-configuration-schema.json
slug: iam-access-analyzer-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: Configuration
---
