---
description: '<p>For a SQL-based Kinesis Data Analytics application, provides additional mapping information when the record format uses delimiters, such as CSV. For example, the following sample records use CSV format, where the records use the <i>''\n''</i> as the row delimiter and a comma (",") as the column delimiter: </p> <p> <code>"name1", "address1"</code> </p> <p> <code>"name2", "address2"</code> </p>'
layout: schema
name: CSVMappingParameters
properties_list:
- description: ''
  name: RecordRowDelimiter
  type: object
- description: ''
  name: RecordColumnDelimiter
  type: object
provider_name: Amazon Managed Service for Apache Flink
provider_slug: amazon-managed-apache-flink
schema_file: json-schema/amazon-managed-apache-flink-csv-mapping-parameters-schema.json
slug: amazon-managed-apache-flink-csv-mapping-parameters
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
title: CSVMappingParameters
---
