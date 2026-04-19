---
description: When you update a reference data source configuration for a SQL-based Kinesis Data Analytics application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.
layout: schema
name: ReferenceDataSourceUpdate
properties_list:
- description: ''
  name: ReferenceId
  type: object
- description: ''
  name: TableNameUpdate
  type: object
- description: ''
  name: S3ReferenceDataSourceUpdate
  type: object
- description: ''
  name: ReferenceSchemaUpdate
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-reference-data-source-update-schema.json
slug: amazon-managed-apache-flink-reference-data-source-update
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: ReferenceDataSourceUpdate
---
