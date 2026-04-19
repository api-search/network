---
description: An Amazon Kinesis data stream.
layout: schema
name: Stream
properties_list:
- description: The name of the stream.
  name: StreamName
  type: string
- description: The Amazon Resource Name (ARN) for the stream.
  name: StreamARN
  type: string
- description: The current status.
  name: StreamStatus
  type: string
- description: The current retention period, in hours.
  name: RetentionPeriodHours
  type: integer
- description: The approximate time the stream was created.
  name: StreamCreationTimestamp
  type: string
provider_name: Amazon Kinesis
provider_slug: amazon-kinesis
schema_file: json-schema/amazon-kinesis-stream-schema.json
slug: amazon-kinesis-stream
tags:
- Analytics
- Big Data
- Data Processing
- Real-Time
- Streaming
title: Stream
---
