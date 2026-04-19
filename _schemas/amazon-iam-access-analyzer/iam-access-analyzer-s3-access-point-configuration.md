---
description: The configuration for an Amazon S3 access point or multi-region access point for the bucket. You can propose up to 10 access points or multi-region access points per bucket. If the proposed Amazon S3 access point configuration is for an existing bucket, the access preview uses the proposed access point configuration in place of the existing access points. To propose an access point without a policy, you can provide an empty string as the access point policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html">Creating access points</a>. For more information about access point policy limits, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points-restrictions-limitations.html">Access points restrictions and limitations</a>.
layout: schema
name: S3AccessPointConfiguration
properties_list:
- description: ''
  name: accessPointPolicy
  type: object
- description: ''
  name: publicAccessBlock
  type: object
- description: ''
  name: networkOrigin
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-s3-access-point-configuration-schema.json
slug: iam-access-analyzer-s3-access-point-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: S3AccessPointConfiguration
---
