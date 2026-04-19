---
description: ''
layout: schema
name: PublishBatchRequestEntry
properties_list:
- description: An identifier for the message in this batch. The Id must be unique within a single PublishBatch request.
  name: Id
  type: string
- description: The body of the message
  name: Message
  type: string
- description: The subject of the batch message for email endpoints
  name: Subject
  type: string
- description: Set to json for per-protocol messages
  name: MessageStructure
  type: string
- description: Message attributes for this entry
  name: MessageAttributes
  type: object
- description: Deduplication ID for FIFO topics
  name: MessageDeduplicationId
  type: string
- description: Message group ID for FIFO topics
  name: MessageGroupId
  type: string
provider_name: Amazon SNS
provider_slug: amazon-sns
schema_file: json-schema/amazon-sns-publish-batch-request-entry-schema.json
slug: amazon-sns-publish-batch-request-entry
tags:
- AWS
- Email
- Messaging
- Notifications
- Pub/Sub
- Push Notifications
- SMS
title: PublishBatchRequestEntry
---
