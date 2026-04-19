---
description: An Amazon Kinesis Video Stream.
layout: schema
name: Stream
properties_list:
- description: The name of the stream.
  name: StreamName
  type: string
- description: The Amazon Resource Name (ARN) of the stream.
  name: StreamARN
  type: string
- description: The status of the stream.
  name: Status
  type: string
- description: How long the channel retains data (in hours).
  name: DataRetentionInHours
  type: integer
- description: When the stream was created.
  name: CreationTime
  type: string
provider_name: Amazon Kinesis Video Streams
provider_slug: amazon-kinesis-video-streams
schema_file: json-schema/amazon-kinesis-video-streams-stream-schema.json
slug: amazon-kinesis-video-streams-stream
tags:
- AWS
- IoT
- Machine Learning
- Media
- Video Streaming
title: Stream
---
