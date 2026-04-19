---
description: Contains the Amazon Resource Name (ARN) of the resource to publish to, such as an S3 bucket, and the ARN of the KMS key to use to encrypt published findings.
layout: schema
name: DestinationProperties
properties_list:
- description: ''
  name: DestinationArn
  type: object
- description: ''
  name: KmsKeyArn
  type: object
provider_name: Amazon GuardDuty
provider_slug: amazon-guardduty
schema_file: json-schema/guardduty-destination-properties-schema.json
slug: guardduty-destination-properties
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
title: DestinationProperties
---
