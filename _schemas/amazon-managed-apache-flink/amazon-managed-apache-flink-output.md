---
description: <p> Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream. </p> <p/>
layout: schema
name: Output
properties_list:
- description: ''
  name: Name
  type: object
- description: ''
  name: KinesisStreamsOutput
  type: object
- description: ''
  name: KinesisFirehoseOutput
  type: object
- description: ''
  name: LambdaOutput
  type: object
- description: ''
  name: DestinationSchema
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-output-schema.json
slug: amazon-managed-apache-flink-output
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: Output
---
