---
description: An Amazon Kinesis Data Firehose delivery stream.
layout: schema
name: DeliveryStream
properties_list:
- description: The name of the delivery stream.
  name: DeliveryStreamName
  type: string
- description: The ARN of the delivery stream.
  name: DeliveryStreamARN
  type: string
- description: The status of the delivery stream.
  name: DeliveryStreamStatus
  type: string
- description: The type of the delivery stream.
  name: DeliveryStreamType
  type: string
- description: The date and time the delivery stream was created.
  name: CreateTimestamp
  type: string
- description: The date and time the delivery stream was last updated.
  name: LastUpdateTimestamp
  type: string
provider_name: Amazon Kinesis Data Firehose
provider_slug: amazon-kinesis-firehose
schema_file: json-schema/amazon-kinesis-firehose-delivery-stream-schema.json
slug: amazon-kinesis-firehose-delivery-stream
tags:
- Analytics
- AWS
- Data Delivery
- Streaming
title: DeliveryStream
---
