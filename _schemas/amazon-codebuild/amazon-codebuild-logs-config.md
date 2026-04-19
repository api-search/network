---
description: Information about logs for a build project. These can be logs in CloudWatch Logs, built in a specified S3 bucket, or both.
layout: schema
name: LogsConfig
properties_list:
- description: ''
  name: cloudWatchLogs
  type: object
- description: ''
  name: s3Logs
  type: object
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
schema_file: json-schema/amazon-codebuild-logs-config-schema.json
slug: amazon-codebuild-logs-config
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
title: LogsConfig
---
