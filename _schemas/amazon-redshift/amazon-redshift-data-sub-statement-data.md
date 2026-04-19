---
description: ''
layout: schema
name: SubStatementData
properties_list:
- description: The identifier of the sub-statement
  name: Id
  type: string
- description: The status of the sub-statement
  name: Status
  type: string
- description: The date and time the sub-statement was created
  name: CreatedAt
  type: string
- description: The date and time the sub-statement was last updated
  name: UpdatedAt
  type: string
- description: The time in nanoseconds the sub-statement ran
  name: Duration
  type: integer
- description: The SQL statement text
  name: QueryString
  type: string
- description: The Redshift query identifier
  name: RedshiftQueryId
  type: integer
- description: Total number of rows in the result set
  name: ResultRows
  type: integer
- description: The size of the result set in bytes
  name: ResultSize
  type: integer
- description: Whether the sub-statement has a result set
  name: HasResultSet
  type: boolean
- description: The error message if the sub-statement failed
  name: Error
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-sub-statement-data-schema.json
slug: amazon-redshift-data-sub-statement-data
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
title: SubStatementData
---
