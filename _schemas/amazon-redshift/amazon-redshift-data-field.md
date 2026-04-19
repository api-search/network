---
description: A single value in a result row. Exactly one of the typed properties will be present, corresponding to the column data type.
layout: schema
name: Field
properties_list:
- description: A value in binary format
  name: blobValue
  type: string
- description: A boolean value
  name: booleanValue
  type: boolean
- description: A double-precision floating point value
  name: doubleValue
  type: number
- description: Whether the value is null
  name: isNull
  type: boolean
- description: A long integer value
  name: longValue
  type: integer
- description: A string value
  name: stringValue
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-field-schema.json
slug: amazon-redshift-data-field
tags:
- Analytics
- Big Data
- Cloud
- Data Lake
- Data Warehouse
- ETL
- Machine Learning
- Serverless
- SQL
title: Field
---
