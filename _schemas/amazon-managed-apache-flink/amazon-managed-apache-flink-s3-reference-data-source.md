---
description: <p>For a SQL-based Kinesis Data Analytics application, identifies the Amazon S3 bucket and object that contains the reference data.</p> <p>A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the <a>UpdateApplication</a> operation to trigger reloading of data into your application. </p>
layout: schema
name: S3ReferenceDataSource
properties_list:
- description: ''
  name: BucketARN
  type: object
- description: ''
  name: FileKey
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-s3-reference-data-source-schema.json
slug: amazon-managed-apache-flink-s3-reference-data-source
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: S3ReferenceDataSource
---
