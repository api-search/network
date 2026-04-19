---
description: Amazon SNS topic for completion status notifications.
layout: schema
name: NotificationChannel
properties_list:
- description: The Amazon SNS topic ARN to post completion status.
  name: SNSTopicArn
  type: string
- description: The ARN of an IAM role that gives Rekognition publishing permissions.
  name: RoleArn
  type: string
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
schema_file: json-schema/amazon-rekognition-notification-channel-schema.json
slug: amazon-rekognition-notification-channel
tags:
- AWS
- Celebrity Recognition
- Computer Vision
- Content Moderation
- Custom Labels
- Deep Learning
- Face Liveness
- Facial Recognition
- Image Analysis
- Machine Learning
- Object Detection
- Text Detection
- Video Analysis
title: NotificationChannel
---
