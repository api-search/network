---
description: CreateTrailRequest schema
layout: schema
name: CreateTrailRequest
properties_list:
- description: The name of the trail.
  name: Name
  type: string
- description: The name of the S3 bucket for log file delivery.
  name: S3BucketName
  type: string
- description: The S3 key prefix for log file delivery.
  name: S3KeyPrefix
  type: string
- description: Whether the trail is created in all regions.
  name: IsMultiRegionTrail
  type: boolean
- description: Whether log file integrity validation is enabled.
  name: EnableLogFileValidation
  type: boolean
- description: The ARN of the CloudWatch Logs log group.
  name: CloudWatchLogsLogGroupArn
  type: string
- description: The role ARN for CloudWatch Logs delivery.
  name: CloudWatchLogsRoleArn
  type: string
provider_name: Amazon CloudTrail
provider_slug: amazon-cloudtrail
schema_file: json-schema/cloudtrail-create-trail-request-schema.json
slug: cloudtrail-create-trail-request
tags:
- AWS
- CloudTrail
- Audit
- Compliance
- Governance
- Security
title: CreateTrailRequest
---
