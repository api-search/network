---
description: The <code>PublicAccessBlock</code> configuration to apply to this Amazon S3 bucket. If the proposed configuration is for an existing Amazon S3 bucket and the configuration is not specified, the access preview uses the existing setting. If the proposed configuration is for a new bucket and the configuration is not specified, the access preview uses <code>false</code>. If the proposed configuration is for a new access point or multi-region access point and the access point BPA configuration is not specified, the access preview uses <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html">PublicAccessBlockConfiguration</a>.
layout: schema
name: S3PublicAccessBlockConfiguration
properties_list:
- description: ''
  name: ignorePublicAcls
  type: object
- description: ''
  name: restrictPublicBuckets
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-s3-public-access-block-configuration-schema.json
slug: iam-access-analyzer-s3-public-access-block-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: S3PublicAccessBlockConfiguration
---
