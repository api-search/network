---
description: For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.
layout: schema
name: ReferenceDataSource
properties_list:
- description: ''
  name: TableName
  type: object
- description: ''
  name: S3ReferenceDataSource
  type: object
- description: ''
  name: ReferenceSchema
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-reference-data-source-schema.json
slug: amazon-managed-apache-flink-reference-data-source
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: ReferenceDataSource
---
