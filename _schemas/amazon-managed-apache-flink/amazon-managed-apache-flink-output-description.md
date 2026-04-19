---
description: For a SQL-based Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.
layout: schema
name: OutputDescription
properties_list:
- description: ''
  name: OutputId
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: KinesisStreamsOutputDescription
  type: object
- description: ''
  name: KinesisFirehoseOutputDescription
  type: object
- description: ''
  name: LambdaOutputDescription
  type: object
- description: ''
  name: DestinationSchema
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-output-description-schema.json
slug: amazon-managed-apache-flink-output-description
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: OutputDescription
---
