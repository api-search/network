---
description: ''
layout: schema
name: NotificationQueueAwsSnsOutbound
properties_list:
- description: Amazon Resource Name (ARN) of the Amazon SNS (SNS) topic to which notifications are pushed.
  name: aws_sns_topic_arn
  type: string
- description: ARN of the IAM role that has permissions to publish messages to the SNS topic.
  name: aws_sns_role_arn
  type: string
- description: ARN for the Snowflake IAM user created for your account.
  name: sf_aws_iam_user_arn
  type: string
- description: External ID for the Snowflake IAM user created for your account.
  name: sf_aws_external_id
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/notification-integration-notification-queue-aws-sns-outbound-schema.json
slug: notification-integration-notification-queue-aws-sns-outbound
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NotificationQueueAwsSnsOutbound
---
