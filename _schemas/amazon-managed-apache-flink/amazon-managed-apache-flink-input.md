---
description: When you configure the application input for a SQL-based Kinesis Data Analytics application, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.
layout: schema
name: Input
properties_list:
- description: ''
  name: NamePrefix
  type: object
- description: ''
  name: InputProcessingConfiguration
  type: object
- description: ''
  name: KinesisStreamsInput
  type: object
- description: ''
  name: KinesisFirehoseInput
  type: object
- description: ''
  name: InputParallelism
  type: object
- description: ''
  name: InputSchema
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-input-schema.json
slug: amazon-managed-apache-flink-input
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: Input
---
