---
description: Actions to execute after the instance launches
layout: schema
name: PostLaunchActions
properties_list:
- description: Deployment type for post-launch actions
  name: deployment
  type: string
- description: S3 bucket for action logs
  name: s3LogBucket
  type: string
- description: S3 key prefix for action logs
  name: s3OutputKeyPrefix
  type: string
- description: CloudWatch log group name
  name: cloudWatchLogGroupName
  type: string
- description: SSM documents to execute
  name: ssmDocuments
  type: array
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-post-launch-actions-schema.json
slug: application-migration-service-post-launch-actions
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: PostLaunchActions
---
