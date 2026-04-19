---
description: Contains information on how the bucker owner's S3 Block Public Access settings are being applied to the S3 bucket. See <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html">S3 Block Public Access</a> for more information.
layout: schema
name: BlockPublicAccess
properties_list:
- description: ''
  name: IgnorePublicAcls
  type: object
- description: ''
  name: RestrictPublicBuckets
  type: object
- description: ''
  name: BlockPublicAcls
  type: object
- description: ''
  name: BlockPublicPolicy
  type: object
provider_name: Amazon GuardDuty
provider_slug: amazon-guardduty
schema_file: json-schema/guardduty-block-public-access-schema.json
slug: guardduty-block-public-access
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
title: BlockPublicAccess
---
