---
description: Proposed access control configuration for an Amazon S3 bucket. You can propose a configuration for a new Amazon S3 bucket or an existing Amazon S3 bucket that you own by specifying the Amazon S3 bucket policy, bucket ACLs, bucket BPA settings, Amazon S3 access points, and multi-region access points attached to the bucket. If the configuration is for an existing Amazon S3 bucket and you do not specify the Amazon S3 bucket policy, the access preview uses the existing policy attached to the bucket. If the access preview is for a new resource and you do not specify the Amazon S3 bucket policy, the access preview assumes a bucket without a policy. To propose deletion of an existing bucket policy, you can specify an empty string. For more information about bucket policy limits, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html">Bucket Policy Examples</a>.
layout: schema
name: S3BucketConfiguration
properties_list:
- description: ''
  name: bucketPolicy
  type: object
- description: ''
  name: bucketAclGrants
  type: object
- description: ''
  name: bucketPublicAccessBlock
  type: object
- description: ''
  name: accessPoints
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-s3-bucket-configuration-schema.json
slug: iam-access-analyzer-s3-bucket-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: S3BucketConfiguration
---
