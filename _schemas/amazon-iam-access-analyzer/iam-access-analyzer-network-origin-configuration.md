---
description: The proposed <code>InternetConfiguration</code> or <code>VpcConfiguration</code> to apply to the Amazon S3 access point. <code>VpcConfiguration</code> does not apply to multi-region access points. You can make the access point accessible from the internet, or you can specify that all requests made through that access point must originate from a specific virtual private cloud (VPC). You can specify only one type of network configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html">Creating access points</a>.
layout: schema
name: NetworkOriginConfiguration
properties_list:
- description: The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see <a href="https://docs.a
  name: vpcConfiguration
  type: object
- description: ''
  name: internetConfiguration
  type: object
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
schema_file: json-schema/iam-access-analyzer-network-origin-configuration-schema.json
slug: iam-access-analyzer-network-origin-configuration
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
title: NetworkOriginConfiguration
---
